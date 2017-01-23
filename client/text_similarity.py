from stemming.porter2 import stem
import json
import string

from utils.setup import send_post_request

apikey = "your_api_key"
endpoint_url = "https://rxnlp-core.p.mashape.com/computeSimilarity"


def set_api_key(key):
    global apikey
    apikey = key

    if key in "your_api_key":
        print("Please set your API Key and Try Again!")
        return False

    return True


def send_request(json_str, endpoint_url):
    headers = {'X-Mashape-Key': apikey}
    r = send_post_request(json_str, endpoint_url, headers)
    # r = requests.post(myUrl, json=myJson, verify=False, headers=headers)
    return r


def make_request(text1, text2, clean):
    data = {}

    data['text1'] = text1
    data['text2'] = text2

    if clean:
        data['clean'] = "true"
    else:
        data['clean'] = "false"

    resp = send_request(data, endpoint_url)

    if resp.status_code == 200:
        finalResponse = resp.text
        dataUnloaded = json.loads(finalResponse)
        return dataUnloaded

    else:
        print("There was a problem with your request:")
        print("Status code: ", resp)
        print("Server response: " + resp.text)
        return None

def print_similarities(label,data):
    print("{0} :".format(label))
    print("===========================")
    print("Dice similarity {0}".format(data['dice']))
    print("Cosine similarity {0}".format(data['cosine']))
    print("Jaccard similarity {0}".format(data['jaccard']))
    print("Average {0}".format(data['average']))


# first set api key
if set_api_key("your_api_key"):
    str1 = "this is, the first string for my test!"
    str2 = "this is the second string for my testing...."

    # Similarity with cleaning
    similarities = make_request(str1, str2, True)
    print_similarities("Similarity with cleaning",similarities)

    # Similarity with no cleaning
    similarities = make_request(str1, str2, False)
    print_similarities("Similarity with no cleaning",similarities)


    # Similarity with cleaning and stemming
    translator = str.maketrans('', '', string.punctuation)

    # strip punctuation
    str1 = str1.translate(translator)
    str2 = str2.translate(translator)

    # stem str1
    tmp = [stem(word) for word in str1.split(" ")]
    str1 = ' '.join(tmp)

    # stem str2
    tmp = [stem(word) for word in str2.split(" ")]
    str2 = ' '.join(tmp)

    # improved similarity agreement with stemming
    similarities = make_request(str1, str2, True)
    print_similarities("Similarity with stemming and cleaning",similarities)