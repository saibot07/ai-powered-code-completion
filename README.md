# AI-Powered Code Completion

This repository provides a simple Python tool for code autocompletion using OpenAI's GPT API. With the rise of advanced AI models like GPT-4, integrating intelligent coding assistance is a hot trend. This tool generates relevant code snippets based on your function headers or initial code.

## Features
- Generates code completions for Python scripts.
- Simple and lightweight.
- Leverages OpenAI's API for completions.

## Installation
1. Clone the repository.
   ```bash
   git clone https://github.com/your_username/ai-powered-code-completion.git
   cd ai-powered-code-completion
   ```
2. Install the required dependencies.
   ```bash
   pip install openai
   ```

## Usage
1. Add your OpenAI API key to the `OPENAI_API_KEY` environment variable.
2. Run the `main.py` script with a partial code snippet as input:
   ```bash
   python main.py "def greeting(name):"
   ```
3. The tool will output a suggested code snippet.

## Example Output
Input:
```python
def greeting(name):
```
Output:
```python
def greeting(name):
    return f"Hello, {name}!"
```

## Notes
- Ensure you have an active OpenAI API key to use the tool.
- This is a simple example for learning purposes, and further enhancements are encouraged!

## License
MIT License.
