# Claude API Interaction Script

This Python script interacts with **Anthropic's Claude** via **AWS Bedrock**. It allows users to input prompts and receive AI-generated responses.

## Features
- Uses AWS Bedrock to interact with **Claude 3 Haiku**.
- Handles user input in an interactive loop.
- Provides error handling for API failures.
- Allows users to exit by typing `quit` or `exit`.

## Prerequisites
- **Python 3.x**
- **AWS Credentials** (configured via `aws configure` or environment variables)
- **Boto3** (AWS SDK for Python)

## Installation
1. Clone or download this repository.

```sh
git clone https://github.com/your-repo/shopsight-python-examples.git
cd shopsight-python-examples
```

1. Configure AWS credentials:

```sh
aws configure
```

1. Setup & Activate Virtual Environment (Optional):

```sh
python -m venv venv
source venv/bin/activate
```

1. Install dependencies:

```sh
pip install -r requirements.txt
```

## Usage

Run the script using Python:

```sh
python example.py
```

Follow the prompts to interact with Claude 3 Haiku. Type `quit` or `exit` to exit the script.

## Configuration

Modify these variables at the top of the script to adjust behavior:

- AWS_REGION: AWS region for Bedrock (default: us-east-1)
- ANTHROPIC_VERSION: API version (bedrock-2023-05-31)
- ANTHROPIC_MODEL: Model ID (anthropic.claude-3-haiku-20240307-v1:0)
- MAX_TOKENS: Maximum token limit for responses (default: 1000)