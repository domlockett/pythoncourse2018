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
topic = []
date = []
web_page = []
web_address = []
temp = []
temp1 = []
sign = []
site = []
name = []
all_topic = []
all_topics = []
ext = []
all_html = []
with open('hw2_dl.csv', 'wb') as f:
    w = csv.DictWriter(f, fieldnames = ("Title", "Published date", "Issues"))
    w.writeheader()



def get_data():
    ## PETITION SITES
    for i in range(0,4):
        web_address = 'https://petitions.whitehouse.gov/?page=' + '%s' % i
        web_page = urllib2.urlopen(web_address) ## having figured it below I know this can be more
        all_html.append(BeautifulSoup(web_page.read()))#eloquent will fix if remaining work time <2hrs

    for i in all_html:
        try:
            ext.append(i.find_all("a"))
        except AttributeError:
            ext.append("NA")

    for i in ext:
        for j in i:
            try:
                if j['href'][0:10] == '/petition/':
                    site.append("https://petitions.whitehouse.gov" +( j['href'].encode('utf-8')))
            except KeyError:
                site.append('NA')

    site = site[2::2]
    ##TITLES
    for i in site:
        name.append(BeautifulSoup(urllib2.urlopen(i).read()).find('h1').get_text().encode('utf-8'))

    ## NUMBER OF SIGNATURES
    for i in all_html:
        temp1.append(i.find_all('span', {'class': "signatures-number"}))
    for j in temp1:
        for e in j:
            sign.append(e.get_text().encode('utf-8'))

     ## ISSUES
        


def why()


BeautifulSoup(urllib2.urlopen(site[1]).read())
