from bs4 import BeautifulSoup

import requests


baseURL = "https://boards.4chan.org/v/thread/430384643"

r = requests.get(baseURL)

data = r.text

soup = BeautifulSoup(data)

f = open("4chanscrape.txt", "w")
  
for br in soup.find_all("br"):
    br.replace_with("\n")
  
for link in soup.find_all('blockquote'):
  if link.has_attr('class') and link['class'] == [u'postMessage']:
    f.write("  [POST]\n\n"+link.text.strip().encode('utf-8')+"\n\n")
