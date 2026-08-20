"""Read-only tests for APES repository contracts.

Run with::

    uv run --with jsonschema python -B -m unittest discover -s tests -v
"""

from __future__ import annotations

import hashlib
import json
import re
import unittest
from collections import Counter
from pathlib import Path
from urllib.parse import unquote

from jsonschema import Draft202012Validator, FormatChecker


ROOT = Path(__file__).resolve().parents[1]
INLINE_LINK = re.compile(r"!?\[[^\]]*\]\(([^)]+)\)")
REFERENCE_LINK = re.compile(r"^\s*\[[^\]]+\]:\s*(\S+)")
HEADING = re.compile(r"^(#{1,6})\s+(.+?)\s*#*\s*$")
SCHEME = re.compile(r"^[A-Za-z][A-Za-z0-9+.-]*:")
TEMPLATE_STAGE_FILES = {
    "Idea": "idea-brief.md",
    "Discovery": "discovery-interview-notes.md",
    "Research": "research-note.md",
    "Validation": "validation-experiment-plan.md",
    "Product": "product-scope-spec.md",
    "Business": "business-viability-brief.md",
    "Engineering": "engineering-change-record.md",
    "Growth": "growth-experiment-record.md",
    "Knowledge": "retrospective-and-learning-record.md",
}
GATE_TRANSITIONS = (
    ("Idea", "Discovery"),
    ("Discovery", "Research"),
    ("Research", "Validation"),
    ("Validation", "Product"),
    ("Product", "Business"),
    ("Business", "Engineering"),
    ("Engineering", "Growth"),
    ("Growth", "Knowledge"),
    ("Knowledge", "Discovery"),
)


def table_columns(line: str) -> list[str]:
    """Split a Markdown table row while preserving escaped pipe characters."""

    return [cell.strip() for cell in re.split(r"(?<!\\)\|", line.strip().strip("|"))]


def linked_repo_path(cell: str, source: Path) -> str:
    """Return one repository-relative Markdown link target from a table cell."""

    match = re.fullmatch(r"\[[^\]]+\]\(([^)]+)\)", cell.strip())
    if match is None:
        raise AssertionError(f"expected one Markdown link, got: {cell}")
    raw = unquote(match.group(1)).partition("#")[0]
    if not raw or SCHEME.match(raw) or raw.startswith("//") or Path(raw).is_absolute():
        raise AssertionError(f"expected a repository-local link, got: {cell}")
    target = (source.parent / raw).resolve()
    try:
        return target.relative_to(ROOT).as_posix()
    except ValueError as error:
        raise AssertionError(f"link target escapes repository: {cell}") from error


def markdown_table(text: str, section: str, headers: tuple[str, ...]) -> list[list[str]]:
    """Return the sole matching Markdown table from one exact level-two section."""

    section_matches = list(
        re.finditer(rf"^## {re.escape(section)}\s*$", text, re.MULTILINE)
    )
    if len(section_matches) != 1:
        raise AssertionError(f"expected one ## {section} section, found {len(section_matches)}")
    start = section_matches[0].end()
    next_section = re.search(r"^## ", text[start:], re.MULTILINE)
    block = text[start : start + next_section.start()] if next_section else text[start:]
    lines = block.splitlines()
    header_indexes = [
        index for index, line in enumerate(lines) if tuple(table_columns(line)) == headers
    ]
    if len(header_indexes) != 1:
        raise AssertionError(
            f"expected one Markdown table with headers {headers} in ## {section}, "
            f"found {len(header_indexes)}"
        )
    rows: list[list[str]] = []
    for line in lines[header_indexes[0] + 2 :]:
        if not line.strip().startswith("|"):
            break
        rows.append(table_columns(line))
    return rows


def visible_lines(text: str) -> list[tuple[int, str]]:
    """Return lines outside fenced code blocks."""

    result: list[tuple[int, str]] = []
    fence: str | None = None
    for number, line in enumerate(text.splitlines(), 1):
        match = re.match(r"^\s*(```|~~~)", line)
        if match:
            marker = match.group(1)
            fence = None if fence == marker else marker if fence is None else fence
            continue
        if fence is None:
            result.append((number, line))
    return result


