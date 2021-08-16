import requests
import json

url = "http://localhost:7574/solr/collection_13/schema/analysis/synonyms/en"
payload = json.dumps({

    "Midi Skirt": [
        "kisa etek"
    ]

})
headers = {'Content-type': 'application/json'}
response = requests.request("PUT", url, headers=headers, data=payload)
print(response.text)
