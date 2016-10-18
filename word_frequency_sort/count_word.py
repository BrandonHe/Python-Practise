#!/usr/bin/python
"""Count words."""
import string
from collections import Counter
def count_words(s, n):
    """Return the n most frequently occuring words in s."""
    
    # Read words from string s into a list
    wordString = s
    # Convert the text to lower string
    wordString = string.lower(wordString)
    # Convert the punctuations to ' '
    for ch in '!"#$%&()*+,-./:;<=>?@[\\]^_`{|}~':
        wordString = string.replace(wordString, ch, ' ')
    # Read words from string s into a list
    wordList = wordString.split()
    sorted(wordList)
    # Tally occurrencies of words in list
    word = Counter(wordList)
    top_n = word.most_common(n);
    # Sorted words in list
    top_n = sorted(top_n, key=lambda x: -word[x])
    # Print the n most frequency words in string s
    return top_n


def test_run():
    """Test count_words() with some inputs."""
    print count_words("cat bat mat cat bat cat", 3)
    print count_words("betty bought a bit of butter but the butter was bitter", 3)


if __name__ == '__main__':
    test_run()