import json
from datetime import datetime
from llm import call_llm


def _agent_summarise_with_llm(results: dict) -> str:
    today = datetime.now().strftime("%Y-%m-%d")

    prompt = f"""
You are an engineering standup assistant.

You are given results from MCP tools as JSON.

Write a concise standup for Talha.

Use this structure exactly:

## Today ({today})
- bullet points of concrete work

## Blocked
- bullet points of blockers (or "None")

## Next
- bullet points of next likely steps

Be factual. Do not invent work not supported by the data.

RESULTS:
{json.dumps(results, indent=2)}
"""
    summary = call_llm(prompt).strip()
    summary += "\n\n(Self-check: Summary generated from LLM-planned MCP tool results.)"
    return summary