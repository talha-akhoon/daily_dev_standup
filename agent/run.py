from .plan import _agent_plan_with_llm
from .execute import _agent_execute_plan
from .summarise import _agent_summarise_with_llm


def run_agent():
    log_parts = []

    plan, plan_log = _agent_plan_with_llm()
    log_parts.append("=== PLANNING ===")
    log_parts.append(plan_log)

    results, exec_log = _agent_execute_plan(plan)
    log_parts.append("=== EXECUTING ===")
    log_parts.append(exec_log)

    log_parts.append("\n=== REASONING ===")
    summary = _agent_summarise_with_llm(results)

    agent_log = "\n".join(log_parts)
    return summary, agent_log
