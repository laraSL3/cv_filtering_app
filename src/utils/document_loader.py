
from pathlib import Path
from markitdown import MarkItDown
from tqdm import tqdm

import concurrent.futures


class DocumentProcessing:
    def __init__(self, data_root_dir:Path):
        self.document_root_dir = data_root_dir
        self.md = MarkItDown()

    def load_and_convert_to_markdown(self, document_path:Path):
        document_content = self.md.convert(document_path)
        return {"source": document_path, "content": document_content.text_content}
    
    def count_number_of_documents(self):
        return len(list(self.document_root_dir.glob("CVs_QA/*.pdf")))
    
    def load_and_convert_to_markdown_all(self):
        total_docs = self.count_number_of_documents()
        document_paths = list(self.document_root_dir.glob("CVs_QA/*.pdf"))
        # for document_path in tqdm(self.document_root_dir.glob("CVs_QA/*.pdf"),total=total_docs):
        #     # print(document_path)
        #     document_content = self.load_and_convert_to_markdown(document_path)
        #     yield {"source": document_path, "content": document_content.text_content}

        with concurrent.futures.ThreadPoolExecutor(max_workers=8) as executor:
            futures = {
                executor.submit(self.load_and_convert_to_markdown, document_path): document_path
                for document_path in document_paths
            }
            
            for future in tqdm(concurrent.futures.as_completed(futures), total=total_docs):
                yield future.result()
    
    def load_jd(self) -> str:
        jd_path = self.document_root_dir / "job_descriptions/jd.txt"
        jd_content = self.md.convert(jd_path)
        return jd_content.text_content

    

