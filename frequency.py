# -*- coding: utf-8 -*-
#for unicode encoding?
import sys  #used to get argv inputs
import json #use to load json
from pprint import pprint as pp
import re #used to strip punctuation

import operator #use to sort dictionary

def readfile(filename, data):
    with open(filename, 'r') as infile:
        for line in infile:
            data.append(json.loads(line))

def extract_text(tweets, word_counts):
    total_words = 0
    #use regex to strip certain types of punct in tweet text, use re.escape b/c some chars have special meaning
    regex = re.compile('[%s]' % re.escape("!.,?:;(){}{}+=/\~`$%^&*"))
    for tweet in tweets:
        text = tweet['text'].lower()
        text = regex.sub('', text)
        text = text.split()
        for word in text:
            total_words += 1
            if word in word_counts:
                word_counts[word] += 1
            else:
                word_counts[word] = 1
    return total_words

def find_max(word_counts):
    sorted_words = sorted(word_counts.iteritems(), key=operator.itemgetter(1), reverse=True)
    return sorted_words
  
def compute_freq(word_counts, total_count):
    for (key, val) in word_counts.iteritems():
        ratio = float(val) / total_count
        print ("%s %f") % (key.encode("utf-8"), ratio)


def main():

    tweets = []
    word_counts = {}

    readfile(sys.argv[1], tweets)
    total_count = extract_text(tweets, word_counts)
    sorted_words = find_max(word_counts)

    pp(sorted_words)

    #compute_freq(word_counts, total_count)


    """
    my_list = find_max(word_counts)
    for i in range(10):
      print my_list[i]
    """

if __name__ == "__main__":
    main()
