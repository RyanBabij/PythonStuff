from bs4 import BeautifulSoup

import requests

baseURL = "https://8ch.net/agdg/res/28950.html"

r = requests.get(baseURL)

data = r.text

soup = BeautifulSoup(data)


f = open("8chanscrape.txt", "w")

for link in soup.find_all('p'):
  if link.has_attr('class') and link['class'] == [u'intro']:
    print "\n"+link.text.strip().encode('utf-8')+"\n\n"
    f.write("\n\n ["+link.text.strip().encode('utf-8')+"]\n\n")
  else:
    print link.text.strip().encode('utf-8')
    f.write(link.text.strip().encode('utf-8')+"\n")
