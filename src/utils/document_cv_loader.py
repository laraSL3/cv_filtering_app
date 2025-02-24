
from pathlib import Path
from markitdown import MarkItDown

class DocumentProcessing:
    def __init__(self, data_root_dir:Path):
        self.document_root_dir = data_root_dir
        self.current_document = None

        self.md = MarkItDown(enable_plugins=False)

    def load_and_convert_to_markdown(self, document_path:Path):
        document_content = self.md.convert(document_path)
        self.current_document = document_content
    
    def process_document_cv(self, document_path:Path):
        document_content = self.load_document_cv(document_path)
        return document_content


    

