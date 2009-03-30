#!/usr/bin/python
#
# 12tweet - tiny little robots that live in the twittersphere
# Created by Jeff Verkoeyen @featherless
#
# The brains of a basic twitter bot. Does little more than print
# all tweets for the given twitter user.
#

import examplebot
import sys

bot = examplebot.Bot()

bot.execute()

# Fire off a tweet to the given user.
#bot.notifyUser('featherless', 'Hi featherless!')

# Print out user statistics.
#bot.printStats()
