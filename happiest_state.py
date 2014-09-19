import sys
import json
import string
import operator
from pprint import pprint as pp

def read_data(filename, data):
    """
    Input:      filename, string representing name of file containing tweets
                data, empty list buffer to be filled with JSON objects representing tweets
    Output:     None
    """
    with open(filename) as in_stream:
        for line in in_stream:
            data.append(json.loads(line))

def read_sentiments(sent_file, sent_hash):
    """
    Input:      filename string representing name of afinn file
                sent_hash, empty dict buffer to be filled with <word: string> <sentiment: int>
    Output:     None
    """
    with open(sent_file) as in_stream:
        for line in in_stream:
            sent = line.strip().split('\t')             #have to split on tabs in case of 2 word phrases seperated by space
            #pp(sent)
            sent_hash[sent[0]] = int(sent[1])

def parse_tweets(list_of_tweets, hash_of_afinn, happiest_state):
    """
    Input:      List of JSON objects, each representing a tweet.
                Hash of AFINN, <word: string> <sentiment: int>
                happiest_state, is a hash of <state: string> <sentiment: int>
    Output:     None
    """
    for tweet in list_of_tweets:
        text = extract_text(tweet)
        #pp(text)
        state = extract_state(tweet)
        #pp(state)
        sentiment = calculate_sent(text, hash_of_afinn)
        #pp(sentiment)
        if not None:
            calculate_state_sent(state, sentiment, happiest_state)

    #code to handing ugly data
    if None in happiest_state:
        del happiest_state[None]

def extract_text(tweet):
    """
    Input:      tweet, JSON object with all fields
    Output:     list of words, the text portion of the tweet JSON object
    """
    return tweet['text'].lower().split()

def extract_state(tweet):
    if tweet.get('place') is None:
        return None

    locations = tweet.get('place').get('full_name')
    tokens = locations.split(', ')

    """
    #for debugging
    pp(locations)
    print len(locations)
    pp(tokens)
    print len(tokens)


    """
    for t in tokens:
        #print t.encode("utf-8")
        #print lookup_state(t.encode("utf-8"))
        #print lookup_state(t)
        return lookup_state(t)

def calculate_sent(text, afinn):
    """
    Input:      text, list of unicode words to look up in afinn
                afinn, hash with words and their sentiment values
    Output:     sent, integer representing the sentiment value of entire text string
    """
    sent = 0
    for word in text:
        if word in afinn:
            sent += int(afinn.get(word))
    return sent

def calculate_state_sent(state, sent, happiest_state):
    if state not in happiest_state:          #this if check is required b/c += will look for key, and if it doesn't exist, it will raise a KeyError
        happiest_state[state] = sent
    else:
        happiest_state[state] += sent

def lookup_state(state_string):
    """
    TODO: doesn't differentiate between Washington state and Washington DC
    """
    states = { 'AK': 'Alaska', 'AL': 'Alabama', 'AR': 'Arkansas', 'AS': 'American Samoa', 'AZ': 'Arizona', 'CA': 'California', 'CO': 'Colorado', 'CT': 'Connecticut', 'DC': 'District of Columbia', 'DE': 'Delaware', 'FL': 'Florida', 'GA': 'Georgia', 'GU': 'Guam', 'HI': 'Hawaii', 'IA': 'Iowa', 'ID': 'Idaho', 'IL': 'Illinois', 'IN': 'Indiana', 'KS': 'Kansas', 'KY': 'Kentucky', 'LA': 'Louisiana', 'MA': 'Massachusetts', 'MD': 'Maryland', 'ME': 'Maine', 'MI': 'Michigan', 'MN': 'Minnesota', 'MO': 'Missouri', 'MP': 'Northern Mariana Islands', 'MS': 'Mississippi', 'MT': 'Montana', 'NA': 'National', 'NC': 'North Carolina', 'ND': 'North Dakota', 'NE': 'Nebraska', 'NH': 'New Hampshire', 'NJ': 'New Jersey', 'NM': 'New Mexico', 'NV': 'Nevada', 'NY': 'New York', 'OH': 'Ohio', 'OK': 'Oklahoma', 'OR': 'Oregon', 'PA': 'Pennsylvania', 'PR': 'Puerto Rico', 'RI': 'Rhode Island', 'SC': 'South Carolina', 'SD': 'South Dakota', 'TN': 'Tennessee', 'TX': 'Texas', 'UT': 'Utah', 'VA': 'Virginia', 'VI': 'Virgin Islands', 'VT': 'Vermont', 'WA': 'Washington', 'WI': 'Wisconsin', 'WV': 'West Virginia', 'WY': 'Wyoming' } 

    states_abbrv_to_name = {key.upper():key.upper() for key, val in states.iteritems()} #convert to upper
    #{ 'CA': 'CA', 'AK': 'AK' , etc... }
    states_name_to_abbrv = {val.upper():key.upper() for key, val in states.iteritems()} #swap key and val
    #{ 'CALIFORNIA': 'CA', 'ALASKA': 'AK' , etc... }

    #print "str: %r" % state_string.encode("utf-8")
    #return ("%s, %s") % (states_abbrv_to_name.get(state_string.upper()), "abbrv -> name")
    #return ("%s, %s") % (states_name_to_abbrv.get(state_string.upper()), "lookup")

    return states_abbrv_to_name.get(state_string.upper()) or states_name_to_abbrv.get(state_string.upper())

def sort_hash(hash):
    return sorted(hash.iteritems(), key=operator.itemgetter(1), reverse=True)

def happiest(states):
    sorted_states = sort_hash(states)
    name, sent = (sorted_states[0])
    print ("%s") % (name)
            
def main():
    tweets = []
    sent_hash = {}
    happiest_state = {}


    read_data(sys.argv[2], tweets)
    read_sentiments(sys.argv[1], sent_hash)
    #pp(tweets)

    parse_tweets(tweets, sent_hash, happiest_state)

    happiest(happiest_state)




if __name__ == "__main__":
    main()
