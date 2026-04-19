import openai
import os
import sys

def get_code_completion(prompt):
    # Ensure the API key is set
    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key:
        raise EnvironmentError("Please set the OPENAI_API_KEY environment variable.")

    # Initialize OpenAI API
    openai.api_key = api_key

    try:
        # Generate completion
        response = openai.Completion.create(
            engine="text-davinci-003", # Adjust engine as needed
            prompt=prompt,
            max_tokens=150,
            temperature=0.5
        )
        return response.choices[0].text.strip()
    except Exception as e:
        return f"Error: {str(e)}"

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python main.py <code_prompt>")
        sys.exit(1)

    code_prompt = sys.argv[1]
    completion = get_code_completion(code_prompt)
    print("Generated Code:\n")
    print(completion)