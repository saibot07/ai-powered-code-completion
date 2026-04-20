# AI-Powered Code Completion

## Description
Smart code completion by S.A.I.: an AI-driven, lightning-fast, and GPT-powered Python tool. It utilizes OpenAI's API to provide intelligent autocompletion for developers, enabling faster and error-free workflows.

## Features
- AI-driven code completion using OpenAI's GPT API
- Easy-to-use CLI for generating code
- Python-first design
- Containerized with Docker for easy deployment

## Prerequisites
- Python 3.9 or above
- OpenAI API key (sign up at [OpenAI](https://platform.openai.com/signup/))

## Installation
1. Clone the repo:
   ```bash
   git clone https://github.com/saibot07/ai-powered-code-completion.git
   cd ai-powered-code-completion
   ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Set up your API key as an environment variable:
   ```bash
   export OPENAI_API_KEY=your_api_key_here
   ```

4. Run the app:
   ```bash
   python main.py
   ```

## Usage
- Input a programming prompt or question when prompted.
- Example prompt: `Write a Python function to check if a number is prime.`

### Advanced Usage with Docker
1. Build the Docker image:
   ```bash
   docker build -t code-completion-ai .
   ```
2. Run the Docker container:
   ```bash
   docker run -e OPENAI_API_KEY=your_api_key_here code-completion-ai
   ```

## Roadmap
Future improvements:
- Support for multiple programming languages
- Web-based GUI
- Additional configurations for engine selection

## License
MIT
