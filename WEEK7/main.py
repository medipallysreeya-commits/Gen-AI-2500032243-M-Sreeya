
import torch
import pandas as pd
import os
from transformers import AutoTokenizer, AutoModelForCausalLM

# Model configuration
MODEL_NAME = "distilgpt2"
TOP_K = 5

# Load pretrained model
print("Loading DistilGPT-2 model...")

tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME)
model = AutoModelForCausalLM.from_pretrained(MODEL_NAME)

model.eval()

print("Model loaded successfully!")

# Get prompt from user
prompt = input("\nEnter your prompt: ")

# Convert prompt into tokens
inputs = tokenizer(prompt, return_tensors="pt")

# Get model predictions
with torch.no_grad():
    outputs = model(**inputs)

# Extract logits for the next token
logits = outputs.logits[0, -1, :]

# Convert logits into probabilities
probabilities = torch.softmax(logits, dim=-1)

# Find top 5 candidate tokens
top_probs, top_indices = torch.topk(probabilities, TOP_K)

# Display results
print("\n" + "=" * 60)
print("NEXT-TOKEN PROBABILITY ANALYSIS")
print("=" * 60)

print("\nInput Prompt:", prompt)
print("\nTop 5 Next-Token Predictions:\n")

results = []

for rank, (prob, token_id) in enumerate(
    zip(top_probs, top_indices), start=1
):
    token_id = token_id.item()
    token = tokenizer.decode([token_id])
    probability = prob.item()
    logit = logits[token_id].item()

    print(f"Rank        : {rank}")
    print(f"Token       : {repr(token)}")
    print(f"Token ID    : {token_id}")
    print(f"Logit       : {logit:.4f}")
    print(f"Probability : {probability:.6f}")
    print("-" * 60)

    results.append({
        "Rank": rank,
        "Token": token,
        "Token_ID": token_id,
        "Logit": logit,
        "Probability": probability
    })

# Save results as CSV
os.makedirs("outputs", exist_ok=True)

df = pd.DataFrame(results)
df.to_csv("outputs/top_k_predictions.csv", index=False)

print("\nResults saved successfully!")
print("Location: outputs/top_k_predictions.csv")
