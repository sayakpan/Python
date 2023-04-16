import openai_secret_manager
import openai

# Get your API key from the OpenAI secrets manager
api_key = "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"
openai.api_key = api_key

# Define the parameters for the Completion API
model = "text-davinci-003"
max_tokens = 1024
temperature = 0.7

# Call the Completion API
def ask_gpt(prompt):
    response = openai.Completion.create(
        engine=model,
        prompt=prompt,
        max_tokens=max_tokens,
        temperature=temperature,
    )
    # Print the response
    return response.choices[0].text.strip()


response = ask_gpt("hi")
print("ChatGPT:", response)

# Start the conversation
print("Hello, I'm ChatGPT! Let's chat.")

# prompt = input("You: ")
# print(prompt)
# response = ask_gpt(prompt)
# print("ChatGPT:", response)
