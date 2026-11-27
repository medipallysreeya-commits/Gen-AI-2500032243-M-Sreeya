# Week 6 – Generative AI Programming: Baseline Evaluation

## Overview
This project evaluates the performance of a locally running **Llama 3.2 model** using Ollama. It uses a Golden Question Set of 30 questions covering fundamental Generative AI concepts.

## Features
- Evaluates 30 predefined questions.
- Uses Ollama API to generate responses.
- Calculates keyword coverage scores.
- Classifies results as PASS, REVIEW, or ERROR.
- Exports evaluation results to a CSV file.

## Technologies Used
- Python
- Ollama
- Llama 3.2
- Requests
- CSV

## Project Structure
- `golden_set.json` – Contains 30 questions and reference answers.
- `main.py` – Runs the evaluation and calculates scores.
- `requirements.txt` – Contains required dependencies.
- `baseline_results.csv` – Stores evaluation results.

## Setup and Execution

**2. Pull the Llama 3.2 model**
```bash
ollama pull llama3.2
```

**3. Run the evaluation**
```bash
python main.py
```

## Evaluation Criteria
- **PASS:** Keyword coverage ≥ 60%
- **REVIEW:** Keyword coverage < 60%
- **ERROR:** Request or execution failure.

## Output
The evaluation generates `baseline_results.csv`, containing model responses, keyword scores, evaluation status, sources, and release information.

**Release:** v0.1
