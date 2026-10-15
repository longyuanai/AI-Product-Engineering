# AI-Product-Engineering · ARCHITECTURE

核实日期：2026-10-15。依据本地README、构建清单和实际入口；本文件不把文档计划当成运行时验收。

## 目标与范围

维护APES工程产物规范、schema、检查清单和交付契约；不把规范仓当运行平台。

GitHub：[longyuanai/AI-Product-Engineering](https://github.com/longyuanai/AI-Product-Engineering)。知识笔记：Vault内 `03_Projects/AI-Product-Engineering/AI-Product-Engineering - Git关联.md`。

## 组件与代码入口

| 实际路径 | 责任边界 |
| --- | --- |
| [schemas](schemas) | 产物契约 |
| [scripts](scripts) | 作者/运维工具 |
| [tests](tests) | 测试 |
| [docs](docs) | 工程规范与说明 |

## 数据与控制流

以下链路对应README/规范描述；实现覆盖以代码入口和适用验证为准。

```mermaid
flowchart LR
    N0["规范与schema"]
    N1["项目产物"]
    N2["契约检查"]
    N3["证据和审阅"]
    N0 --> N1
    N1 --> N2
    N2 --> N3
```

## 构建与依赖依据

按README和各子目录清单运行；文档/静态/脚本项目不额外引入构建框架。

## 验证边界

核对artifact metadata契约、示例与schema的一致性；每个检查保留可复现的通过/失败样例。

## 现行依据

- [README.md](README.md)
