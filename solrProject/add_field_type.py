import json
import requests

def add_field_type(collection_name):
    url = "http://localhost:7574/solr/" + collection_name + "/schema"
    headers = {'Content-type': 'application/json'}

    with open("field-types.json") as field_type_json:
        data = json.load(field_type_json)

    for language in data.keys():
        for field_type in data[language]:
            payload = json.dumps({"add-field-type": field_type})
            response = requests.request("POST", url, headers=headers, data=payload)
            print(response.text)





