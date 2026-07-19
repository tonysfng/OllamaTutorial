from openAI import OpenAI

BASE_URL = "http://localhost:12434/engines/llama.cpp/v1/"

client = OpenAI(base_url=BASE_URL, api_key="YOUR_API_KEY")

MODEL_NAME = "smollm2:135m"
Prompt = "Write a short story about a brave knight and a dragon."

message = [{"role": "user", "content": Prompt}]
response = client.chat.completions.create(model=MODEL_NAME, messages=message)

print(response.choices[0].message.content)
