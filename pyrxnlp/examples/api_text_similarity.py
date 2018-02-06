from pyrxnlp.api.text_similarity import TextSimilarity


apikey = "your_api_key"


if __name__ == '__main__':
    str1 = "this is, the first string for my test!"
    str2 = "this ## is the second string for my testing...."

    # show cosine,dice,jaccard similarity with cleaning
    t = TextSimilarity(apikey, True)
    t.show_similarity(str1, str2)
    print("====\n")

    # show cosine,dice,jaccard similarity with no cleaning
    t = TextSimilarity(apikey, False)
    t.show_similarity(str1, str2)
    print("====\n")

    # get cosine,dice,jaccard similarity and print with cleaning
    t = TextSimilarity(apikey, True)
    sims = t.get_similarity(str1, str2)
    print("Sims:", sims)
