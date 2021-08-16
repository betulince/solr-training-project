import requests


def create_collection(collection_name):
    configset_name = collection_name + "_config"
    url = "http://localhost:7574/solr/admin/collections?action=CREATE&name=" + collection_name + "&numShards=1" \
                                                                                                 "&replicationFactor=1&wt=json&collection.configName=" + configset_name + ""
    payload = {}
    headers = {}
    response = requests.request("POST", url, headers=headers, data=payload)
    print(response.text)
