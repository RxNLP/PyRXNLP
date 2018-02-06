from pyrxnlp.api import util


class TextSimilarity:

    def __init__(self, apikey, clean=False):
        self.apikey = apikey
        self.clean = clean

    def make_request(self, text1, text2):
        if util.check_key(self.apikey):
            data = {}
            data['text1'] = text1
            data['text2'] = text2

            if self.clean:
                data['clean'] = "true"
            else:
                data['clean'] = "false"

            resp = util.send_request(
                self.apikey, data, util.endpoint_compute_similarity)

            if resp.status_code == 200:
                return util.get_json_data(resp)
            else:
                util.print_server_error(resp)
                return None

    def print_similarities(self):
        data = self.output
        if data is not None:
            print("Dice similarity {0}".format(data['dice']))
            print("Cosine similarity {0}".format(data['cosine']))
            print("Jaccard similarity {0}".format(data['jaccard']))
            print("Average {0}".format(data['average']))

    def show_similarity(self, text1, text2):
        similarities = self.make_request(text1, text2)
        self.output = similarities
        self.print_similarities()

    def get_similarity(self, text1, text2):
        """get similarity between two pieces of text"""
        similarities = self.make_request(text1, text2)
        return similarities
