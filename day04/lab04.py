## Go to https://polisci.wustl.edu/faculty/specialization
## Go to the page for each of the professors.
## Create a .csv file with the following information for each professor:
## 	-Specialization
## 	-Name
## 	-Title
## 	-E-mail
## 	-Web page
	
from bs4 import BeautifulSoup
import csv 
import urllib2 
import random
import time
import os


web_address = 'https://polisci.wustl.edu/faculty/specialization'
web_page = urllib2.urlopen(web_address)
soup = BeautifulSoup(web_page.read())
soup.prettify()
page= soup.find_all('a')
page= page[14:57]
data =soup.find_all('div', {'class': 'views-row'})

ext=[]
name=[]
title=[]
web=[]
biggun=[]
## 
## website
for i in page:
         ext.append(i['href'])
ext = ext[11:54]
def site():
    for i in ext:
        if i[0]=='/':
            web.append('https://polisci.wustl.edu'+i)
        else:
            web.append(i)
site()

## name and title

for i in range(0,len(page)):
    name.append(str(data[i].get_text().split('\n')[1]))
    title.append(str(data[i].get_text().split('\n')[2]))

##website
for line in web:
    web_address = 'https://polisci.wustl.edu/faculty/specialization'
    web_page = urllib2.urlopen(web_address)
    soup = BeautifulSoup(web_page.read())
    biggun.append(soup)


address = 'https://polisci.wustl.edu/faculty/jeremy-caddel'
web_page = urllib2.urlopen(address)
test = BeautifulSoup(web_page.read())
mail=test.find_all('div',{'class': 'field-item even'})
mail= []
for i in web:
    web_page = urllib2.urlopen(i)
    test = BeautifulSoup(web_page.read())
    a[1]['a']
    mail.append()
    