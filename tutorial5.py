from elasticsearch import Elasticsearch


ELASTIC_PASSWORD ="OPkK*NVkUrbBRdxfQMD7"

client = Elasticsearch(
    "https://localhost:9200",
    basic_auth=("elastic", ELASTIC_PASSWORD),
    ca_certs="D:\\Spring Boot Elasticsearch 8 Course\\elasticsearch-8.7.0-windows-x86_64\\elasticsearch-8.7.0\\config\\certs\\http_ca.crt"
)

if client.ping():
    print("Connected with Elasticsearch")
else:
    print("Connection Failed")


settings = {
    "analysis":{
        "analyzer":{
            "my_analyzer":{
                "type":"custom",
                "char_analyzer": ["html_strip"],
                "tokenizer": "standard",
                "filter": ["lowercase","english_stop"]
            }
        },
        "filter":{
            "english_stop":{
                "type":"stop",
                "stopwords":"_english_"
            }
        }
    }
}

# response =client.indices.create(index="products009",settings=settings)

resp = client.indices.get(index="products009")
print(resp)