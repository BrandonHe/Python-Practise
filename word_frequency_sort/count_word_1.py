"""Count words."""

def count_words(s, n):
    """Return the n most frequently occuring words in s."""

    wordsList = s.split()
    wordFreq = []   # list store all uniq words from s
    wordCount = []  # list store the word count
    top_n = []      # list store the required answer

    # loop to find all words
    for i in range(0, len(wordsList)):          
        if wordsList[i] not in wordFreq:
            wordFreq.append(wordsList[i])
            currentWord = wordsList[i]
            count = 0
            # loop to count the curent word
            for word in range(0,len(wordsList)):   
                if currentWord == wordsList[word]:
                    count = count + 1
            
            wordCountTuple = (currentWord,count)
            wordCount.append(wordCountTuple)
    
    # sort by values
    sortedWordCount = sorted(wordCount,key=lambda(k,v):(-v,k))

    for item in range(0, n):
        top_n.append(sortedWordCount[item])
    return top_n


def test_run():
    """Test count_words() with some inputs."""
    print count_words("cat bat mat cat bat cat", 3)
    print count_words("betty bought a bit of butter but the butter was bitter", 3)


if __name__ == '__main__':
    test_run()
