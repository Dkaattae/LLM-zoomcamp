# intro

## LLM
i use google gemini model, which has a free tier.   
go to [google ai studio](https://aistudio.google.com/app/apikey) to get a free api key. 

copy the api key and put it into .env file   
`nano .env `   
inside .env file write   
`GEMINI_API_KEY="<your_api_key>" ` 
ctrl+O to save file, enter to confirm filename,   
crtl+X to exit.   
`echo ".env" >> .gitignore`

then in python code, copy from [google doc](https://ai.google.dev/gemini-api/docs)

note: i disabled my api key. i need generate a new api key and edit .env file everytime i work on this project.

## homework
### 1, spin up elastic search
```
docker run -it \
    --rm \
    --name elasticsearch \
    -m 4GB \
    -p 9200:9200 \
    -p 9300:9300 \
    -e "discovery.type=single-node" \
    -e "xpack.security.enabled=false" \
    docker.elastic.co/elasticsearch/elasticsearch:8.17.6
```

### 2, indexing data
`pip install elasticsearch=8.17.0`   
note: if version is not specified, pip will install elasticsearch 9.0.x, which is not compatible with docker image 8.17.6   
```
for doc in tqdm(documents):
    es_client.index(index=index_name, document=doc)
```
this is the line to indexing data in elastic search.

### 3, searching
making sure the booster set to 4 and get rid of filter. 

### 4, filtering   
running elastic search again but adding filter. the filter could be passed in parameters.   

### 5, building prompt
based on the results from q4, iterate over results add to context, and then add context to prompt

### 6, tokens  
`tokens = encoding.encode(prompt)`   
tiktoken will give us the token of given prompt.   
but actually, llm will use a bit more. becuase there are extra strings for system use.   

### bonus, llm
feed prompt into genai, it will give us the answer. 
