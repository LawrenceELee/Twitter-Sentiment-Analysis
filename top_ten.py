import sys                        #used to access sys.argv
import json                       #used to encoded JSON data from twitter
import operator                   #used for sorting hashtags
from pprint import pprint as pp

def read_input(filename, data):
  with open(filename, 'r') as in_stream:
    for line in in_stream:
      data.append(json.loads(line))

def parse_tweets(tweets, hashtag_counts):
  """
  Input:  List of JSON encoded objects representing tweets with their fields as a dictionary
  Output: Dictionary with key: hashtags and val: counts
  """
  for tweet in tweets:
    list_of_entities = tweet['entities']
    #pp(list_of_entities)
    list_of_hashtags = list_of_entities['hashtags']
    #pp(list_of_hashtags)
    for hashtag in list_of_hashtags:
      text = hashtag['text']
      if text in hashtag_counts:
        hashtag_counts[text] += 1
      else:
        hashtag_counts[text] = 1

def sort_hashtags(hashtag_counts):
  """
  Input:  Dictionary of hashtags and their counts
  Output: List of tuples (hashtag, count) sorted in descending order
  """
  sorted_hashtags = sorted(hashtag_counts.iteritems(), key=operator.itemgetter(1), reverse=True)
  return sorted_hashtags

def top_ten(hashtags):
  """
  Input:  List of tuples (hashtag, count) sorted in descending order
  Output: print "<hashtag: utf-8 string> <count: integer>"
  """
  for i in range(10):
    (ht, count) = hashtags[i]                   #python idiomatic way to unpacking hashtag tuple
    print "%s %i" % (ht.encode("utf-8"), count) #tell print that string is encoded in utf-8

def nested_for_loop_test():
  """
  I used this function to test out how nested for loops work in python
  """
  for i in range(5):
    for j in range(10):
      print ("%i %i") % (i, j)

def main():
  tweets = []
  hashtag_counts = {}

  read_input(sys.argv[1], tweets)
  #pp(tweets)

  parse_tweets(tweets, hashtag_counts)
  #pp(hashtag_counts)

  sorted_hashtags = sort_hashtags(hashtag_counts)
  #pp(sorted_hashtags)

  top_ten(sorted_hashtags)

  #nested_for_loop_test()


if __name__ == "__main__":
  main()
