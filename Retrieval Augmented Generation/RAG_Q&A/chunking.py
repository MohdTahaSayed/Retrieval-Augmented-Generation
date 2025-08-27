
import zipfile, os
from langchain_community.document_loaders import TextLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter

def extract_and_load_md_files(zip_filename, extract_dir="/content/md_docs"):
    os.makedirs(extract_dir, exist_ok=True)
    with zipfile.ZipFile(zip_filename, 'r') as zip_ref:
        zip_ref.extractall(extract_dir)

    md_files = [os.path.join(root, f)
                for root, _, files in os.walk(extract_dir)
                for f in files if f.endswith('.md')]
    print(f"✅ Extracted and found {len(md_files)} markdown files.")

    documents = []
    for file_path in md_files:
        try:
            loader = TextLoader(file_path)
            documents.extend(loader.load())
        except Exception as e:
            print(f"Error loading {file_path}: {e}")

    return documents

def split_documents(documents, chunk_size=256, chunk_overlap=20):
    splitter = RecursiveCharacterTextSplitter(chunk_size=chunk_size, chunk_overlap=chunk_overlap)
    docs = splitter.split_documents(documents)
    print(f"✅ Split into {len(docs)} chunks.")
    return docs
