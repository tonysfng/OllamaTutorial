import requests
import json

# Set up the base URL for the local Ollama API
url = "http://localhost:12434/engines/llama.cpp/v1/chat/completions"

# Define the payload (your input prompt)
payload = {
    "model": "smollm2:135m",  # Replace with the model name you're using
    "messages": [
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "What is Python?"},
    ],
}

# Send the HTTP POST request with streaming enabled
response = requests.post(url, json=payload)
response.raise_for_status()  # Raise an error for bad responses
print(
    response.json()["choices"][0]["message"]["content"]
)  # Print the JSON response from the API

# Check the response status
