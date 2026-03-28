# Hugging Face Cursor plugin

How the **Hugging Face** Cursor plugin is set up and how to use it.

## What the plugin adds

### Agent skills (specialized playbooks)

These are instruction packs the agent can follow for HF-specific work. Trigger them with **`/skill-name`** in chat, or the agent can pick them up when your task matches (Hub CLI, datasets, training, etc.).

| Skill | Role |
|--------|------|
| **hf-cli** | Hub CLI (`hf`) — repos, models, datasets, Spaces; replaces deprecated `huggingface-cli`. |
| **hugging-face-dataset-viewer** | Dataset Viewer API — splits, paging, search, filters, parquet URLs, stats. |
| **hugging-face-datasets** | Create/manage Hub datasets — init, configs, streaming updates, SQL-style work. |
| **hugging-face-evaluation** | Evals on model cards, Artificial Analysis, vLLM/lighteval, model-index metadata. |
| **hugging-face-jobs** | Run jobs on HF Jobs — UV scripts, Docker, hardware, cost, secrets, timeouts. |
| **hugging-face-model-trainer** | TRL training on Jobs — SFT/DPO/GRPO, GGUF, Trackio, Hub auth. |
| **hugging-face-paper-publisher** | Paper pages on the Hub, linking models/datasets, markdown articles. |
| **hugging-face-tool-builder** | Scripts that chain HF APIs for repeatable fetch/enrich pipelines. |
| **hugging-face-trackio** | Experiment logging, dashboards, alerts, CLI/JSON for automation. |
| **gradio** | Building Gradio UIs and demos in Python. |

### Subagents

**`agents`** — extra agent routing for heavier or multi-step HF workflows (invoke with **`/agents`** or the agent may choose it when appropriate).

### Rules and hooks

Anything the plugin ships as **rules** or **hooks** applies in the background; you do not run those yourself.

### MCP server: `huggingface-skills`

This exposes **tools** (beyond what is in the skills text) for the agent to call. The server’s **`STATUS.md`** indicates it **expects authentication** via the **`mcp_auth`** tool on server **`plugin-huggingface-skills-huggingface-skills`** with an empty arguments object: `{}`.

Until Hugging Face MCP auth completes in Cursor, Hub-backed **MCP tools** from this server may be limited; **skills** and **`/…` commands** still guide the agent using the skill docs and other tooling.

## How to drive it

1. **Slash commands** — Use **`/`** and pick a skill (e.g. **`/hf-cli`**, **`/hugging-face-jobs`**) or subagent (**`/agents`**) when you want that mode explicitly.
2. **Natural language** — Describe the task (“fine-tune with TRL on HF Jobs”, “query this dataset via the viewer API”); the agent should attach the right skill.
3. **MCP** — After **`mcp_auth`** succeeds, the **`huggingface-skills`** server’s tools become fully available to the agent for API-backed actions.

To finish setup, complete **MCP authentication** for **`plugin-huggingface-skills-huggingface-skills`** when Cursor prompts you, or retry from MCP settings.
