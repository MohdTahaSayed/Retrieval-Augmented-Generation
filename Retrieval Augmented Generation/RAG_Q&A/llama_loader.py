
from langchain.llms import LlamaCpp

def load_llama_model(model_path="/content/tinyllama.gguf"):
    llm = LlamaCpp(
        model_path=model_path,
        temperature=0.7,
        max_tokens=256,
        n_ctx=512,
        top_p=1,
        verbose=True
    )
    print("✅ TinyLLaMA loaded with safe limits.")
    return llm
