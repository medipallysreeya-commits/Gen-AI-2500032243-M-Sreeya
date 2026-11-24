# Week 3 – LLM Usage Monitoring and Logging

## Description
This project extends the multiple LLM provider system by adding usage monitoring and logging. It tracks token usage, response time, estimated API cost, and errors. The usage details are stored in MongoDB for monitoring.

## Technologies Used
- Python
- Google Gemini API
- Ollama (Llama 3.2)
- MongoDB
- PyMongo
- Requests
- python-dotenv
- Unittest

## Features
- Supports Gemini and Ollama providers.
- Tracks input and output tokens.
- Measures API response time (latency).
- Estimates Gemini API usage cost.
- Handles temporary errors using retry logic.
- Stores usage details in MongoDB.
- Includes unit testing.

## Setup and Execution

1. Install the required libraries:
   ```bash
   pip install google-genai requests pymongo python-dotenv
   ```

2. Create a `.env` file and add:
   ```env
   GEMINI_API_KEY=your_api_key
   MONGODB_URI=your_mongodb_connection_string
   ```

3. Configure Gemini input and output token prices if required.

4. Run the main Python file:
   ```bash
   python main.py
   ```

5. Choose the provider and enter your prompt.

## Testing
Run unit tests using:
```bash
python -m unittest
```

## Database
Usage records are stored in MongoDB:
- Database: `llm_monitoring`
- Collection: `api_usage`

## Learning Outcome
Learned how to monitor LLM usage, track tokens and latency, estimate API costs, handle errors, store usage records in MongoDB, and perform unit testing.
