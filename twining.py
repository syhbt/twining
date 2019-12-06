#!/usr/bin/python3

# I made a simple program to collect data on Twitter for fun. 
# You can also use this program as a data mining tool for students who are conducting a study of data science.
# I think it's so cute, learning python at the same time while I learning data science.
# Syhbt - 2019.

import argparse
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream

print ('''
            #################################
            #                               #
            #      Twitter Text Mining      #
            #                               #
            #################################
''')


token = "ACCESS-TOKEN"
token_secret = "ACCESS-TOKEN-SECRET"
consumer_key = "API_KEY"
consumer_secret = "API_KEY_SECRET"

parser = argparse.ArgumentParser(usage='twining.py -k KEYWORD -o FILE.TXT\n       twining.py -h (Show helps)\n       twining.py --version (Print version)')

parser.add_argument('-k', required=True, help='Keyword to filter tweet (ex: Python, Ruby, Java)', dest='keyword')
parser.add_argument('-o', required=True, help='Save to file (ex: output.txt)', dest='file')
parser.add_argument('--version', action='version', version='Twining v1.0')

args = parser.parse_args()

key = args.keyword
output_file = args.file

class Listener(StreamListener):
    def on_status(self, status):
        if hasattr(status, "retweeted_status"):
            try:
                tls = status.retweeted_status.extended_tweet['full_text']
                file = open(output_file, 'a')
                file.write(tls)
                file.close()
            except AttributeError:
                tls = status.retweeted_status.text
                file = open(output_file, 'a')
                file.write(tls)
                file.close()
        else:
            try:
                tls = status.extended_tweet['full_text']
                file = open(output_file, 'a')
                file.write(tls)
                file.close()
            except AttributeError:
                tls = status.text
                file = open(output_file, 'a')
                file.write(tls)
                file.close()
    def on_error(self, status):
        print(status)

if __name__ == "__main__":
    try:
        listen = Listener()
        auth = OAuthHandler(consumer_key,consumer_secret)
        auth.set_access_token(token, token_secret)
        run = Stream(auth, listen)

        run.filter(track=[key])
    except KeyboardInterrupt:
        print ('\n[*] Program stopped by user.')