from elasticsearch import Elasticsearch
from flask import Flask, request, jsonify
from datetime import datetime

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

app = Flask(__name__)

index = "products006"

@app.route('/products', methods=['POST'])
def create_product():
    data = request.get_json()
    data['timestamp'] = datetime.now()

    response = client.index(index=index,document=data)
    print(response)
    return jsonify({'message':'product created successfully','result': response['result']}),201

@app.route('/products/<string:id>', methods=['GET'])
def read_product(id):
    response = client.get(index=index, id=id)

    if response['found']:
        return jsonify(response['_source']),200
    else:
        return jsonify({'message':'product not found'}),404


@app.route('/products/<string:id>', methods=['PUT'])
def update_product(id):
    data = request.get_json()
    data['timestamp'] =datetime.now()

    response = client.update(index=index,id=id,doc=data)
    return jsonify({'message': 'product updated successfully','result': response['result']}),200


@app.route('/products/<string:id>',methods=['DELETE'])
def delete_product(id):
    response = client.delete(index=index,id=id)
    if response['result'] == 'deleted':
        return jsonify({"message": "product deleted successfully"}),200
    else:
        return jsonify({"message": "Product not found"}),404


@app.route('/products',methods=['GET'])
def list_products():
    query = request.args.get('query')

    if query:
        response = client.search(index=index, query={"match":{'name':query}})
        products = [hit['_source'] for hit in response['hits']['hits']]
    else:
        response = client.search(index=index,query={'match_all':{}})
        products = [hit['_source'] for hit in response['hits']['hits']]

    return jsonify(products),200


if __name__ == '__main__':
    app.run(debug=True)