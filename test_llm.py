from openai import OpenAI

client = OpenAI()

response = client.responses.create(
    model="gpt-5.6",
    input="A Linux server is running out of disk space. Give me the first troubleshooting step."
)

print(response.output_text)