# Week 5 – LLM Token Economics and Budget Estimation

## Description
This project estimates the token usage, API cost, and budget requirements for an LLM-based application. It calculates daily and monthly costs, checks RPM and TPM limits, and verifies whether the project stays within the configured budget.

## Technologies Used
- Python
- python-dotenv
- Dataclasses
- Unittest

## Features
- Calculates daily input and output tokens.
- Estimates daily and monthly API costs.
- Checks Requests Per Minute (RPM) limits.
- Checks Tokens Per Minute (TPM) limits.
- Includes a configurable safety margin.
- Checks daily and monthly budget limits.
- Provides PASS or REVIEW results.
- Includes unit testing.

## Setup and Execution

1. Install the required library:
   ```bash
   pip install python-dotenv
   ```

2. Create a `.env` file and configure:
   - REQUESTS_PER_DAY
   - AVG_INPUT_TOKENS
   - AVG_OUTPUT_TOKENS
   - PEAK_REQUESTS_PER_MINUTE
   - INPUT_PRICE_PER_MILLION
   - OUTPUT_PRICE_PER_MILLION
   - RPM_LIMIT
   - TPM_LIMIT
   - MONTHLY_BUDGET_USD
   - DAILY_BUDGET_USD
   - SAFETY_MARGIN_PERCENT

3. Run the program:
   ```bash
   python main.py
   ```

## Testing
Run unit tests:
```bash
python -m unittest
```

## Learning Outcome
Learned how to estimate LLM token usage, calculate API costs, check rate limits, manage budgets, and perform unit testing.
