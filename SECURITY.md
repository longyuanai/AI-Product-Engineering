# AI-Product-Engineering · SECURITY

核实日期：2026-10-15。依据本地README、构建清单和实际入口；本文件不把文档计划当成运行时验收。

## 目标与范围

维护APES工程产物规范、schema、检查清单和交付契约；不把规范仓当运行平台。

GitHub：[longyuanai/AI-Product-Engineering](https://github.com/longyuanai/AI-Product-Engineering)。知识笔记：Vault内 `03_Projects/AI-Product-Engineering/AI-Product-Engineering - Git关联.md`。

## 本项目安全边界

核对artifact metadata契约、示例与schema的一致性；每个检查保留可复现的通过/失败样例。

- 仅处理自有、授权、靶场或CTF资产；未知上传内容按数据处理，不作为脚本执行。
- API Key、Token、主密码、私钥、个人资料、客户数据与运行数据库不进入Git、公开Issue或知识备份。
- 真实外部模型、支付、生产数据库、Telegram/飞书操作与硬件烧录需各自明确授权；默认使用本地夹具。

## 报告与修复

维护者账号：[longyuanai](https://github.com/longyuanai)。敏感问题先使用仓库已启用的私下报告渠道；未确认渠道时，不把敏感原件写入公开Issue。没有编造支持版本或联系邮箱。

记录授权范围、根因、影响、脱敏复现、修复与回归证据；修改前保存可恢复版本。文档完善不等于产品通过全面安全审计。

## 现行依据

- [README.md](README.md)
