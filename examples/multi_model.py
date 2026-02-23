"""Switch between models with one API key via Crazyrouter"""
from openai import OpenAI

client = OpenAI(
    api_key="sk-your-crazyrouter-key",
    base_url="https://crazyrouter.com/v1"
)

models = ["gpt-4o", "claude-sonnet-4-20250514", "gemini-2.5-pro"]
prompt = "Explain quantum computing in one sentence."

for model in models:
    try:
        r = client.chat.completions.create(
            model=model,
            messages=[{"role": "user", "content": prompt}],
            max_tokens=100
        )
        print(f"[{model}]: {r.choices[0].message.content}\n")
    except Exception as e:
        print(f"[{model}]: Error - {e}\n")
