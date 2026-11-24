# Week 4 – Tokenizer Comparison

## Description
This project compares three different tokenization methods: BPE, WordPiece, and SentencePiece. It uses English, Telugu, and Hindi sentences to observe how different tokenizers split text into tokens and generate token IDs.

## Technologies Used
- Python
- Hugging Face Transformers
- GPT-2 Tokenizer
- Multilingual BERT Tokenizer
- XLM-R Tokenizer

## Features
- Compares three tokenization methods.
- Supports English, Telugu, and Hindi languages.
- Displays tokens and their token IDs.
- Shows the total token count for each tokenizer.
- Uses pretrained tokenizers from Hugging Face.

## Setup and Execution

1. Install the required library:
   ```bash
   pip install transformers
   ```

2. Run the Python file:
   ```bash
   python main.py
   ```

3. View the tokenization results for all three languages.

## Tokenizers Used

- **BPE:** GPT-2
- **WordPiece:** Multilingual BERT
- **SentencePiece:** XLM-R

## Learning Outcome
Learned how different tokenization techniques work and how they process multilingual text by comparing tokens, token IDs, and token counts.
