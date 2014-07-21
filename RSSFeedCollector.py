'''
Created on Jul 13, 2014

@author: ALLWINLEOPRAKASH
'''

import urllib2
import sys
from xml.dom import minidom


def main():
    pass

# URL for the rss feed 

rss_url = "http://www.icerocket.com/search?q=worldcup&tab=blog&rss=1"

# hdr included to exclude special characters in form of [CDATA!

params = {'User-Agent': 'Mozilla/5.0',
       'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8'}

#Get URL

def OPFileCheck():

    """Check existence of Output file FeedOutput.txt"""
    try:
        #reads the api key from the instagram_api.txt file
        fp = open("FeedOutput.txt")
        rssfeed = fp.readline()
        if rssfeed == "":
            print("The FeedOutput.txt file appears to be blank. Iteration starts now")
        fp.close()
    except IOError:
        print('Please create the Output file with name FeedOutput.txt and continue')
        sys.exit(0)
    except Exception as e:
        print(e)

def FeedCollector():

    feedw = open("FeedOutput.txt", "a")

    with open("FeedOutput.txt", "r") as feedr:
        feedsrc = feedr.read()
    
    try:
        resp = urllib2.Request(rss_url,headers=params)
    
        # Get RSS feed source
        briefingRSS = minidom.parse(urllib2.urlopen(resp))
    
        # Find each Upgrade and Downgrade listed in XML file
        channel = briefingRSS.getElementsByTagName("channel")[0]
        items = channel.getElementsByTagName("item")
        
        # Iteration to read, check and append the url
        for item in items:
            link_chk = item.getElementsByTagName("link")[0].firstChild.data
            op = item.getElementsByTagName("link")[0].firstChild.data+'-'+ item.getElementsByTagName("pubDate")[0].firstChild.data + '\n'
            # Condition to check new feed link
            if link_chk not in feedsrc:
                feedw.write(op)
                print 'New addition :'+op
            else:
                print 'No new addition'
    
    except Exception as e:
        print(e)
        print 'status:ERROR'+'-'+'statusInfo'+resp.status_code

    feedr.close()
    feedw.close()
