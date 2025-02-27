from pathlib import Path

from langchain_core.prompts import PromptTemplate

import pandas as pd

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

    all_responses = []
    for cv in doc_loader.load_and_convert_to_markdown_all():
        response = llm_chain.invoke({
            "job_description":jd, 
            "cv":cv['content']
        })
        response_dict = response.model_dump()
        response_dict['source'] = cv['source']
        all_responses.append(response_dict)
    
    df = pd.DataFrame(all_responses)
    sorted_df = df.sort_values(by='Score', ascending=False)

    sorted_df.to_csv("src/data/output_data/filtered_cvs.csv",index=False)


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