import os
import openai
import argparse

def main():
    print('Running copy Kitt!')

    parser = argparse.ArgumentParser()
    parser.add_argument("--input", "-i", type=str, required=True)
    args = parser.parse_args()
    user_input = args.input
    print(f"User input: {user_input}")
    pass


if __name__ == "__main__":
    main()
# Load your API key from an environment variable or secret management service
#openai.api_key = os.getenv("OPENAI_API_KEY")
#subject = "Mobility application"
#prompt = f"Generate upbeat branding snippet for {subject}"
#response = openai.Completion.create(model="text-davinci-002", prompt=prompt, temperature=0, max_tokens=32)
#print(response)