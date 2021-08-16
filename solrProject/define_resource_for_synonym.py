import requests
import json

url = "http://localhost:7574/solr/collection_13/schema/analysis/synonyms/en"

payload = json.dumps({
  "class": "org.apache.solr.rest.schema.analysis.ManagedSynonymGraphFilterFactory$SynonymManager"
})
headers = {
  'Content-Type': 'application/json'
}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)