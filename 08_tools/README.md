# 08 — Tools

Tools are ordinary functions exposed through a constrained interface. The model proposes a structured call; application code validates and executes it. The allow-list is the security boundary.

Run `python 08_tools/tool_calling.py`. Never replace the safe calculator with unrestricted shell or `eval` on untrusted input.
