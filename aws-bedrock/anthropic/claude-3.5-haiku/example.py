import boto3
import json

AWS_REGION="us-east-1"
ANTHROPIC_VERSION="bedrock-2023-05-31"
ANTHROPIC_MODEL="anthropic.claude-3-haiku-20240307-v1:0"
MAX_TOKENS=1000

def get_claude_response(prompt):

    # Initialize the Bedrock client
    bedrock = boto3.client(
        service_name='bedrock-runtime',
        region_name=AWS_REGION
    )

    # Prepare the request body
    body = {
        "anthropic_version": ANTHROPIC_VERSION,
        "max_tokens": MAX_TOKENS,
        "messages": [
            {
                "role": "user",
                "content": prompt
            }
        ]
    }

    try:
        # Make the API call
        response = bedrock.invoke_model(
            modelId=ANTHROPIC_MODEL,
            body=json.dumps(body)
        )

        # Parse and return the response
        response_body = json.loads(response['body'].read())
        return response_body['content'][0]['text']

    except Exception as e:
        print(f"Error: {str(e)}")
        return None

def main():
    print("Enter 'quit' or 'exit' to end the program.")
    
    while True:
        # Get user input
        user_prompt = input("\nEnter your prompt for Claude: ").strip()
        
        # Check if user wants to exit
        if user_prompt.lower() in ['quit', 'exit']:
            break
            
        # Skip empty prompts
        if not user_prompt:
            print("Please enter a valid prompt.")
            continue
            
        # Get and display response
        print("\nGetting response from Claude...\n\n")
        response = get_claude_response(user_prompt)
        
        if response:
            print(response)
        else:
            print("\nFailed to get a response from Claude.")

if __name__ == "__main__":
    main()
