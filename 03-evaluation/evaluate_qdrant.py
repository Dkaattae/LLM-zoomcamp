import requests
import pandas as pd
from tqdm.auto import tqdm

from qdrant_client import QdrantClient, models

def hit_rate(relevance_total):
    cnt = 0

    for line in relevance_total:
        if True in line:
            cnt = cnt + 1

    return cnt / len(relevance_total)

def mrr(relevance_total):
    total_score = 0.0

    for line in relevance_total:
        for rank in range(len(line)):
            if line[rank] == True:
                total_score = total_score + 1 / (rank + 1)

    return total_score / len(relevance_total)

def evaluate(ground_truth, search_function):
    relevance_total = []

    for q in tqdm(ground_truth):
        doc_id = q['document']
        results = search_function(q)
        relevance = [d.payload['id'] == doc_id for d in results.points]
        relevance_total.append(relevance)

    return {
        'hit_rate': hit_rate(relevance_total),
        'mrr': mrr(relevance_total),
    }

def search(query, limit=5):

    results = qd_client.query_points(
        collection_name=collection_name,
        query=models.Document( #embed the query text locally with "jinaai/jina-embeddings-v2-small-en"
            text=query,
            model=model_handle 
        ),
        limit=limit, # top closest matches
        with_payload=True #to get metadata in the results
    )

    return results


url_prefix = 'https://raw.githubusercontent.com/DataTalksClub/llm-zoomcamp/main/03-evaluation/'
docs_url = url_prefix + 'search_evaluation/documents-with-ids.json'
documents = requests.get(docs_url).json()

ground_truth_url = url_prefix + 'search_evaluation/ground-truth-data.csv'
df_ground_truth = pd.read_csv(ground_truth_url)
ground_truth = df_ground_truth.to_dict(orient='records')

points = []

qd_client = QdrantClient("http://localhost:6333")
EMBEDDING_DIMENSIONALITY = 512
model_handle = "jinaai/jina-embeddings-v2-small-en"
collection_name = "zoomcamp-rag"

# Create the collection with specified vector parameters
qd_client.delete_collection(collection_name=collection_name)
qd_client.create_collection(
    collection_name=collection_name,
    vectors_config=models.VectorParams(
        size=EMBEDDING_DIMENSIONALITY,  # Dimensionality of the vectors
        distance=models.Distance.COSINE  # Distance metric for similarity search
    )
)

for i, doc in enumerate(documents):
    text = doc['question'] + ' ' + doc['text']
    point = models.PointStruct(
        id=i,
        vector=models.Document(text=text, model=model_handle), #embed text locally with "jinaai/jina-embeddings-v2-small-en" from FastEmbed
        payload=doc
    )
    points.append(point)


qd_client.upsert(
    collection_name=collection_name,
    points=points
)

qdrant_results = evaluate(ground_truth, lambda q: search(q['question']))

print('hit rate: ', qdrant_results['hit_rate'])
print('mrr: ', qdrant_results['mrr'])