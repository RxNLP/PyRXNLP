.. _pyrxnlp---text-mining-tools-for-building-intelligent-data-driven-applications:

PyRXNLP - Text-mining tools for building intelligent data-driven applications.
------------------------------------------------------------------------------

Features:
---------

-  Topics extraction
-  Sentence clustering - with cluster labels
-  Opinosis opinion summarization

Getting Started:
----------------

1. Install pyrxnlp

::

    pip install pyrxnlp

2. If you are using the cloud APIs, get your `API Key`_

3. Start coding. Here's an example of **Clustering Sentences**

.. code:: python

        apikey = "your_api_key"

       # Cluster from a list of sentences
        list_of_sentences = [
            "the sky is so high",
            "the sky is blue",
            "fly high into the sky.",
            "the trees are really tall",
            "I love the trees",
            "trees make me happy",
            "the sun is shining really bright"]

        # initialize sentence clustering
        clustering = ClusterSentences (apikey)

        # generate clusters and print
        clusters = clustering.cluster_from_list (list_of_sentences)
        if clusters is not None:
            print ("------------------------------")
            print ("Clusters from a list of sentences")
            print ("------------------------------")
            clustering.print_clusters (clusters)


You should see output similar to:

::

    ------------------------------
    Clusters from a list of sentences
    ------------------------------
    Cluster label:  ['sky']
    Cluster scores:  6.571693476432014
    Cluster sentences:  ['fly high into the sky.', 'the sky is so high', 'the sky is blue']
    ===
    Cluster label:  ['tree']
    Cluster scores:  6.571693476432014
    Cluster sentences:  ['I love the trees', 'trees make me happy', 'the trees are really tall']
    ===
    Cluster label:  ['sentences_with_no_cluster_membership']
    Cluster scores:  0.0
    Cluster sentences:  ['0006:the sun is shining really bright']
    ===

.. _API Key: http://www.rxnlp.com/api-key/