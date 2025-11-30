from config import OPENAI_API_KEY

def call_llm(prompt: str) -> str:
    """
    Central LLM call.
    """
    return _call_llm_openai(prompt)


def _call_llm_openai(prompt: str) -> str:
    from openai import OpenAI

    client = OpenAI(api_key=OPENAI_API_KEY)
    resp = client.chat.completions.create(
        model="gpt-5-mini",
        messages=[{"role": "user", "content": prompt}],
    )
    return resp.choices[0].message.content