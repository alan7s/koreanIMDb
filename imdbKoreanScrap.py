import pandas as pd
import re
import os.path

from bs4 import BeautifulSoup
from requests import get

url= "https://www.imdb.com/search/title/?countries=kr&languages=ko&sort=release_date,desc&count=250&start="
name=[] #List titles names
id=[] #list imdb ID
kr_name=[] #List name in korean
wiki= "https://en.wikipedia.org/wiki/"
headers = {"Accept-Language": "en-US, en;q=0.5"}

def scrap(url):
    page = get(url,headers = headers)
    soup = BeautifulSoup(page.content, 'lxml')
    content = soup.find(id="main")
    for movieFrame in content.find_all("div", class_="lister-item mode-advanced"):
        movieFirstLine = movieFrame.find("h3", class_="lister-item-header")
        movieTitle = movieFirstLine.find("a").text
        movieID = movieFirstLine.find("a")['href'].replace("/title/","").replace("/","")
        name.append(movieTitle)
        id.append(movieID)
        linkwiki = wiki+movieTitle.replace(" ","_")
        print(linkwiki)
        scrapwiki(linkwiki)

def scrapwiki(url):
    page = get(url,headers = headers)
    soup = BeautifulSoup(page.content, 'lxml')
    content = soup.find(id="mw-content-text")
    titleLine = content.find_all('span',{'lang':'ko-Hang'})
    try:
        titleName = re.search('<span lang="ko-Hang" title="Korean language text">(.*)</span>', str(titleLine[1]))
        print(titleName.group(1))
        kr_name.append(titleName.group(1))
    except:
        error = "not found"
        print(error)
        kr_name.append(error)

def createCSV(): #create csv file
	df = pd.DataFrame({'Title':name,'ID':id,'Korean title':kr_name})
	df.to_csv('koreanTitles.csv', index=False, encoding='utf-8')

def saveCSV(): #save to the csv
	df = pd.DataFrame({'Title':name,'ID':id,'Korean title':kr_name})
	df.to_csv('koreanTitles.csv', mode='a', index=False, encoding='utf-8', header=False)

if not os.path.exists('./koreanTitles.csv'):
	createCSV() #file not exist

i = 1
while(i<=9751): #limit 9751
    print(i)
    LINK = url+str(i) #build the link
    scrap(LINK) #start web scraping
    i+=250

saveCSV() #append mode