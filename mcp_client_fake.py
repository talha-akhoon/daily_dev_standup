from typing import Dict, Any


class FakeMcpClient:
    """
    Simulate MCP servers + tools.
    TODO: Swap out later for the real thing
    """

    def call(self, server: str, tool: str, params: Dict[str, Any]) -> Dict[str, Any]:
        """
            Return dummy data to test if the LLM returns the correct output
        """
        if server == "github" and tool == "get_activity":
            return {
                "commits": 3,
                "prs_opened": 1,
                "prs_merged": 2,
                "reviews": 1,
                "details": [
                    "Merged PR #123: Fix JWT rotation",
                    "Committed to feature/carrier-bidding",
                ],
                "params_used": params,
            }

        if server == "jira" and tool == "get_updates":
            return {
                "tickets_moved": ["LM-312 Carrier bidding → In Review"],
                "blocked": ["LM-298 OAuth regression waiting on QA"],
                "details": [
                    "Commented on LM-402 API timeout investigation"
                ],
                "params_used": params,
            }

        if server == "calendar" and tool == "get_meetings":
            return {
                "meetings": [
                    {"title": "Daily standup", "duration": 15},
                    {"title": "Partner sync", "duration": 40},
                ],
                "params_used": params,
            }

        return {
            "error": f"Unknown tool {server}.{tool}",
            "params_used": params,
        }
