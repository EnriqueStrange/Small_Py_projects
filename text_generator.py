import openai

openai.api_key = "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"

def generate_text():
    prompt = "Generate a random meaningful sentence"
    generated_text = openai.Completion.create(engine="text-davinci-002", prompt=prompt, max_tokens=1024, n=1, temperature=0.5)["choices"][0]["text"]
    print(generated_text)

generate_text()