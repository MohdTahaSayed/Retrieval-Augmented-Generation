# Retrieval Augmented Generation (RAG)

This repository demonstrates **Retrieval-Augmented Generation** using TinyLLaMA. It contains two main variations:

## 1. RAG_Summarizer
- Summarizes markdown documents using TinyLLaMA.
- Splits documents into chunks for better processing.
- Evaluation done with ROUGE metrics.
- Designed to run in Jupyter Notebook or Google Colab.

## 2. RAG_Q&A
- Provides a **question-answering pipeline** over documents.
- Uses embeddings and a vectorstore for retrieval.
- LLaMA generates answers with source references.
- Modular Python scripts handle chunking, embeddings, LLaMA loading, RAG pipeline, and optional ROUGE evaluation.

## Requirements
- Python 3.10+
- Dependencies listed in `requirements.txt`
- Compatible with Google Colab and Jupyter Notebook

## How to Run
1. Clone the repository:
   ```bash
   git clone https://github.com/MohdTahaSayed/Retrieval-Augmented-Generation.git
