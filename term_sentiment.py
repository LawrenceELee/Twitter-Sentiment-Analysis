import sys
import pprint as pp
import json
import re
import operator


def load_json(filename, data):
    with open(filename, 'r') as infile_handle:
        for line in infile_handle:
            data.append(json.loads(line))

def load_sent(filename, data):
    with open(filename, 'r') as infile_handle:
        for line in infile_handle:
            word, sent = line.strip().split("\t")
            #print("%s %i") % (word, int(sent))
            data[word] = int(sent)

def calculate_sent(json_list, sent_dict, unknown_words):
    regex = re.compile('[%s]' % re.escape("!.,?:;(){}{}[]+=/\~`$%^&*\"-_"))

    for line in json_list:
        text = regex.sub('', line['text'])
        text = text.lower().split()
        total_sent = 0
        unknown_words_tmp = []

        for word in text:
            if word in sent_dict:
                total_sent += sent_dict.get(word) 
            else:
                unknown_words_tmp.append(word)

                if word not in unknown_words:
                    unknown_words[word] = {'sent':0.0, 'count':1,} 
                else:
                    unknown_words[word]['count'] += 1

        for word in unknown_words_tmp:
            unknown_words[word]['sent'] += total_sent
        #pp.pprint(unknown_words)
        #pp.pprint(text)
        #print(total_sent)

def calculate_avg(unknown_words):
    tmp = {}
    for key,val in unknown_words.iteritems():
        #print("%f/%f = %f") % (val['sent'], val['count'], round(val['sent']/val['count']))
        tmp[key] = int(round(val['sent']/val['count']))
    return tmp

def sort(word_counts):
    '''
    returns a list
    '''
    sorted_words = sorted(word_counts.iteritems(), key=operator.itemgetter(1), reverse=True)
    return sorted_words

def print_output(my_dict):
    for key, val in my_dict.iteritems():
        print("%s %s") % (key.encode('utf-8'), val)

def main():
    sent_filename = sys.argv[1]
    tweet_filename = sys.argv[2]

    sent_file = open(sent_filename)
    tweet_file = open(tweet_filename)

    sentiments = {}
    tweets = []
    unknown = {}

    load_sent(sent_filename, sentiments)
    load_json(tweet_filename, tweets)

    calculate_sent(tweets, sentiments, unknown)
    new_word_sent = calculate_avg(unknown)

    print_output(new_word_sent)
    

if __name__ == '__main__':
    main()
