






import requests
import json

# Replace 'YOUR_GEMINI_API_KEY' with your actual Gemini API key
GOOGLE_API_KEY = "AIzaSyA4DkeyW9Qwk8gIV0ygke0buwfDcEwtLCM"

# List available models
list_url = f"https://generativelanguage.googleapis.com/v1beta/models?key={GOOGLE_API_KEY}"
resp = requests.get(list_url)
if resp.status_code == 200:
    print("Available models:")
    for m in resp.json().get("models", []):
        print("-", m["name"])
else:
    print("Model list error:", resp.status_code, resp.text)

# Now use the latest available Gemini Pro model for content generation
model_name = "models/gemini-2.5-pro"
url = f"https://generativelanguage.googleapis.com/v1beta/{model_name}:generateContent?key={GOOGLE_API_KEY}"
headers = {"Content-Type": "application/json"}
data = {"contents": [{"parts": [{"text": "Hello, Gemini! help me  in  a  project?"}]}]}
response = requests.post(url, headers=headers, data=json.dumps(data))
if response.status_code == 200:
    result = response.json()
    print("Gemini Response:", result["candidates"][0]["content"]["parts"][0]["text"])
else:
    print("Error:", response.status_code, response.text)
