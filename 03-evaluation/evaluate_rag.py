import requests
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from tqdm.auto import tqdm

from minsearch import VectorSearch
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.decomposition import TruncatedSVD
from sklearn.pipeline import make_pipeline

from rouge import Rouge

def cosine(u, v):
    u = u.flatten()
    v = v.flatten()
    u_norm = np.sqrt(u.dot(u))
    v_norm = np.sqrt(v.dot(v))
    return u.dot(v) / (u_norm * v_norm)

def compute_similarity(record):
    v_orig = pipeline.transform([record['answer_orig']])
    v_llm = pipeline.transform([record['answer_llm']])
    return cosine(v_orig, v_llm)

url_prefix = 'https://raw.githubusercontent.com/DataTalksClub/llm-zoomcamp/main/03-evaluation/'
results_url = url_prefix + 'rag_evaluation/data/results-gpt4o-mini.csv'
df_results = pd.read_csv(results_url)
results_dict = df_results.to_dict(orient='records')

pipeline = make_pipeline(
    TfidfVectorizer(min_df=3),
    TruncatedSVD(n_components=128, random_state=1)
)

pipeline.fit(df_results.answer_llm + ' ' + df_results.answer_orig + ' ' + df_results.question)

similarity = []

for record in tqdm(results_dict):
    sim = compute_similarity(record)
    similarity.append(sim)

df_results['cosine'] = similarity
# print(df_results['cosine'].describe())


# print histgram of cosine similarity
# df_results['cosine'].hist(bins=100)
# plt.title('Distribution of cosine similarity of gpt4o-mini')
# plt.xlabel('Cosine')
# plt.ylabel('Frequency')
# plt.savefig("Cosine_Similarity.png")

rouge_scorer = Rouge()
rouge1_f = []

for record in tqdm(results_dict):   
    scores = rouge_scorer.get_scores(record['answer_llm'], record['answer_orig'])[0]
    rouge1_f.append(scores['rouge-1']['f'])

df_results['rouge1_f'] = rouge1_f

print(df_results['rouge1_f'].describe())