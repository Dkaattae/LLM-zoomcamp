# evaluate search

## text search
text search function:   
`index.search(query=q['question'], course=q['course'], boost=boost)`

## vector search
vector search function: 
`vindex.search(pipeline.transform([q['question']]), q['course'], num_results=5)`
embed question only   
hit rate:  0.48173762697212014
mrr:  0.3572833369353793
embed question plus answer   
hit rate:  0.8210503566025502
mrr:  0.6717347453353508

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

# evaluate rag
## cosine similarity
A_orig -> Q -> A_llm   
cosine(A_orig_emb, A_llm_emb)
count    1830.000000
mean        0.841584
std         0.173737
min         0.079093
25%         0.806927
50%         0.905812
75%         0.950711
max         0.996457

## rouge
Rouge-1 F1 average
0.351695