import os
import requests
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

def process_prompt_and_post(prompt):
    """
    Sends a prompt to the Perplexity AI API and posts the response to Ghost.

    Args:
        prompt (str): The text prompt to send to Perplexity AI.
    """
    # Step 1: Send the prompt to Perplexity AI
    perplexity_url = "https://api.perplexity.ai/v1/chat/completions"
    headers = {
        "Authorization": f"Bearer {os.getenv('PERPLEXITY_API_KEY')}",
        "Content-Type": "application/json"
    }
    data = {
        "model": "gpt-3.5-turbo",  # or any other model you want to use
        "messages": [{"role": "user", "content": prompt}]
    }

    response = requests.post(perplexity_url, headers=headers, json=data)
    
    if response.status_code != 200:
        print("Error contacting Perplexity API:", response.text)
        return

    # Step 2: Extract the response from Perplexity AI
    perplexity_response = response.json()
    generated_text = perplexity_response['choices'][0]['message']['content']

    # Step 3: Post the response to Ghost
    ghost_url = os.getenv('GHOST_API_POST_URL')
    ghost_headers = {
        "Authorization": f"Ghost {os.getenv('GHOST_API_KEY')}",
        "Content-Type": "application/json"
    }
    ghost_data = {
        "posts": [{
            "title": "Response from Perplexity AI",
            "html": generated_text
        }]
    }

    ghost_response = requests.post(ghost_url, headers=ghost_headers, json=ghost_data)

    if ghost_response.status_code == 201:
        print("Successfully posted to Ghost!")
    else:
        print("Error posting to Ghost:", ghost_response.text)

# Example usage
if __name__ == "__main__":
    prompt = "What are the latest advancements in AI?"
    process_prompt_and_post(prompt)
