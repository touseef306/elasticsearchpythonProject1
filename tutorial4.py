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

mapping ={
    "properties":{
        "title":{
            "type":"text"
        },
        "content":{
            "type":"text"
        },
        "date":{
            "type":"date",
            "format":"yyyy-MM-dd"
        }
    }
}

response = client.indices.create(index="index0001", mappings=mapping)
resp = client.indices.get(index="index0001")
print(resp)