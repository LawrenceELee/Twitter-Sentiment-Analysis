import sys
import json
from pprint import pprint as pp

def hw():
    print 'Hello, world!'

def lines(fp):
    print str(len(fp.readlines()))

def parse_afinn(afinn_file, scores):
    afinnfile = open(afinn_file)
    #scores = {} # initialize an empty dictionary
    for line in afinnfile:
        term, score  = line.split("\t")  # The file is tab-delimited. "\t" means "tab character"
        scores[term] = int(score)  # Convert the score to an integer.

    #print scores.items() # Print every (term, score) pair in the dictionary
    #print scores
    #print "score %i" % scores['good']

def read_tweets(filename):
    """Read the JSON formatted tweets into a list"""
    read_data = []
    with open(filename, 'r') as infile:
        for line in infile:
            #read_data.append(line)
            read_data.append(json.loads(line))

    return read_data

def parse_tweets(tweets, afinn_hash):
    """Parse and do sentiment calculation on tweet text."""
    for tweet in tweets:
        #pp(tweet['text'])
        #print "%s" % tweet['text']
        #print "%r" % tweet['text']
        words = tweet['text'].lower().split()

        senti = 0
        val = 0
        for word in words:
            if word in afinn_hash:
                val = afinn_hash[word]
            else:
                val = 0

            senti += val
            #pp(word)
            #pp(val)

        pp(senti)


def main():
    #sent_file = open(sys.argv[1])

    tweets = read_tweets(sys.argv[2])

    afinn_hash = {}
    parse_afinn(sys.argv[1], afinn_hash)

    #pp(tweets)
    #pp(tweets[0])

    parse_tweets(tweets, afinn_hash)

    """
    print ""
    print ""
    print "lines in output.txt %i" % len(tweets)
    lines(sent_file)
    """

if __name__ == '__main__':
    main()
