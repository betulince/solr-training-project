import requests
import json

def add_field(collection_name):
    url = "http://localhost:7574/solr/" + collection_name + "/schema"
    headers = {
        'Content-type': 'application/json'
    }
    with open('fields.json') as field_json:
        data = json.load(field_json)
        for language in data.keys():
            for field in data[language]:
                if language != 'NOLANG':
                    field['name'] = field['name'].replace('#', language).replace('*', language)

                field_list = ['productAccessor', 'orig', 'facetField', 'textSorting', 'dataLoadType']
                for deleted_field in field_list:
                    if deleted_field in field:
                        del field[deleted_field]

                request_type = "add-field"
                if field['indexType'] == 'dynamicField':
                    request_type = "add-dynamic-field"
                if 'indexType' in field:
                    del field['indexType']
                payload = json.dumps({request_type: field})
                print(payload)

                response = requests.request("POST", url, headers=headers, data=payload)
                print(response.text)
