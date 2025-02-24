from pathlib import Path

from src.utils import prompt_templates
from src.utils import document_cv_loader
from src.utils import llm_model_loader


def solution_filtering_cvs():
    pass


if __name__ == '__main__':

    input_root_dir = Path("src/data/input_data/CVs_QA")

    gemini_model = llm_model_loader.LLMModelLoader(llm_type="google-gemini").llm
    cv_loader = document_cv_loader.DocumentProcessing(data_root_dir=input_root_dir)

    solution_filtering_cvs()