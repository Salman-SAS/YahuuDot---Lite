from google import genai

client = genai.Client(api_key="Thank you for reading my project ")

for m in client.models.list():
    print(m.name)
