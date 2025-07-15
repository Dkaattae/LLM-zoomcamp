
import dlt
import os
import requests
from dlt.destinations import qdrant
from qdrant_client import QdrantClient
from dlt.destinations.adapters import qdrant_adapter


@dlt.resource(table_name="dtc_faq_docs", max_table_nesting=0)
def zoomcamp_data():
    docs_url = 'https://github.com/alexeygrigorev/llm-rag-workshop/raw/main/notebooks/documents.json'
    docs_response = requests.get(docs_url)
    documents_raw = docs_response.json()

    for course in documents_raw:
        course_name = course['course']

        for doc in course['documents']:
            doc['course'] = course_name
            yield doc

if __name__ == "__main__":
    qclient = QdrantClient(path="db.qdrant")

    client = qdrant(
        host="localhost",  
        port=6333,
        grpc_port=6334,
        path="db.qdrant"
    )

    os.environ["DLT_EMBEDDINGS__PROVIDER"] = "sentence_transformers"
    os.environ["DLT_EMBEDDINGS__MODEL_NAME"] = "all-MiniLM-L6-v2"

    pipeline = dlt.pipeline(
        pipeline_name="zoomcamp_pipeline",
        destination=client,
        dataset_name="zoomcamp_tagged_data"

    )
    
    faq_docs = zoomcamp_data()
    qdrant_adapter(faq_docs, embed=["text"])
    load_info = pipeline.run(faq_docs)
    print(pipeline.last_trace)
