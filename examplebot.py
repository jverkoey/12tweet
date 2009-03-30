#!/usr/bin/python
#
# 12tweet - tiny little robots that live in the twittersphere
# Created by Jeff Verkoeyen @featherless
#
# The brains of a basic twitter bot. Does little more than print
# all tweets for the given twitter user.
#

import twitterbot
import random

class Bot(twitterbot.StandardBot):
    '''A generic twitter bot.
    '''
    def __init__(self):
        twitterbot.StandardBot.__init__(self,
            dbuser = "12tweet",
            dbpass = "12tweet21r!",
            dbdb   = "12tweet",
            twituser = '12tweetbot',
            twitpass = '12tweet21r!')


    def execute(self):
        # Fetch all tweets since our last commit.
        tweets = self.getTweets()

        # Commit our tweets right away. If there are any errors in code following
        # this, we won't run into an infinite loop of tweets being pulled.
        # You might choose to commit the tweets at a later point, however.
        self.commitTweets()

        if len(tweets) == 1:
            print str(len(tweets)) + " new tweet"
        elif len(tweets) > 1:
            print str(len(tweets)) + " new tweets"
        for tweet in tweets:
            if tweet.user.screen_name in self.existing_users:
                print tweet.user.screen_name+": " + tweet.text
            else:
                # Someone who isn't following us has sent us a reply.
                print "I don't know this person: " + tweet.user.screen_name

