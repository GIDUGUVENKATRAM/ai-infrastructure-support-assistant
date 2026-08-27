from openai import OpenAI

client = OpenAI()

print("AI Infrastructure Support Assistant")
print("------")

issue = input(" Describe your infrastructure issue: ")

try:

    response = client.responses.create(
    model="gpt-5.6",
    input=issue
)
    print()
    print("AI Response:")
    print(response.output_text )

except Exception as error:
    print()
    print("Something went wrong while contacting the AI service")
    print("Error:")
    print(error)