def heading_slug(value: str) -> str:
    """Approximate GitHub's heading slug rules for repository-local anchors."""

    value = re.sub(r"<[^>]*>", "", value)
    value = re.sub(r"!?\[([^\]]+)\]\([^)]+\)", r"\1", value)
    value = value.replace("`", "").lower().strip()
    value = "".join(char for char in value if char.isalnum() or char in " _-")
    return re.sub(r"\s", "-", value)


def anchors_for(path: Path) -> set[str]:
    anchors: set[str] = set()
    duplicates: Counter[str] = Counter()
    for _, line in visible_lines(path.read_text(encoding="utf-8-sig")):
        match = HEADING.match(line)
        if match:
            base = heading_slug(match.group(2))
            suffix = duplicates[base]
            duplicates[base] += 1
            anchors.add(base if suffix == 0 else f"{base}-{suffix}")
        for explicit in re.findall(
            r'<a\s+(?:name|id)=["\']([^"\']+)["\']', line, re.IGNORECASE
        ):
            anchors.add(explicit.lower())
    return anchors


def local_link_targets(source: Path) -> list[tuple[int, str]]:
    targets: list[tuple[int, str]] = []
    for number, line in visible_lines(source.read_text(encoding="utf-8-sig")):
        line_without_code = re.sub(r"`[^`]*`", "", line)
        values = [match.group(1).strip() for match in INLINE_LINK.finditer(line_without_code)]
        reference = REFERENCE_LINK.match(line_without_code)
        if reference:
            values.append(reference.group(1).strip())
        for value in values:
            if value.startswith("<") and value.endswith(">"):
                value = value[1:-1]
            value = re.split(r"\s+[\"']", value, maxsplit=1)[0]
            value = unquote(value)
            if value and not SCHEME.match(value):
                targets.append((number, value))
    return targets


