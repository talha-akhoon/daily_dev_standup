import json
from typing import Dict, Any, List, Tuple
from mcp_client_fake import FakeMcpClient

mcp = FakeMcpClient()


def _agent_execute_plan(plan: List[Dict[str, Any]]) -> Tuple[Dict[str, Any], str]:
    """
    Execute the LLM-generated plan using FakeMcpClient.
    Returns (results, log_fragment).
    """
    results: Dict[str, Any] = {}
    logs: List[str] = ["\nEXECUTION:"]

    for step in plan:
        tool_full = step.get("tool", "")
        args = step.get("args", {})

        if "." not in tool_full:
            logs.append(f"[SKIP] Invalid tool name: {tool_full}")
            continue

        server, tool = tool_full.split(".", 1)

        logs.append(f"REQUEST → {tool_full}({args})")
        res = mcp.call(server, tool, args)
        logs.append(f"RESPONSE ← {json.dumps(res)}")
        results[tool_full] = res

    return results, "\n".join(logs)
