from elasticsearch import Elasticsearch


ELASTIC_PASSWORD ="o*kALlyz2NvyYKYu_G3r"

client = Elasticsearch(
    "https://localhost:9200",
    basic_auth=("elastic", ELASTIC_PASSWORD),
    ca_certs="D:\\certs\\python\\http_ca.crt"
)

if client.ping():
    print("Connected with Elasticsearch")
else:
    print("Connection Failed")