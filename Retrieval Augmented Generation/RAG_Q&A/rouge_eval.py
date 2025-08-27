from google.colab import files
uploaded = files.upload()  

import zipfile
import os

with zipfile.ZipFile("RAG.Assignment.Taha.zip.zip", 'r') as zip_ref:
    zip_ref.extractall(".")  

from rouge_score import rouge_scorer
import os

generated_dir = "summaries"
reference_dir = "references"
output_file = "rouge_scores.txt"

scorer = rouge_scorer.RougeScorer(['rouge1', 'rouge2', 'rougeL'], use_stemmer=True)

with open(output_file, "w") as out_f:
    for filename in os.listdir(generated_dir):
        if filename.endswith(".txt"):
            gen_path = os.path.join(generated_dir, filename)
            ref_path = os.path.join(reference_dir, filename)

            if os.path.exists(ref_path):
                with open(gen_path) as f_gen, open(ref_path) as f_ref:
                    generated = f_gen.read().strip()
                    reference = f_ref.read().strip()
                    scores = scorer.score(reference, generated)

                    out_f.write(f"== {filename} ==\n")
                    out_f.write(f"ROUGE-1: {scores['rouge1']}\n")
                    out_f.write(f"ROUGE-2: {scores['rouge2']}\n")
                    out_f.write(f"ROUGE-L: {scores['rougeL']}\n\n")

print("✅ ROUGE scores saved to rouge_scores.txt")

files.download('rouge_scores.txt')
