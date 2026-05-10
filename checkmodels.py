from google import genai

client = genai.Client(api_key="AIzaSyDvBYNHTE2t7s8zA0IkeCRu6eDQ0U5GxLE")

for m in client.models.list():
    print(m.name)