class RepositoryContractTests(unittest.TestCase):
    def test_schema_fixtures_match_documented_expectations(self) -> None:
        schema_path = ROOT / "schemas" / "artifact-metadata.schema.json"
        schema = json.loads(schema_path.read_text(encoding="utf-8"))
        Draft202012Validator.check_schema(schema)
        validator = Draft202012Validator(schema, format_checker=FormatChecker())
        expected_keywords = {
            "missing-owners.json": "required",
            "malformed-version.json": "pattern",
            "type-id-mismatch.json": "oneOf",
            "unexpected-field.json": "additionalProperties",
        }

        valid = sorted((ROOT / "schemas/fixtures/artifact-metadata/valid").glob("*.json"))
        invalid = sorted((ROOT / "schemas/fixtures/artifact-metadata/invalid").glob("*.json"))
        self.assertEqual(4, len(valid))
        self.assertEqual(4, len(invalid))
        for path in valid:
            with self.subTest(fixture=path.name):
                errors = list(validator.iter_errors(json.loads(path.read_text(encoding="utf-8"))))
                self.assertEqual([], errors)
        for path in invalid:
            with self.subTest(fixture=path.name):
                errors = list(validator.iter_errors(json.loads(path.read_text(encoding="utf-8"))))
                self.assertIn(expected_keywords[path.name], {error.validator for error in errors})

    def test_markdown_local_links_and_anchors_resolve(self) -> None:
        markdown = sorted(path for path in ROOT.rglob("*.md") if ".git" not in path.parts)
        broken: list[str] = []
        for source in markdown:
            for line, raw in local_link_targets(source):
                path_part, marker, anchor = raw.partition("#")
                target = source if not path_part else (source.parent / path_part).resolve()
                try:
                    target.relative_to(ROOT)
                except ValueError:
                    broken.append(f"{source.relative_to(ROOT)}:{line} -> {raw} (outside root)")
                    continue
                if not target.exists():
                    broken.append(f"{source.relative_to(ROOT)}:{line} -> {raw} (missing)")
                    continue
                anchor_target = target / "README.md" if target.is_dir() else target
                if marker and anchor and anchor_target.suffix.lower() == ".md":
                    if anchor.lower() not in anchors_for(anchor_target):
                        broken.append(f"{source.relative_to(ROOT)}:{line} -> {raw} (anchor)")
        self.assertEqual([], broken)

    def test_source_register_current_statistics_match_rows(self) -> None:
        path = ROOT / "research/source-register.md"
        text = path.read_text(encoding="utf-8-sig")
        headings = list(re.finditer(r"^## Source Audit Statistics.*$", text, re.MULTILINE))
        self.assertTrue(headings)
        first_statistics = headings[0].start()
        rows = []
        for line in text[:first_statistics].splitlines():
            if line.startswith("| SRC-"):
                columns = table_columns(line)
                self.assertEqual(15, len(columns), line)
                rows.append(columns)
        ids = [row[0] for row in rows]
        self.assertEqual([f"SRC-{number:03d}" for number in range(1, 55)], ids)

        current = text[headings[-1].start() :]
        claim_line = re.search(r"^- Claim verification: \*\*(.+?)\*\*\.\s*$", current, re.MULTILINE)
        reliability_line = re.search(r"^- Source reliability: \*\*(.+?)\*\*\.\s*$", current, re.MULTILINE)
        self.assertIsNotNone(claim_line)
        self.assertIsNotNone(reliability_line)

        actual_claims = Counter(row[13] for row in rows)
        actual_reliability = Counter(row[8] for row in rows)
        declared_claims = {
            key.strip(): value for key, value in re.findall(r"([A-Za-z ]+?)=(\d+)", claim_line.group(1))
        }
        declared_reliability = dict(re.findall(r"([A-E])=(\d+)", reliability_line.group(1)))
        for status in ("Contradicted", "Inaccessible"):
            actual_claims.setdefault(status, 0)
        for level in "ABCDE":
            actual_reliability.setdefault(level, 0)
        self.assertEqual({key: str(value) for key, value in actual_claims.items()}, declared_claims)
        self.assertEqual({key: str(value) for key, value in actual_reliability.items()}, declared_reliability)

    def test_verification_log_records_are_complete_and_current(self) -> None:
        path = ROOT / "research/notes/verification-log.md"
        text = path.read_text(encoding="utf-8-sig")
        header = text.split("## Schema", 1)[0]
        self.assertIn("Sprint 2.4 Targeted Re-verification", header)
        self.assertIn("Last Updated: 2026-08-15", header)
        entries = list(re.finditer(r"^### (VR-\d{3}) —", text, re.MULTILINE))
        self.assertEqual(
            [f"VR-{number:03d}" for number in range(1, 35)],
            [entry.group(1) for entry in entries],
        )
        fields = (
            "Verification ID",
            "Source ID",
            "Original URL",
            "Access Date",
            "Access Result",
            "Claims Checked",
            "Evidence Location",
            "License Checked",
            "Maintenance Checked",
            "Outcome",
            "Notes",
        )
        for number, entry in enumerate(entries):
            end = entries[number + 1].start() if number + 1 < len(entries) else len(text)
            section = text[entry.start() : end]
            with self.subTest(record=entry.group(1)):
                for field in fields:
                    pattern = rf"^- \*\*{re.escape(field)}:\*\*"
                    self.assertIsNotNone(re.search(pattern, section, re.MULTILINE), field)

    def test_coverage_matrix_dimensions_and_distribution(self) -> None:
        matrix = (ROOT / "research/coverage/lifecycle-coverage-matrix.md").read_text(encoding="utf-8-sig")
        lines = matrix.splitlines()
        header_index = next(index for index, line in enumerate(lines) if line.startswith("| Project (S-NN) |"))
        header = table_columns(lines[header_index])
        self.assertEqual(20, len(header))
        rows = []
        for line in lines[header_index + 2 :]:
            if not line.startswith("| **S-"):
                break
            rows.append(table_columns(line))
        self.assertEqual(10, len(rows))
        self.assertTrue(all(len(row) == 20 for row in rows))
        values = Counter(cell for row in rows for cell in row[1:])
        self.assertEqual({"Pri": 24, "Sec": 1, "Part": 7, "N": 15, "—": 143}, values)

        task = (ROOT / "tasks/sprint-03-coverage-map.md").read_text(encoding="utf-8-sig")
        self.assertNotIn("10×18", task)
        self.assertGreaterEqual(task.count("10×19"), 2)

    def test_directory_indexes_include_direct_markdown_children(self) -> None:
        for directory in ("checklists", "commands", "examples", "tasks", "templates"):
            with self.subTest(directory=directory):
                index = ROOT / directory / "README.md"
                text = index.read_text(encoding="utf-8-sig")
                children = sorted(path for path in index.parent.glob("*.md") if path.name != "README.md")
                self.assertTrue(children)
                for child in children:
                    self.assertIn(child.name, text)

    def test_root_navigation_mentions_repository_contract_tests(self) -> None:
        text = (ROOT / "README.md").read_text(encoding="utf-8-sig")
        self.assertIn("tests/README.md", text)

    def test_lifecycle_templates_have_required_metadata(self) -> None:
        metadata_fields = ("Status", "Version", "Owner", "Last Updated", "Purpose")
        for stage, filename in TEMPLATE_STAGE_FILES.items():
            with self.subTest(stage=stage):
                text = (ROOT / "templates" / filename).read_text(encoding="utf-8")
                lines = text.splitlines()
                self.assertRegex(lines[0], r"^# \S")
                self.assertEqual("", lines[1])
                for offset, field in enumerate(metadata_fields, 2):
                    self.assertRegex(lines[offset], rf"^- {re.escape(field)}: \S")
                self.assertIsNone(re.search(r"\b(?:Claude|Codex|Cursor|Copilot)\b", text, re.IGNORECASE))

    def test_lifecycle_template_contracts_match_schema(self) -> None:
        schema = json.loads((ROOT / "schemas/artifact-metadata.schema.json").read_text(encoding="utf-8"))
        schema_types = set(schema["properties"]["type"]["enum"])
        prefix_by_type = {
            branch["properties"]["type"]["const"]: branch["properties"]["id"]["pattern"].removeprefix("^")
            for branch in schema["oneOf"]
        }
        self.assertEqual(schema_types, set(prefix_by_type))

        for stage, filename in TEMPLATE_STAGE_FILES.items():
            with self.subTest(stage=stage):
                text = (ROOT / "templates" / filename).read_text(encoding="utf-8")
                type_match = re.search(r"^- Schema type: `([^`]+)`$", text, re.MULTILINE)
                prefix_match = re.search(r"^- ID prefix: `([^`]+)`$", text, re.MULTILINE)
                self.assertIsNotNone(type_match)
                self.assertIsNotNone(prefix_match)
                artifact_type = type_match.group(1)
                self.assertIn(artifact_type, schema_types)
                self.assertEqual(prefix_by_type[artifact_type], prefix_match.group(1))

    def test_lifecycle_stages_and_stage_gates_are_complete(self) -> None:
        expected_templates = set(TEMPLATE_STAGE_FILES.values())
        actual_templates = {
            path.name for path in (ROOT / "templates").glob("*.md") if path.name != "README.md"
        }
        self.assertEqual(expected_templates, actual_templates)

        expected_gates = {
            f"gate-{number}-{source.lower()}-to-{target.lower()}.md"
            for number, (source, target) in enumerate(GATE_TRANSITIONS, 1)
        }
        actual_gates = {path.name for path in (ROOT / "checklists").glob("gate-*.md")}
        self.assertEqual(expected_gates, actual_gates)

        lifecycle = (ROOT / "docs/lifecycle.md").read_text(encoding="utf-8-sig")
        lifecycle_stages = re.findall(r"^\d+\. \*\*([^*]+)\*\*", lifecycle, re.MULTILINE)
        self.assertEqual(list(TEMPLATE_STAGE_FILES), lifecycle_stages)

        for number, (source, target) in enumerate(GATE_TRANSITIONS, 1):
            with self.subTest(gate=number):
                gate = ROOT / "checklists" / f"gate-{number}-{source.lower()}-to-{target.lower()}.md"
                text = gate.read_text(encoding="utf-8")
                self.assertIn(f"- From stage: **{source}**", text)
                self.assertIn(f"- To stage: **{target}**", text)
                self.assertIn(TEMPLATE_STAGE_FILES[source], text)


    def test_alpha_release_identity_and_license_boundary(self) -> None:
        promise = (
            "`v0.2.0-alpha.1` provides documented and repository-contract-tested "
            "mappings for all nine APES lifecycle stages from canonical "
            "template/checklist inputs to project-owned artifact/gate-record paths. "
            "Internal maintainer dogfood has exercised only the Idea path; the other "
            "eight paths and unaffiliated first-time-user usability remain unverified. "
            "A named human alone records the final gate decision."
        )
        old_promise = "A new user can select one APES lifecycle stage"
        readme = (ROOT / "README.md").read_text(encoding="utf-8-sig")
        getting_started = (ROOT / "docs/getting-started.md").read_text(encoding="utf-8")
        faq = (ROOT / "docs/faq.md").read_text(encoding="utf-8")
        changelog = (ROOT / "CHANGELOG.md").read_text(encoding="utf-8-sig")
        adr = (ROOT / "governance/adr/ADR-0004-apache-2-0-repository-license.md").read_text(
            encoding="utf-8"
        )
        decision = (
            ROOT / "governance/decisions/2026-08-19-v0-2-0-alpha-1-release-candidate.md"
        ).read_text(encoding="utf-8")
        contributing = (ROOT / "CONTRIBUTING.md").read_text(encoding="utf-8-sig")
        license_text = (ROOT / "LICENSE").read_text(encoding="utf-8")

        self.assertIn("- Version: v0.2.0-alpha.1", readme)
        self.assertIn("## [0.2.0-alpha.1] - 2026-08-19", changelog)
        for text in (readme, getting_started, faq, decision):
            self.assertIn(promise, text)
            self.assertNotIn(old_promise, text)
        self.assertFalse((ROOT / "VERSION").exists())
        self.assertIn("Version 2.0, January 2004", license_text)
        self.assertIn("END OF TERMS AND CONDITIONS", license_text)
        for text in (readme, adr, decision, contributing):
            self.assertIn("Apache-2.0", text)
        self.assertIn("documentation, templates, checklists, schemas, fixtures, tests", readme)
        self.assertIn("Third-party material retains", adr)

    def test_getting_started_mvp_navigation_is_complete(self) -> None:
        path = ROOT / "docs/getting-started.md"
        text = path.read_text(encoding="utf-8")
        rows = markdown_table(
            text,
            "Choose One Stage",
            ("Stage", "Canonical Template", "Exit Gate", "Canonical Checklist"),
        )
        actual = [
            (row[0], linked_repo_path(row[1], path), row[2], linked_repo_path(row[3], path))
            for row in rows
        ]
        expected = [
            (
                source,
                f"templates/{TEMPLATE_STAGE_FILES[source]}",
                f"{source} → {target}",
                f"checklists/gate-{number}-{source.lower()}-to-{target.lower()}.md",
            )
            for number, (source, target) in enumerate(GATE_TRANSITIONS, 1)
        ]
        self.assertEqual(expected, actual)
        with self.assertRaises(AssertionError):
            linked_repo_path("[idea-brief.md](https://evil.example/idea-brief.md)", path)
        for value in (
            "APES_SOURCE_ROOT",
            "PROJECT_WORK_ROOT",
            "TEMPLATE_PATH",
            "OUTPUT_PATH",
            "EXIT_GATE_CHECKLIST_PATH",
            "GATE_RECORD_PATH",
            "GATE_DECISION_OWNER",
        ):
            self.assertIn(value, text)
        self.assertIn("inspects every path component without first following links", text)
        self.assertIn("distinguishes a genuinely missing leaf from a dangling link", text)
        self.assertIn("alias or hard link to protected APES source", text)
        self.assertIn("Decision cell is already `Pass`, `Failed`, or `Deferred`", text)
        self.assertIn("Do not begin the next lifecycle stage automatically", text)
        self.assertIn("project-owned", text)

    def test_run_stage_command_requires_explicit_contract(self) -> None:
        path = ROOT / "commands/run-apes-stage.md"
        text = path.read_text(encoding="utf-8")
        required = (
            "STAGE",
            "APES_SOURCE_ROOT",
            "PROJECT_WORK_ROOT",
            "TEMPLATE_PATH",
            "OUTPUT_PATH",
            "EXIT_GATE_CHECKLIST_PATH",
            "GATE_RECORD_PATH",
            "GATE_DECISION_OWNER",
            "STANDARDS_CONTEXT_PATHS",
        )
        for value in required:
            self.assertIn(f"- {value}:", text)
        rows = markdown_table(
            text,
            "Stage Reference",
            ("Stage", "Canonical Template", "Exit-Gate Checklist"),
        )
        actual = [
            (row[0], linked_repo_path(row[1], path), linked_repo_path(row[2], path))
            for row in rows
        ]
        expected = [
            (
                source,
                f"templates/{TEMPLATE_STAGE_FILES[source]}",
                f"checklists/gate-{number}-{source.lower()}-to-{target.lower()}.md",
            )
            for number, (source, target) in enumerate(GATE_TRANSITIONS, 1)
        ]
        self.assertEqual(expected, actual)
        for phrase in (
            "before any file creation or update",
            "match the same Stage Reference row",
            "nearest existing ancestor",
            "link-aware metadata",
            "dangling link is a hard stop",
            "including a link at the final leaf",
            "descendants of the resolved `PROJECT_WORK_ROOT`",
            "shares file identity with any protected source file",
            "hard link cannot bypass protection",
            "Decision cell in its Gate Record table",
            "stop before changing the artifact or gate record",
            "new `GATE_RECORD_PATH`",
            "do not create or modify any file",
            "stop without guessing a replacement",
        ):
            self.assertIn(phrase, text)
        self.assertIn("Treat both canonical APES files as read-only", text)
        self.assertIn("Only the named human GATE_DECISION_OWNER", text)
        self.assertIn("Stop after the handoff", text)
        self.assertNotIn("PATH_TO_STANDARDS_MODULE", text)
        self.assertNotIn("together with the repository's", text)

    def test_templates_and_gates_are_copy_safe(self) -> None:
        templates = (ROOT / "templates/README.md").read_text(encoding="utf-8")
        checklists = (ROOT / "checklists/README.md").read_text(encoding="utf-8")
        self.assertIn("read-only APES reference", templates)
        self.assertIn("OUTPUT_PATH", templates)
        self.assertIn("read-only APES references", checklists)
        self.assertIn("GATE_RECORD_PATH", checklists)
        self.assertIn("GATE_DECISION_OWNER", checklists)

        required_sections = (
            "## Working Copy Rule",
            "## Entry Artifacts",
            "## Required Evidence",
            "## Gate Checklist",
            "## Failure and Compensating Evidence",
            "## Gate Record",
        )
        for number, (source, target) in enumerate(GATE_TRANSITIONS, 1):
            gate = ROOT / "checklists" / f"gate-{number}-{source.lower()}-to-{target.lower()}.md"
            text = gate.read_text(encoding="utf-8")
            with self.subTest(gate=number):
                for section in required_sections:
                    self.assertIn(section, text)
                self.assertIn("never mark or decide the canonical APES file", text)
                self.assertIn("GATE_DECISION_OWNER", text)

        release = (ROOT / "checklists/release-readiness.md").read_text(encoding="utf-8")
        readiness_path = ROOT / "examples/v0.2.0-alpha.1-maintainer-release-readiness.md"
        readiness = readiness_path.read_text(encoding="utf-8")
        self.assertIn("This is a canonical APES checklist", release)
        self.assertIn("Ready for Maintainer Decision", release)
        self.assertNotIn("- [x]", release)
        self.assertIn("Gate 1 result of `Pending`, `Failed`, or `Deferred`", release)
        self.assertIn("makes the candidate ineligible for `Release`", release)
        self.assertTrue(readiness_path.exists())
        self.assertIn("../checklists/release-readiness.md", readiness)
        self.assertIn("- Gate decision owner: `longyuan`", readiness)
        self.assertIn("- Candidate decision owner: `longyuan`", readiness)
        self.assertIn("## Human Decisions", readiness)
        self.assertIn("Ineligible for `Release` until a later Gate 1 `Pass`", readiness)

        task = (ROOT / "tasks/release-v0-2-0-alpha-1-preparation.md").read_text(encoding="utf-8")
        digest_match = re.search(
            r"^- Release-readiness record SHA-256: `([0-9a-f]{64})`$",
            task,
            re.MULTILINE,
        )
        self.assertIsNotNone(digest_match)
        expected_digest = digest_match.group(1) if digest_match is not None else ""
        actual_digest = hashlib.sha256(readiness_path.read_bytes()).hexdigest()
        self.assertEqual(expected_digest, actual_digest)

    def test_alpha_status_and_dogfood_boundaries(self) -> None:
        readme = (ROOT / "README.md").read_text(encoding="utf-8-sig")
        research = (ROOT / "research/README.md").read_text(encoding="utf-8-sig")
        decision = (
            ROOT / "governance/decisions/2026-08-19-v0-2-0-alpha-1-release-candidate.md"
        ).read_text(encoding="utf-8")
        idea = (
            ROOT / "examples/v0.2.0-alpha.1-maintainer-dogfood-idea-brief.md"
        ).read_text(encoding="utf-8")
        gate = (ROOT / "examples/v0.2.0-alpha.1-maintainer-dogfood-gate-1.md").read_text(
            encoding="utf-8"
        )
        readiness = (
            ROOT / "examples/v0.2.0-alpha.1-maintainer-release-readiness.md"
        ).read_text(encoding="utf-8")

        for text in (readme, research, decision):
            self.assertIn("RESEARCH AGAIN", text)
            self.assertIn("In Review", text)
        self.assertIn("F2 remains `In Review / Request changes`", readme)
        self.assertIn("F3 has not started", readme)
        self.assertIn("- Status: Ready for Gate Review", idea)
        self.assertNotIn("- Status: Draft", idea)
        for evidence_id in ("LOCAL-005", "LOCAL-006"):
            self.assertIn(evidence_id, idea)
            self.assertIn(evidence_id, gate)
        gate_criteria = (
            "The Idea brief identifies an evidence-backed signal worth investigating.",
            "Source and access date are present for every asserted fact.",
            "Hypotheses and assumptions are labeled.",
            "Intended outcomes are stated without committing to a solution.",
            "Discovery questions target the highest-impact unknowns.",
            "Out-of-scope boundaries are explicit.",
        )
        for criterion in gate_criteria:
            self.assertIn(criterion, gate)
        self.assertEqual(6, gate.count("| Supported |"))
        self.assertNotIn("`LOCAL-001`–", gate)
        self.assertNotIn("`LOCAL-001` through", gate)
        for text in (idea, gate, readiness):
            self.assertIn("internal acceptance evidence only", text)
            self.assertIn("not adoption evidence", text)
            self.assertIn("not external validation", text)
            self.assertIn("not a roadmap real case", text)
        self.assertIn("other eight", readiness)
        self.assertIn("unaffiliated first-time-user usability remain unverified", readiness)

        gate_headers = (
            "Decision",
            "Decision Owner",
            "Evidence References",
            "Unmet Criteria",
            "Compensating Evidence",
            "Review Date",
        )
        gate_rows = markdown_table(gate, "Gate Record", gate_headers)
        decoy = (
            "| Decision | Decision Owner | Evidence References | Unmet Criteria | "
            "Compensating Evidence | Review Date |\n"
            "| --- | --- | --- | --- | --- | --- |\n"
            "| Pass | not-longyuan | none | none | none | 2099-01-01 |\n\n"
        )
        self.assertEqual(gate_rows, markdown_table(decoy + gate, "Gate Record", gate_headers))
        self.assertEqual(1, len(gate_rows))
        gate_value, gate_owner = gate_rows[0][:2]
        gate_state = "Pending" if gate_value.startswith("Pending human decision:") else gate_value
        self.assertIn(gate_state, {"Pending", "Pass", "Failed", "Deferred"})
        self.assertEqual("longyuan", gate_owner)

        candidate_rows = markdown_table(
            decision,
            "Decision",
            ("Decision", "Decision Owner", "Gate 1 Result", "Evidence", "Date"),
        )
        self.assertEqual(1, len(candidate_rows))
        candidate_value, candidate_owner, candidate_gate = candidate_rows[0][:3]
        candidate_state = "Pending" if candidate_value.startswith("Pending:") else candidate_value
        self.assertIn(candidate_state, {"Pending", "Release", "Hold"})
        self.assertEqual("longyuan", candidate_owner)
        self.assertEqual(gate_state, candidate_gate)
        if candidate_state == "Release":
            self.assertEqual("Pass", gate_state)
        if gate_state in {"Pending", "Failed", "Deferred"}:
            self.assertNotEqual("Release", candidate_state)

        readiness_rows = markdown_table(
            readiness,
            "Human Decisions",
            ("Decision", "Owner", "Eligibility", "Result", "Date"),
        )
        self.assertEqual(2, len(readiness_rows))
        self.assertEqual(["Internal dogfood Gate 1", "Alpha candidate"], [row[0] for row in readiness_rows])
        self.assertTrue(all(row[1] == "longyuan" for row in readiness_rows))
        readiness_gate = (
            "Pending"
            if readiness_rows[0][3].startswith("Pending:")
            else readiness_rows[0][3]
        )
        readiness_candidate = (
            "Pending"
            if readiness_rows[1][3].startswith("Pending:")
            else readiness_rows[1][3]
        )
        self.assertEqual(gate_state, readiness_gate)
        self.assertEqual(candidate_state, readiness_candidate)


if __name__ == "__main__":
    unittest.main()
