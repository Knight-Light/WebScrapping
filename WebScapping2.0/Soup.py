import numpy as np
import requests
import pandas as pd
from bs4 import BeautifulSoup
import sqlite3
import re


with open("DataCollected.html", "r", encoding="utf8") as f:
    html_1 = f.read()
    f.close()

soup = BeautifulSoup(html_1, 'html.parser')
Link=[]

t1 = soup.find("div", {'align':'center'})
#print(t1)

t2 = t1.find("table", {'class':'mobview'})

for link in t2.findAll('a'):
    a = "https://main.sci.gov.in"
    data = str(link.get('href'))
    d1 = a + data
    Link.append(d1)

Date = []

for t3 in t2.findAll('td'):
    b = t3.text
    if b != '':
        Date.append(b)


info = {Link[i]:Date[i] for i in range(len(Link))}
print(len(info))


#https://main.sci.gov.in/
'''for link in soup.findAll('a'):
    print(link.get('href'))
'''

D1 = []
for t4 in t2.findAll('th'):
    c = t4.text
    if c != '':
        D1.append(c)

Desc = np.unique(D1)
print(Desc)

for info[]