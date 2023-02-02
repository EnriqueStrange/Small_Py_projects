import openai

# Replace "YOUR_API_KEY" with your OpenAI API key
openai.api_key = "YOUR_API_KEY"

def generate_text():
    """
    This function generates random meaningful text using OpenAI GPT-3 API
    """
    # Define the prompt or the text to be used as context
    prompt = "Generate a random meaningful sentence"

    # Generate the text using OpenAI API
    generated_text = openai.Completion.create(engine="text-davinci-002", prompt=prompt, max_tokens=1024, n=1, temperature=0.5)["choices"][0]["text"]

    # print the generated text
    print(generated_text)

generate_text()
