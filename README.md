# Twining
The twitter data mining tools that can help you gather information by keyword.

![](https://img.shields.io/badge/twinning-v1.0-blue) ![](https://img.shields.io/badge/python-v3.7.2-yellow) ![](https://img.shields.io/badge/tweepy-v3.8.0-blue)

## Requirements  :
- Python 3
- pip3
- Tweepy 3.8.0

## How to :

Clone :

`$ git clone https://github.com/syhbt/twining.git`

Change directory to cloned project :

`$ cd twining/`

Install requirements :

`$ pip install -r requirements.txt`

Edit this code :

    token = "ACCESS-TOKEN"
    token_secret = "ACCESS-TOKEN-SECRET"
    consumer_key = "API_KEY"
    consumer_secret = "API_KEY_SECRET"

*) note : you can get the token and consmer key at the twitter developer pages.

*) More info : https://developer.twitter.com/en/docs/basics/authentication/guides/access-tokens

## Usage :

`$ python3 twining.py --help`

Example : 

`$ python twining.py  -k Porgramming -o Output.txt`

This program will automatically retrieve data streaming from Twitter. The duration of data retrieval affects the amount of data obtained. The longer you run this program, the more data you get.