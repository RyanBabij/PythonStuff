from bs4 import BeautifulSoup

import requests


baseURL = "https://news.google.com/"

r = requests.get(baseURL)

data = r.text

soup = BeautifulSoup(data)

print "RIP START\n"

f = open("headlines.txt", "w")

for link in soup.find_all('h3'):
  print link.text.strip().encode('utf-8')
  f.write(link.text.strip().encode('utf-8')+"\n")
  
print "\n\n"

for link in soup.find_all('h4'):
  print link.text.strip().encode('utf-8')
  f.write(link.text.strip().encode('utf-8')+"\n")

from collections import Counter

infile = "headlines.txt"
outfile = "headlinesKeywords.txt"

delete_list = [" during ", " but ", " who ", " before ", " to ", " in ", " on ", " of ", " for ", " after ", " the ", " and ", " at ", " a ", " over ", " the ", "The ", " from ", " can ", " with ", " as ", " says ", " by ", "0", "1", "2", "3", "4", "5", "6", "7", "8", "9", ":", "$", " m ", "|"]
fin = open(infile)
fout = open(outfile, "w+")
for line in fin:
    for word in delete_list:
        line = line.replace(word, " ")
    fout.write(line)
fin.close()
fout.close()


print "\n\n\n"

#opens the file. the with statement here will automatically close it afterwards.
with open("headlinesKeywords.txt") as input_file:

    #build a counter from each word in the file
    count = Counter(word for line in input_file
                         for word in line.split())


print(count.most_common(20))

print "\n\n"
