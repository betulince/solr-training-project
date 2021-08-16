import requests
import json


def add_document(collection_name):
    url = "http://localhost:7574/solr/" + collection_name + "/update?commitWithin=100"
    headers = {'Content-Type': 'application/json'}

    with open('fields.json') as field_json:
        field_data = json.load(field_json)
    en_fields = field_data["EN"]
    nolang_fields = field_data["NOLANG"]
    field_list = en_fields + nolang_fields
    with open('/home/betul/products.json') as product_file:
        product_data = json.load(product_file)

        product_available_fields = ['name', 'brand', 'productId']
        for product in product_data:
            my_docs = {}
            for field in product_available_fields:
                for solr_field in field_list:
                    if solr_field["productAccessor"] == field:
                        my_docs_key = solr_field["name"].replace("#", "EN").replace("*", "EN")
                        my_docs[my_docs_key] = product[field]

            #print(my_docs)

            payload = json.dumps({
                "add": {
                    "doc":
                        my_docs
                }
            })

            print(payload)
            response = requests.request("POST", url, headers=headers, data=payload)
            print(response.text)

"""

        for field in data:  # field.keys() = name,brand,productId
            field_list = ['image', 'price', 'oldPrice', 'inStock', 'categories', 'params', 'url']
            for deleted_field in field_list:
                if deleted_field in field:
                    del field[deleted_field]

            for key in field.keys():
                for f in en_fields:
                    if f["productAccessor"] == key:
                        field[f["name"].replace("#", "EN")] = field[key]
                        del field[f["productAccessor"]]

            payload = json.dumps({
                "add": {
                    "doc":
                        field
                }
            })

            print(payload)
            response = requests.request("POST", url, headers=headers, data=payload)
            print(response.text)
"""