# Next-Token Probabilities using Hugging Face Transformers

## Overview

This project explores how a Generative AI language model predicts the next token in a given text sequence. It uses the pretrained **DistilGPT-2 model** through the Hugging Face Transformers library to demonstrate the next-token prediction mechanism used in Large Language Models (LLMs).

The program accepts a text prompt, extracts the model's logits, converts them into probabilities using the Softmax function, and displays the Top 5 most probable next-token candidates.

## Technologies Used
- Python
- Hugging Face Transformers
- PyTorch
- Pandas

## Working Process
1. Accept a text prompt from the user.
2. Tokenize the input.
3. Generate logits using DistilGPT-2.
4. Apply Softmax to calculate probabilities.
5. Display the Top 5 predicted tokens.
6. Save the results in a CSV file.

## Output

Displays the predicted tokens along with their token IDs, logits, and probability scores. Results are automatically saved in `outputs/top_k_predictions.csv`.

## Conclusion

This experiment provides practical insight into how language models predict the next token using logits and probability distributions, demonstrating a fundamental mechanism behind GPT-based models.
