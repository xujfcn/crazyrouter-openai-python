"""Streaming chat completion with Crazyrouter"""
from openai import OpenAI

client = OpenAI(
    api_key="sk-your-crazyrouter-key",
    base_url="https://crazyrouter.com/v1"
)

stream = client.chat.completions.create(
    model="claude-sonnet-4-20250514",
    messages=[{"role": "user", "content": "Write a short poem about APIs"}],
    stream=True
)

for chunk in stream:
    if chunk.choices[0].delta.content:
        print(chunk.choices[0].delta.content, end="", flush=True)
print()
