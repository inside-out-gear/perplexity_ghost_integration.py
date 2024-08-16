# Perplexity AI to Ghost Post Automation

This Python script automates the process of sending a text prompt to the Perplexity AI API, retrieving the generated response, and posting it to a Ghost blog via its API. 

## Features

- Sends a user-defined prompt to the Perplexity AI API.
- Retrieves and processes the AI-generated response.
- Posts the response as a draft on a Ghost blog.
- Securely manages API keys using environment variables.

## Requirements

- Python 3.x
- `requests` library
- `python-dotenv` library

## Installation

1. **Clone the repository:**

   ```bash
   git clone https://github.com/yourusername/perplexity-to-ghost.git
   cd perplexity-to-ghost
