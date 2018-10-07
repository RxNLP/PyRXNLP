## PyRXNLP - Python SDK for RxNLP's Text Mining APIs 

Build intelligent data-driven applications with minimal effort. 

## APIs 
- [Topics extraction](http://www.rxnlp.com/api-reference/topics-and-themes-api-reference/)
- [Sentence clustering](http://www.rxnlp.com/sentence-clustering-api/) - with cluster labels
- [HTML2Text](http://rxnlp.com/api-reference/html2text-api/#.W7VaQxNKj64)
- [Opinion Summarization](https://market.mashape.com/rxnlp/text-mining-and-nlp#opinosis-summaries)
- [Text Similarity](http://rxnlp.com/text-similarity-api/#.W7VaEBNKj64)
- [N-Gram Counter](http://rxnlp.com/api-reference/n-gram-and-word-counter-api-reference/#.W7VaJhNKj64)


## Getting Started:

1. Install pyrxnlp
  ```
  pip install pyrxnlp
  ```

2. Get your [API Key](http://www.rxnlp.com/api-key/). 

3. Start coding. Here's an example of **Clustering Sentences**. 

Replace `your_api_key` with an actual key.

```python
   
   import os
   from pyrxnlp.api.cluster_sentences import ClusterSentences

   # replace this with your api key (see: http://www.rxnlp.com/api-key/)
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


```

You should see output similar to:

```
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

```

Here's an example for computing Text Similarity:

```python
from pyrxnlp.api.text_similarity import TextSimilarity

apikey = "your_api_key"


str1 = "this is, the first string for my test!"
str2 = "this ## is the second string for my testing...."

# Example 1: show cosine,dice,jaccard similarity with cleaning
t = TextSimilarity(apikey, True)
t.show_similarity(str1, str2)
print("====\n")

#Example 2: show cosine,dice,jaccard similarity with no cleaning
t = TextSimilarity(apikey, False)
t.show_similarity(str1, str2)
print("====\n")
    
```

## Code Examples & Tutorials
- You will find working examples under [pyrxnlp/examples/](https://github.com/RxNLP/PyRXNLP/tree/master/pyrxnlp/examples)

## Contributing 

### Reporting issues

When reporting issues please use "Github Issues" and include as much detail as possible about your operating system, python version and API endpoint used if applicable. Whenever possible, please also include a brief, self-contained code example that demonstrates the problem. Visuals are appreciated!

