# evaluate

## text search
text search function:   
`index.search(query=q['question'], course=q['course'], boost=boost)`

## vector search
vector search function: 
`vindex.search(query_vector=pipeline.transform([q['question']]))`

## qdrant
```
docker run -p 6333:6333 -p 6334:6334 \
   -v "$(pwd)/qdrant_storage:/qdrant/storage:z" \
   qdrant/qdrant
```
start a qdrant client on localhost:6333   
create a collection (delete first if exists)   
convert docs to points   
upsert points   
search function   
evaluate   

hit rate:  0.9118219148476334
mrr:  0.8247352496217863