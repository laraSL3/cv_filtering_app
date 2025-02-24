from pathlib import Path

from langchain_core.prompts import PromptTemplate

from src.utils import prompt_templates
from src.utils import document_loader
from src.utils import llm_model_loader
from src.utils.schemas import ResponseOutput


def solution_filtering_cvs(llm,doc_loader):

    final_prompt = PromptTemplate.from_template(
            template=prompt_templates.cv_filtering_system_prompt,
            input=['job_description', 'cv']
        )

    structured_llm = llm.with_structured_output(
        ResponseOutput,method="json_schema"
    )
    llm_chain = final_prompt | structured_llm

    jd = doc_loader.load_jd()
    it = 0
    for cv in doc_loader.load_and_convert_to_markdown_all():
        response = llm_chain.invoke({
            "job_description":jd, 
            "cv":cv
        })
        print(response)


if __name__ == '__main__':

    input_root_dir = Path("src/data/input_data/")
    # llm_type = "google-gemini"
    llm_type = "azure-openai"

    gemini_model = llm_model_loader.LLMModelLoader(llm_type=llm_type).llm
    docs_loader = document_loader.DocumentProcessing(data_root_dir=input_root_dir)

    solution_filtering_cvs(
        llm=gemini_model,
        doc_loader=docs_loader
    )