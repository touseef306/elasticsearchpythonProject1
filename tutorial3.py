from elasticsearch import Elasticsearch
from elasticsearch.helpers import bulk


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


response = client.search(index="products",aggs={
    "avg_price":{
        'avg':{
            'field':'price'
        }
    },
    "min_price":{
        "min":{
            "field": "price"
        }
    },
    "max_price":{
        "max":{
            "field":"price"
        }
    }
})

print(response)

