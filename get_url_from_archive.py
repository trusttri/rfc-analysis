import json
import re
import datetime
import urllib2
from os import walk


# using the mediawiki, in the current page look up the sections.

# if there is the RfC, keep the url


# else, get the page url and using BeautifulSoup scrape all the anchors. Extract the anchor containing "archive"


# Using 1,2,3.. iterate over the archives until the section exists