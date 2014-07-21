'''
Created on Jul 17, 2014

@author: ALLWINLEOPRAKASH
'''

import RssFeedCollector as rs
import datetime 


rs.OPFileCheck()

var = 1


# Continuous active loop to retrieve real time data
while var == 1:
    sec = datetime.datetime.now().second
    # Check and append the new entries every 20 seconds
    if sec % 20 == 0:
        rs.FeedCollector()
