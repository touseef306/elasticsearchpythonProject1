from elasticsearch import Elasticsearch
from elasticsearch_dsl import Search, Q
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

# s= Search(using=client, index="products")
#
# response = s.execute()
#
# print(response.hits.total)
#
# for hit in response:
#     print(hit.name, hit.price)


# q_match = Q('match', name='product')
# q_range = Q('range', price={'gte':101,'lte':200})
#
# q = q_match & q_range
#
# s = Search(using=client, index="products").query(q)
#
# response = s.execute()
#
# print(response.hits.total)
#
# for hit in response:
#     print(hit.name, hit.price)


q_match = Q('match', name={'query':"product 1", 'operator':'and'})


s =Search(using=client, index="products").query(q_match)

response = s.execute()

print(response.hits.total)

for hit in response:
    print(hit.name, hit.price)






