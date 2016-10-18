#!/usr/bin/python

from collections import Counter
wordstring = 'it it was it was the best of times it was the worst of times was was it was of'
# Function returns the most frequently occurring words in string
def count_words(string, number):
	wordlist = string.split()
#	wordfreq = []
#	for word in wordlist:
#		wordfreq.append(wordlist.count(word))
	
	word = Counter(wordlist)
	print(word.most_common(number))
#	print("Output\n" + str(zip(wordlist, wordfreq)))

count_words(wordstring, 4)

