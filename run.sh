#brock petersen
#edited 7/10/2015

#!/usr/bin/env bash

#Used example script to run word count and median numbers of words 

# I'll execute my programs, with the input directory tweet_input and output the files in the directory tweet_output
python ./src/words_tweeted.py ./tweet_input/tweets.txt ./tweet_output/ft1.txt
python ./src/median_unique.py ./tweet_input/tweets.txt ./tweet_output/ft2.txt



