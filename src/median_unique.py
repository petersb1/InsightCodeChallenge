__author__ = 'Brock'

#Version 1: 7.10.2015

#calculate the median number of words in the set as each word arrives
#input directory: tweet_input file: tweets.txt
#output directory: tweet_output file: ft12.txt
#each word is considered an entity seperated by white space

from collections import Counter
import numpy as np
import sys

inFile = sys.argv[1]
outFile = sys.argv[2]

#read tweets into an array
with open(inFile) as f:
    lines = [line.rstrip('\n') for line in f]

#create variable to store median
median = []

#function to calculate median
def medianCalc(x):
    if isinstance(x,str):
        median = len(Counter(x.split()))
    else:
        medians=[]
        for i in range(len(x)):
            a = Counter(x[i].split())
            medians.append(len(a))
        median=np.median(medians)
    return median

#create loop to calcualte median of each new line
#ideally the run script would check for a new line then run the function if a new line existed. With this process a list of medians could be stored to reduce computation time.
for i in range(len(lines)):
    j = i+1
    t = lines[0:j]
    median.append(medianCalc(t))

#write to txt
with open(outFile, 'w') as textFile:
     for i in range(len(median)):
         textFile.write(str(median[i]) + '\n')
