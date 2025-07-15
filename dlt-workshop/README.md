
# load docs to qdrant using dlt


`docker pull qdrant/qdrant`   

```
docker run -p 6333:6333 -p 6334:6334 \
   -v "$(pwd)/db.qdrant:/qdrant/storage:z" \
   qdrant/qdrant
```
in pipeline.py export environment variables   
DLT_EMBEDDINGS__PROVIDER=sentence_transformers   
DLT_EMBEDDINGS__MODEL_NAME=all-MiniLM-L6-v2   
for less CPU consumption   
run 
`python pipeline.py`   

Access web UI at http://localhost:6333/dashboard

go to collections/zoomcamp_tagged_data_dtc_faq_docs
visualize
```
{
  "limit": 948,
  "using": "fast-bge-small-en",
  "color_by": {
    "payload": "section"
  },
  "filter": {
    "must": [
      {"key": "course", "match": {"value": "data-engineering-zoomcamp"} }
    ]
  }
}
```