import json
from typing import Dict, Any, List, Tuple
from llm import call_llm


def _agent_plan_with_llm() -> Tuple[List[Dict[str, Any]], str]:
    """
    Ask the LLM which tools to call and in what order.
    Returns (plan, log_fragment).
    """
    prompt = """
You are an autonomous engineering assistant.

Goal: generate a daily developer standup summary.

You have these MCP tools available:

- github.get_activity(day: str)
- jira.get_updates(day: str)
- calendar.get_meetings(day: str)

Decide which tools are needed and in what order to best achieve the goal.

Return ONLY valid JSON in this format:

{
  "plan": [
    {"tool": "github.get_activity", "args": {"day": "today"}},
    {"tool": "jira.get_updates", "args": {"day": "today"}},
    {"tool": "calendar.get_meetings", "args": {"day": "today"}}
  ]
}
"""
    raw = call_llm(prompt)
    log = f"PLAN RAW FROM LLM:\n{raw}\n"

    try:
        data = json.loads(raw)
        plan = data.get("plan", [])
        if not isinstance(plan, list):
            raise ValueError("plan is not a list")
    except Exception as e:
        log += f"\n[WARN] Failed to parse plan JSON ({e}), using fallback plan.\n"
        plan = []

    return plan, log
