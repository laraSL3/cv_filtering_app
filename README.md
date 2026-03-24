# CV Filtering App

An AI-powered CV screening tool that evaluates resumes against a job description using large language models (LLMs). Each CV is scored on a scale of 1–100, with reasoning provided, and results are exported as a sorted CSV file.

---

## Features

- Converts PDF CVs to Markdown and evaluates them against a job description
- Supports **Google Gemini** and **Azure OpenAI** as LLM backends
- Parallel processing of CVs via `ThreadPoolExecutor`
- Structured output (Name, Score, Reason) saved to CSV, sorted by score descending
- Configurable via `.env` file using `pydantic-settings`

---

## Project Structure

```
cv_filtering_app/
├── pyproject.toml
├── README.md
├── src/
│   ├── configs.py                        # Pydantic settings for LLM providers
│   ├── services/
│   │   └── solution_filtering_cvs.py    # Main entry point / orchestration logic
│   ├── utils/
│   │   ├── document_loader.py           # PDF → Markdown conversion & JD loading
│   │   ├── llm_model_loader.py          # LLM factory (Gemini / Azure OpenAI)
│   │   ├── prompt_templates.py          # System prompt template
│   │   └── schemas.py                   # Pydantic output schema (Name, Score, Reason)
│   ├── tests/
│   │   └── langchain_testing_for_gemini.py
│   └── data/
│       ├── input_data/
│       │   ├── CVs_QA/                  # Place PDF CVs here
│       │   └── job_descriptions/
│       │       └── jd.txt               # Job description text file
│       └── output_data/
│           └── filtered_cvs.csv         # Generated output (auto-created)
```

---

## Supported LLM Providers

| Provider | `llm_type` value | Notes |
|---|---|---|
| Google Gemini | `"google-gemini"` | Uses `langchain-google-genai` |
| Azure OpenAI | `"azure-openai"` | Uses `langchain-openai` with Azure endpoints |

---

## Prerequisites

- Python **3.11** or higher
- [uv](https://docs.astral.sh/uv/) (recommended) or `pip`

---

## Installation

### Using `uv` (recommended)

```bash
uv sync
```

### Using `pip`

```bash
pip install -e .
```

---

## Environment Setup

Create a `.env` file in the **project root** (same level as `pyproject.toml`):

```bash
touch .env
```

### `.env` Variables

#### Google Gemini

```env
# Google Gemini
GOOGLE_API_KEY=your_google_api_key_here
GOOGLE_MODEL_NAME=gemini-2.0-flash        # e.g. gemini-1.5-pro, gemini-2.0-flash
GEMINI_TEMPERATURE=0.0
```

| Variable | Required | Description |
|---|---|---|
| `GOOGLE_API_KEY` | Yes | API key from [Google AI Studio](https://aistudio.google.com/app/apikey) |
| `GOOGLE_MODEL_NAME` | Yes | Model identifier (e.g. `gemini-1.5-pro`, `gemini-2.0-flash`) |
| `GEMINI_TEMPERATURE` | No | Sampling temperature (default: `0.0`) |

#### Azure OpenAI

```env
# Azure OpenAI
AZURE_OPENAI_API_KEY=your_azure_openai_api_key_here
AZURE_OPENAI_ENDPOINT=https://your-resource-name.openai.azure.com/
AZURE_OPENAI_MODEL=your_deployment_name
AZURE_DEPLOYMENT_NAME=your_deployment_name
AZURE_OPENAI_API_VERSION=2024-08-01-preview
AZURE_OPENAI_API_VERSION_OLD=2023-05-15
AZURE_OPENAI_TEMPERATURE=0.0
```

| Variable | Required | Description |
|---|---|---|
| `AZURE_OPENAI_API_KEY` | Yes | Azure OpenAI resource API key |
| `AZURE_OPENAI_ENDPOINT` | Yes | Azure OpenAI resource endpoint URL |
| `AZURE_OPENAI_MODEL` | Yes | Azure deployment name (e.g. `gpt-4o`) |
| `AZURE_DEPLOYMENT_NAME` | Yes | Azure deployment name (same as above) |
| `AZURE_OPENAI_API_VERSION` | Yes | API version (e.g. `2024-08-01-preview`) |
| `AZURE_OPENAI_API_VERSION_OLD` | Yes | Legacy API version (e.g. `2023-05-15`) |
| `AZURE_OPENAI_TEMPERATURE` | No | Sampling temperature (default: `0.0`) |

> **Note:** If you are only using one provider, you only need to fill in the variables for that provider. Unused provider variables will be ignored by the application.

---

## Preparing Input Data

1. **CVs**: Place all PDF resumes inside `src/data/input_data/CVs_QA/`
2. **Job Description**: Write or paste the job description into `src/data/input_data/job_descriptions/jd.txt`

---

## Running the App

Select the LLM provider by editing the `llm_type` variable in `src/services/solution_filtering_cvs.py`:

```python
# src/services/solution_filtering_cvs.py

llm_type = "google-gemini"   # Use Google Gemini
# llm_type = "azure-openai"  # Use Azure OpenAI
```

Then run the service from the **project root**:

```bash
python -m src.services.solution_filtering_cvs
```

---

## Output

Results are saved to `src/data/output_data/filtered_cvs.csv`, sorted by score descending.

| Column | Description |
|---|---|
| `Name` | Candidate's full name extracted from the CV |
| `Score` | Evaluation score (1–100) relative to the job description |
| `Reason` | Detailed reasoning, highlighting matches and gaps |
| `source` | Path to the source PDF file |

---

## Scoring Criteria

The LLM evaluates each CV on a **1–100 scale**, with emphasis on:

- Hands-on experience in **AI/ML**
- Relevance of skills to the job description
- Practical project work and tooling experience

---

## Dependencies

| Package | Purpose |
|---|---|
| `langchain-google-genai` | Google Gemini LLM integration |
| `langchain-openai` | Azure OpenAI LLM integration |
| `markitdown` | PDF to Markdown conversion |
| `pydantic` | Data validation and structured output |
| `pydantic-settings` | `.env` file configuration management |
| `pandas` | CSV output generation |
| `tqdm` | Progress bar during CV processing |
