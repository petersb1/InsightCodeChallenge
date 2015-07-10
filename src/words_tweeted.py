__author__ = 'Brock'

#Version 1: 7.10.2015

#calculate total number of times each word has been tweeted
#input directory: tweet_input file: tweets.txt
#output directory: tweet_output file: ft1.txt
#each word is considered an entity seperated by white space

from collections import Counter
import sys

inFile = sys.argv[1]
outFile = sys.argv[2]

#read tweets into an array
with open(inFile) as f:
    lines = [line.rstrip('\n') for line in f]

#concatinate all words to a single string
words=[]
for i in range(len(lines)):
   words=words+lines[i].split()

#use Counter to count individual words
words = sorted(Counter(words).items())

#write to txt
with open(outFile, 'w') as textFile:
     for i in range(len(words)):
         textFile.write(str(words[i][0]) + ' ' + str(words[i][1]) + '\n')