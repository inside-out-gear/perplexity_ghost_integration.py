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
   ```

2. **Install the required libraries:**

   ```bash
   pip install requests python-dotenv
   ```

3. **Create a `.env` file:**

   In the root directory of the project, create a file named `.env` and add your API keys and URLs:

   ```plaintext
   PERPLEXITY_API_KEY=YOUR_PERPLEXITY_API_KEY
   GHOST_API_KEY=YOUR_GHOST_API_KEY
   GHOST_API_POST_URL=YOUR_GHOST_API_POST_URL
   ```

   Replace the placeholders with your actual API keys and URLs.

4. **Run the script:**

   You can now run the script by executing the following command:

   ```bash
   python your_script_name.py
   ```

   Replace `your_script_name.py` with the name of your Python script file.

## Usage

Modify the `prompt` variable in the script to change the text prompt sent to the Perplexity AI API. For example:

```python
prompt = "What are the latest advancements in AI?"
```

## Contributing

Contributions are welcome! If you have suggestions for improvements or new features, feel free to open an issue or submit a pull request.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Acknowledgments

- [Perplexity AI](https://www.perplexity.ai/) for their AI API.
- [Ghost](https://ghost.org/) for their blogging platform and API.

```

### Explanation of the Sections:

- **Title**: Clearly states the purpose of the project.
- **Features**: Lists the main functionalities of the script.
- **Requirements**: Specifies what is needed to run the script.
- **Installation**: Provides step-by-step instructions to set up the project.
- **Usage**: Explains how to modify the script for different prompts.
- **Contributing**: Encourages others to contribute to the project.
- **License**: States the licensing information.
- **Acknowledgments**: Gives credit to the services used in the project.

Feel free to customize any sections to better fit your project or personal style!
