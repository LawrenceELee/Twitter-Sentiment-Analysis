#Files:
----------
```
I used some geo-fencing to limit tweets from the US so that they are mainly
in English so I can spot check them.
```

##tweet_sentiment.py
Calculate overall positive or negative of a tweet.


##term_sentiment.py
Calculate a new sentiment score for words not in AFINN list using the sentiment of the surrounding words that we know sentiments for.


##frequency.py
Creates frequency histogram of most used words in tweets.


##happiest_state.py
Calculates sentient for each tweet, then sums up all tweets for each state.


##top_ten.py
Calculates the top ten hashtags.


##data/sample_tweet_data.json:
Some sample tweet data that I scraped from the twitter firehose.


##data/AFINN-111.txt
##data/AFINN-README.txt
holds a list of words with their associated negative/positive value


##out:
Hold results after running analysis programs.


#Usage:
----------
python term_sentiment.py data/AFINN-111.txt data/sample_tweet_data.json > out/term_sentiment.out


#Results:
----------
```
Some sample results: I, the, to, a, you, my are some of the most frequent words.
frequency.out
[(u'i', 2997),
 (u'the', 2283),
 (u'to', 2102),
 (u'a', 1846),
 (u'you', 1553),
 (u'my', 1509),
 (u'and', 1173),
 (u'in', 1076),
 (u'me', 1072),
 (u'is', 946),
```


```
Happiest state: according to my time slice of the data.
happiest_state.out
NY
```


```
hermano (not in AFINN-111) has a neutral sentiment.
term_sentiment.out
@shalei 0
tilton 0
@thatssoclarisa 2
hanging 0
@cmk817 3
igual 0
tía 0
hermann 3
hermano 0
⚾ 0
```


```
Top ten hashtags from my time slice are below:
top_ten.out
CamTweetMe 90
Job 89
Jobs 64
TweetMeCam 59
tbt 46
TweetMyJobs 41
tweetmecam 28
MTVHottest 22
TBT 16
VeteranJob 16
```


```
1st tweet in my data file has neutral sentiment, 3rd tweet has positive (4), etc.
tweet_sentiment.out
0
0
4
0
0
0
2
0
0
0
```
