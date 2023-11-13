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


def create_document(index,id,document):
    resp = client.index(index=index,id=id,document=document)
    return resp

document = {
    'title':'Introduction to Elasticsearch',
    'description': 'learn the basics of elasticsearch and python'
}

# response = create_document(index="index001",id=2,document=document)

# print(response)

def update_document(index,id,updated_doc):
    resp = client.update(index=index,id=id, doc=updated_doc)
    return resp

update_doc ={
    'doc':{
    'description': 'Master Elasticsearch and python integration'
}
}

# response = update_document(index="index001",id=2, updated_doc=update_doc)
# print(response)

def delete_docuemnt(index,id):
    resp = client.delete(index=index,id=id)
    return resp

# response = delete_docuemnt(index="index001",id=2)
# print(response)

documents = [
    {
        '_op_type':'index',
        '_index': 'products',
        '_source': {
            'name' : 'product 1',
            'price': 100.00,
            'category': 'boooks',
            'description': 'A good boook'
        }
    },{
        '_op_type':'index',
        '_index': 'products',
        '_source': {
            'name' : 'product 2',
            'price': 150.00,
            'category': 'boooks',
            'description': 'A good boook'
        }
    }
]

# success,failed= bulk(client,documents,index='products',raise_on_error=False)

# print(f'Successfully indexed {success} documents')
# print(f'Failed to index {len(failed)} documents')
# print(f'Errors: {failed}')


# response = client.search(index="products", query={
# "range":{
#     "price":{
#         "lt":300
#     }
# }
# })
# print(response)

query = {"match": {"name": "product"}}

results = client.search(index='products', query=query, filter={"range": {"price": {"gt": 100.00}}})

print(results)

