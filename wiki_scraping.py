#!/usr/bin/env python
# coding: utf-8

# In[1]:


import requests
from bs4 import BeautifulSoup
import random


# In[18]:


def scrapeWikiArticle(url):
        response = requests.get(url=url,)
        soup = BeautifulSoup(response.content, 'html.parser')

        title = soup.find(id="firstHeading")
        print(title.text)
        
        allLinks = soup.find(id="bodyContent").find_all("a")
        #print(allLinks)
        random.shuffle(allLinks)
        linkToScrape = 0

        for link in allLinks:
            # We are only interested in other wiki articles
            if link['href'].find("/wiki/") == -1: 
                continue
            # Use this link to scrape
            linkToScrape = link
            break
            
        scrapeWikiArticle("https://en.wikipedia.org" + linkToScrape['href'])            
scrapeWikiArticle("https://en.wikipedia.org/wiki/Web_scraping")


# reference: https://www.freecodecamp.org/news/scraping-wikipedia-articles-with-python/

# In[ ]:




