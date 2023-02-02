import requests # Import the requests module
import json # Import the json module

# Define the API endpoint for DALL-E
url = "https://api.openai.com/v1/images/generations"

# Define the API key for OpenAI
api_key = "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"

# Define the header for the API request
headers = {
    "Content-Type": "application/json",
    "Authorization": f"Bearer {api_key}" # Use f-strings to insert the API key into the header
}

# Define the prompt for DALL-E
prompt = input("Enter the prompt for DALL-E: ") 

# Define the payload for the API request
payload = {
    "model": "image-alpha-001",
    "prompt": prompt,
    "num_images": 1, # Only generate one image
    "size": "1024x1024" # Specify the size of the image
}

# Send the API request
response = requests.post(url, headers=headers, data=json.dumps(payload))

# Check the status code of the response
if response.status_code == 200:
    # Extract the image from the response
    image = response.json()["data"][0]["url"]

    # Download the image from the URL
    binary_image = requests.get(image).content

    # Write the binary image to a PNG file
    with open("image.png", "wb") as f:
        f.write(binary_image)

    print("Image saved successfully!")
else:
    # Print the error message
    print(response.json()["message"])
