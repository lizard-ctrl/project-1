
import tweepy
from authorization_tokens import *
import random

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)


virgo_list = [ " I'm such a virgo lol!" ,
                " Virgos are so crazy" ,
                " Don't you just love being a virgo hehe",
                " Virgos win again today!" ,
                " Virgos are literally the best" ,
                " Don't you wish you were a virgo",
                " its so great to be a virgo",
                " so glad i woke up today as a virgo!",
                " virgos do it the best",
                " thank god im a virgo!"
                ]




random_number = random.randrange(len(virgo_list))
virgo = virgo_list[random_number]




search_results = api.search( q= "lol", lang="en" )
random_number = random.randrange( len(search_results) )
random_tweet = search_results[random_number]
oldtweet = random_tweet.text


api.update_status(oldtweet + virgo)
print("Done.")
