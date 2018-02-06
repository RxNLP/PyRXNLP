"""
Clustering sentences from a list of sentences, a file or just some chunk of text.
"""
import os
from pyrxnlp.api.cluster_sentences import ClusterSentences

apikey = "your_api_key"

if __name__ == '__main__':

    # Examples:
    # Cluster from a list of sentences
    list_of_sentences = [
        "the sky is so high",
        "the sky is blue",
        "fly high into the sky.",
        "the trees are really tall",
        "I love the trees",
        "trees make me happy",
        "the sun is shining really bright"]
    clustering = ClusterSentences(apikey)
    clusters = clustering.cluster_from_list(list_of_sentences)

    if clusters is not None:
        print("------------------------------")
        print("Clusters from a list of sentences")
        print("------------------------------")
        clustering.print_clusters(clusters)

    # Cluster from plain text
    clustering = ClusterSentences(apikey)
    clusters = clustering.cluster_from_text(
        "Philadelphia (CNN) Michelle Obama cast the presidential race as one between a positive role model for children -- in Hillary Clinton -- and a damaging one -- in Donald Trump -- in the marquee speech on the Democratic National Convention's opening night. The first lady never mentioned Trump by name, but leveraging her popularity, she made a rare, if not unprecedented, foray into partisan politics to knock the Republican nominee.Obama condemned the hateful language that we hear from public figures on TV, saying that our motto is, when they go low, we go high.And in a shot at Trump's Make America Great Again campaign slogan, Obama discussed raising her children in a White House that was built by slaves.Memorable lines from the DNC's opening night Don't let anyone tell you that this country isn't great. This right now is the greatest country on earth, the first lady said. Obama electrified the crowd at the Wells Fargo Arena in Philadelphia, taking the stage just after 10 p.m. ET and -- in a departure from the political attacks on display all day -- making the case that, because of her character and temperament, Clinton is the role model she'd like her daughters to see in the Oval Office.It was a remarkable embrace of the prime-time stage for Obama, who was reluctant about the spotlight that came when her husband, then-Illinois Sen. Barack Obama, launched his presidential campaign against Clinton in 2007. To understand the journey she's taken as a reluctant conscript on the public scene, to come here and command that stage the way she did tonight was extraordinary -- and I think did for Hillary Clinton what no one else has done to this point, said David Axelrod, a top Obama strategist on the 2008 campaign and now a CNN political commentator.")
    if clusters is not None:
        print("------------------------------")
        print("Clusters from a chunk of text")
        print("------------------------------")
        clustering.print_clusters(clusters)

    # Cluster from a text file
    abspath = os.path.dirname(os.path.abspath(__file__))
    file = abspath + "/../../corpora/clusteringsentences.txt"
    clustering = ClusterSentences(apikey)
    clusters = clustering.cluster_from_textfile(file)
    if clusters is not None:
        print("------------------------------")
        print("Clusters from a file")
        print("------------------------------")
        clustering.print_clusters(clusters)
