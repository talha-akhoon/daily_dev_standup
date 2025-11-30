from typing import Tuple
from dotenv import load_dotenv
import gradio as gr

load_dotenv()

def run_agent() -> Tuple[str, str]:
    """
    Full agent loop:
    1) LLM-planned tool usage
    2) Execute plan via MCP
    3) LLM reasoning over results
    4) Return (summary, agent_log)
    """
    agent_log: str = ''
    summary: str = ''

    return summary, agent_log

with gr.Blocks(title="Daily Dev Recap Agent") as demo:
    gr.Markdown("## 🤖 Daily Dev Recap (MCP-style Agent)")
    gr.Markdown(
        "This demo shows an LLM-planned agent calling MCP tools "
        "from GitHub, Jira and Google Calendar "
        "and generating a standup summary."
    )

    with gr.Row():
        with gr.Column():
            agent_log_box = gr.Textbox(
                label="Agent Log",
                lines=24,
                interactive=False,
                show_label=True,
            )
        with gr.Column():
            summary_box = gr.Textbox(
                label="Standup Summary",
                lines=24,
                interactive=False,
                show_label=True,
            )

    generate_btn = gr.Button("Generate Recap (Agent)")

    def on_click():
        summary, log = run_agent()
        return log, summary

    generate_btn.click(
        fn=on_click,
        inputs=[],
        outputs=[agent_log_box, summary_box],
    )

if __name__ == "__main__":
    demo.launch()
