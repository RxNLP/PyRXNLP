import requests
import json
from requests.packages.urllib3.exceptions import InsecureRequestWarning

requests.packages.urllib3.disable_warnings(InsecureRequestWarning)


endpoint_compute_similarity = "https://rxnlp-core.p.mashape.com/computeSimilarity"
endpoint_url_sent_clustering = "https://rxnlp-core.p.mashape.com/generateClusters"


def print_server_error(response):
    print("There was a problem with your request:")
    print("Status code: ", response)
    print("Server response: " + response.text)


def get_json_data(response):
    finalResponse = response.text
    dataUnloaded = json.loads(finalResponse)
    return dataUnloaded


def send_request(apikey, json_str, endpoint_url):
    headers = {'X-Mashape-Key': apikey}
    r = requests.post(
        endpoint_url,
        json=json_str,
        verify=False,
        headers=headers)
    return r


def check_key(key):
    if key in "not set":
        print("Your API Key is invalid or has not been set.")
        print("Type: key('your assigned key') to set it or update the config.cfg.")
        return -1
    else:
        return 1
