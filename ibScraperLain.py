from bs4 import BeautifulSoup

import requests

baseURL = "https://lainchan.org/sec/res/4243.html"

r = requests.get(baseURL)

data = r.text

soup = BeautifulSoup(data)

f = open("LainChanScrape.txt", "w")
  
for br in soup.find_all("br"):
  br.replace_with("\n")
  
#for link in soup.find_all('p'):
  #f.write(link.text.strip().encode('utf-8')+"\n\n")

  
#for link in soup.find_all('label'):
  #if link.has_attr('for'):
    #f.write("\n\n  ["+link.text.strip().encode('utf-8')+"]\n\n")
  #else:
    
  

for link in soup.find_all(['div','label']):
  if link.has_attr('class') and link['class'] == [u'body']:
    f.write(link.text.strip().encode('utf-8')+"\n\n")
  if link.has_attr('for'):
    f.write("\n  ["+link.text.strip().encode('utf-8')+"]\n\n")
