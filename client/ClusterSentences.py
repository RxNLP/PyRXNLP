
import json

from utils.setup import send_post_request

apikey = "your_api_key"
endpoint_url = "https://rxnlp-core.p.mashape.com/generateClusters"


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


def make_request(sentences, isChunk):
    data = {}

    if isChunk == False:
        data['type'] = 'pre-sentenced'
        data['text'] = [dict(sentence=s) for s in sentences]
    else:
        data['type'] = 'chunk'
        data['text'] = sentences

    resp = send_request(data, endpoint_url)

    if resp.status_code == 200:
        finalResponse = resp.text
        dataUnloaded = json.loads(finalResponse)
        clusters = dataUnloaded['results']['clusters']
        return clusters

    else:
        print("There was a problem with your request:")
        print("Status code: ", resp)
        print("Server response: " + resp.text)
        return None


def cluster_from_list(mylist):
    """ cluster sentences from list of sentences (pre-sentenced)"""

    clusters = make_request(mylist, False)
    return clusters


def cluster_from_text(text):
    """ cluster a chunk of text (sentence boundary unknown) """

    clusters = make_request(text, True)
    return clusters


def cluster_from_textfile(fname):
    """ cluster a chunk of text from file """

    with open(fname) as f:
        content = f.readlines()

    # make it one big text
    text = '\n'.join(content);
    clusters = make_request(text, True)
    return clusters


def printClusters(clusters):
    if clusters != None:
        for c in clusters:

            # To get individual topics, clean and split it
            title = "Cluster Topic(s): {0}, Score {1}".format(c['clusterTopics'], c['clusterScore'])
            print(title)

            # print sentences belonging to a cluster
            for sent in c['clusteredSentences']:
                print("\t", sent)

            print("===")


# first set api key
if set_api_key("your_api_key"):

    ## Examples:
    ## Cluster from a list of sentences
    listOfSentences = ["the sky is so high", "the sky is blue", "fly high into the sky.", "the trees are really tall",
                       "I love the trees", "trees make me happy", "the sun is shining really bright"]
    clusters = cluster_from_list(listOfSentences)
    if clusters is not None:
        print("Clusters from a list of sentences")
        print("##################################")
        printClusters(clusters)

    ## Cluster from plain text
    clusters = cluster_from_text(
        "Philadelphia (CNN) Michelle Obama cast the presidential race as one between a positive role model for children -- in Hillary Clinton -- and a damaging one -- in Donald Trump -- in the marquee speech on the Democratic National Convention's opening night. The first lady never mentioned Trump by name, but leveraging her popularity, she made a rare, if not unprecedented, foray into partisan politics to knock the Republican nominee.Obama condemned the hateful language that we hear from public figures on TV, saying that our motto is, when they go low, we go high.And in a shot at Trump's Make America Great Again campaign slogan, Obama discussed raising her children in a White House that was built by slaves.Memorable lines from the DNC's opening night Don't let anyone tell you that this country isn't great. This right now is the greatest country on earth, the first lady said. Obama electrified the crowd at the Wells Fargo Arena in Philadelphia, taking the stage just after 10 p.m. ET and -- in a departure from the political attacks on display all day -- making the case that, because of her character and temperament, Clinton is the role model she'd like her daughters to see in the Oval Office.It was a remarkable embrace of the prime-time stage for Obama, who was reluctant about the spotlight that came when her husband, then-Illinois Sen. Barack Obama, launched his presidential campaign against Clinton in 2007. To understand the journey she's taken as a reluctant conscript on the public scene, to come here and command that stage the way she did tonight was extraordinary -- and I think did for Hillary Clinton what no one else has done to this point, said David Axelrod, a top Obama strategist on the 2008 campaign and now a CNN political commentator.")
    if clusters is not None:
        print("Clusters from a chunk of text")
        print("##################################")
        printClusters(clusters)

    ## Cluster from a text file
    file = "../examples/clusteringsentences.txt"
    clusters = cluster_from_textfile(file)
    if clusters is not None:
        print("Clusters from a file")
        print("##################################")
        printClusters(clusters)
