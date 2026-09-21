# 09 — Agents

An agent is a model plus instructions, tools, state, and an execution loop. It is not a person and does not automatically reason reliably. This example uses a tiny JSON tool protocol and a maximum step limit.

```bash
python 09_agents/agent.py --demo
```

**Experiment:** add a safe read-only tool. Do not add arbitrary shell execution or unrestricted file access. Treat prompt injection and tool arguments as untrusted.
