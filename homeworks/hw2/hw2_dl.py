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
web_page = []
web_address = []
all_html = []
ext = []
site = []
name = []
temp = []
sign = []
temp1 = []
temp2 = []
topic = []
date = []
fin = []
issue= []
date = []
store = {"Topic":[], "Name":[], "Sigs":[], "Date":[]}

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
            pass


site = site[1::2]
site.pop(41)
site.pop(60)
##TITLES:
for i in site:
    name.append(BeautifulSoup(urllib2.urlopen(i).read()).find('h1').get_text().encode('utf-8'))
    if (BeautifulSoup(urllib2.urlopen(i).read()).find('h1').get_text().encode('utf-8'))[0:16] == "Log In or Create":
        pass
    else:
        name.append(BeautifulSoup(urllib2.urlopen(i).read()).find('h1').get_text().encode('utf-8'))

 ## NUMBER OF SIGNATURES
for i in all_html:
    temp.append(i.find_all('span', {'class': "signatures-number"}))
for j in temp:
    for e in j:
        sign.append(e.get_text().encode('utf-8'))

    ## ISSUES

for i in all_html:
    temp1 +=( i.find_all('div', {'class':"field-items"}))
temp1 = temp1[1:]
for j in temp1:
    try:
        temp2 += j.find_all('h6')
        for i in temp2:
            fin+=[(str(i.get_text()))]
        issue += [fin]
        temp2 = []
        fin = []
    except:
        issue += 'NA'

issue.insert(12, '[]')
issue.pop(-7)
issue.pop(19)
issue.pop(40)
    ## Date
for i in site:
    try:
        date.append(BeautifulSoup(urllib2.urlopen(i).read()).find('h4').get_text().encode('utf-8').split('on',1)[-1])
    except AttributeError:
        date.append('na')

       



    ## WRITE THIS BASTARD
with open('C:/Python27.14/pythoncourse2018/homeworks/hw2/hw2_dl.csv', 'wb') as f:
    w = csv.DictWriter(f, fieldnames = ("Title of Petition", "Published Date", "Issues","Number of Signatures"))
    w.writeheader()
    for i in range(0,len(name)):
        w.writerow({"Title of Petition": name[i], "Published Date": date[i], "Issues": issue[i], "Number of Signatures": sign[i]})


