##• Go to https://petitions.whitehouse.gov/petitions 
##• Go to the petition page for each of the petitions. 
##• Create a .csv file with the following information for each petition:
##   – Title # h3
##   – Published date # h4 class 'petition-attribution'
##   – Issues #div class = 'field field-name-field-petition-issues field-type-taxonomy-term-reference field-label-hidden tags'
##   -- number of signatures #div class= 'signatures-progress-bar'
from bs4 import BeautifulSoup
import urllib2 
import random
import time
import os
import re
import csv

with open('hw2_dl.csv', 'wb') as f:
    w = csv.DictWriter(f, fieldnames = ("Title", "Published date", "Issues"))
    w.writeheader()
    web_address='https://petitions.whitehouse.gov/petitions'
    web_page = urllib2.urlopen(web_address)
    all_html = BeautifulSoup(web_page.read())
    all_html.prettify
    all_topic = all_html.find_all("h3")[3:]
    all_topics = [i.text for i in all_topics]
    topic = []
    extension=[]
    for i in all_topics:
        topic.append(i.encode('utf-8', 'ignore'))
    dates = all_html.find_all('div', {'h4' : "petition-attribution"})
   
    ## collect website extension for the publish date
    ext = all_html.find_all("a")
    for i in ext:
        extension.append(i['href'])


    for i in all_topic:
        extension.append = i.attrs["href"]

all_topics
