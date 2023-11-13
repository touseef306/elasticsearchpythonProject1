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


# response = client.search(index="products", query={
#     "range":
#         {
#             "price":{
#                 "gte":100,
#                 "lte":200
#             }
#         }
# })
#
#
#
# response1 = client.search(index="products", query={
#    "match":{
#        "name": "product"
#    }
# })


response2 = client.search(index="products", query={
    "bool":{
        "filter":[
            {
                "range":
                        {
                            "price":{
                                "gte":100,
                                "lte":200
                            }
                        }
            }
        ],
        "must":[
            {
                "match":{
                       "name": "product"
                   }
            }
        ]
    }
},from_=0,size=2,sort={
    "price":{
        "order":"desc"
    }
})

for hit in response2["hits"]["hits"]:
    print(hit['_source']['name'], hit['_source']['price'])

