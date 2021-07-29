# import required modules
from bs4 import BeautifulSoup
import requests
import random
import math
import webbrowser
import re

total = input("How many Layers Deep?: ")
print("Spider Webs")
for x in range(0,int(total)):
    if(x ==0):
        page = requests.get("https://en.wikipedia.org/wiki/Spider_web")
  
        # scrape webpage
        soup = BeautifulSoup(page.content, 'html.parser')
  
        # create object
        object = soup.find(id="mw-content-text")
  
        # find tags
        items = object.find_all('a',attrs={'href': re.compile("/wiki/")})  
        links = []
        # display tags
        for result in items:
            if result['href'].find(".jpg") == -1 and result['href'].find("disambiguation") == -1 and result['href'].find("#") == -1 and result['href'].find("identifier") == -1 and result['href'].find("/wiki/") != -1 and result['href'].find("wikimedia") == -1 and result['href'].find("/File:") == -1 and result['href'].find("Category") == -1 and result['href'].find("Special:") == -1 and result['href'].find("Wikipedia:") == -1 and result['href'].find("Help:") == -1 and result['href'].find("Template") == -1 and result['href'].find("wiktionary") == -1: 
                links.append(result['href'])
  
        random.shuffle(links)
        chosen = ""
        for x in range(0,len(links[0])):
            if links[0][x] != "_":
                chosen = chosen + links[0][x]
            else:
                chosen = chosen + " "
        print(chosen[6:])
    else:
        page = requests.get("https://en.wikipedia.org/" + links[0], 'html.parser')
        soup = BeautifulSoup(page.content,'html.parser')
        object = soup.find(id="mw-content-text")
        items = object.find_all('a',attrs={'href': re.compile("/wiki/")})
        links= []
        for result in items:
            if result['href'].find(".jpg") == -1 and result['href'].find("disambiguation") == -1 and result['href'].find("#") == -1 and result['href'].find("identifier") == -1 and result['href'].find("/wiki/") != -1 and result['href'].find("wikimedia") == -1 and result['href'].find("/File:") == -1 and result['href'].find("Category") == -1 and result['href'].find("Special:") == -1 and result['href'].find("Wikipedia:") == -1 and result['href'].find("Help:") == -1 and result['href'].find("Template") == -1 and result['href'].find("wiktionary") == -1 and result['href'].startswith("/wiki/"): 
                links.append(result['href'])
        
        random.shuffle(links)
        chosen = ""
        for x in range(0,len(links[0])):
            if links[0][x] != "_":
                chosen = chosen + links[0][x]
            else:
                chosen = chosen + " "
        print(chosen[6:])
