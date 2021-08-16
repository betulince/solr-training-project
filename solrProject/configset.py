import requests


def create_configset(collection_name):
    configset_name = collection_name + "_config"
    url = "http://localhost:7574/solr/admin/configs?action=CREATE&name=" + configset_name + "&baseConfigSet=_default" \
                                                                                            "&configSetProp.immutable" \
                                                                                            "=false&wt=xml&omitHeader" \
                                                                                            "=true "
    payload = {}
    headers = {}
    response = requests.request("POST", url, headers=headers, data=payload)
    print(response.text)
