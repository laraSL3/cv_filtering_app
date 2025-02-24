
from pathlib import Path
from markitdown import MarkItDown

class DocumentProcessing:
    def __init__(self, data_root_dir:Path):
        self.document_root_dir = data_root_dir
        self.md = MarkItDown()

    def load_and_convert_to_markdown(self, document_path:Path):
        document_content = self.md.convert(document_path)
        return document_content
    
    def load_and_convert_to_markdown_all(self):
        for document_path in self.document_root_dir.glob("CVs_QA/*.pdf"):
            # print(document_path)
            document_content = self.load_and_convert_to_markdown(document_path)
            yield document_content.text_content
    
    def load_jd(self) -> str:
        jd_path = self.document_root_dir / "job_descriptions/jd.txt"
        jd_content = self.md.convert(jd_path)
        return jd_content.text_content

    

