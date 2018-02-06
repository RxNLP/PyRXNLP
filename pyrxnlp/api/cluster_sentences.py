from pyrxnlp.api import util


class ClusterSentences:
    def __init__(self, apikey):
        self.apikey = apikey

    def make_request(self, sentences, is_chunk):
        data = {}

        if not is_chunk:
            data['type'] = 'pre-sentenced'
            data['text'] = [dict(sentence=s) for s in sentences]
        else:
            data['type'] = 'chunk'
            data['text'] = sentences

        resp = util.send_request(
            self.apikey, data, util.endpoint_url_sent_clustering)

        if resp.status_code == 200:
            data = util.get_json_data(resp)
            clusters = data['results']['clusters']
            return clusters

        else:
            util.print_server_error(resp)
            return None

    def cluster_from_list(self, mylist):
        """ cluster sentences from list of sentences (pre-sentenced)"""

        clusters = self.make_request(mylist, False)
        return clusters

    def cluster_from_text(self, text):
        """ cluster a chunk of text (sentence boundary unknown) """

        clusters = self.make_request(text, True)
        return clusters

    def cluster_from_textfile(self, fname):
        """ cluster a chunk of text from file """

        with open(fname) as f:
            content = f.readlines()

        # make it one big text
        text = '\n'.join(content)
        clusters = self.make_request(text, True)
        return clusters

    def get_sentences(self, cluster):
        clust_dict = cluster['clusteredSentences']
        [[key] for key in cluster['clusteredSentences']]

    def print_clusters(self, clusters):
        if clusters is not None:
            for c in clusters:

                cluster_labels = c['clusterTopics']
                cluster_score = c['clusterScore']
                sentences = list(c['clusteredSentences'].values())

                # To get individual topics, clean and split it
                print("Cluster label: ", cluster_labels)
                print("Cluster scores: ", cluster_score)
                print("Cluster sentences: ", sentences)

                print("===")
