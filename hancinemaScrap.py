import pandas as pd
import re
import os.path

from bs4 import BeautifulSoup
from requests import get

url= "https://www.hancinema.net/all_korean_movies_dramas.php?nopage=" #0
name=[] #List titles names
kr_name=[] #List name in korean
headers = {"Accept-Language": "en-US, en;q=0.5"}

def scrap(url):
    page = get(url,headers = headers)
    soup = BeautifulSoup(page.content, 'html.parser')
    content = soup.find("div", class_="planning_film")
    for movieFrame in content.find_all("div"):
        movieFirstLine = movieFrame.find("p")
        movieTitle = movieFirstLine.find("a")
        name.append(re.search('">(.*) \(', str(movieTitle)).group(1))
        kr_name.append(re.search('<span>(.*)</span>', str(movieTitle)).group(1))

def createCSV(): #create csv file
	df = pd.DataFrame({'Title':name,'Korean title':kr_name})
	df.to_csv('koreanTitles2.csv', index=False, encoding='utf-8')

def saveCSV(): #save to the csv
	df = pd.DataFrame({'Title':name,'Korean title':kr_name})
	df.to_csv('koreanTitles2.csv', mode='a', index=False, encoding='utf-8', header=False)

if not os.path.exists('./koreanTitles2.csv'):
	createCSV() #file not exist

i = 0
while(i<=267): #limit 267
    print(i)
    LINK = url+str(i) #build the link
    scrap(LINK) #start web scraping
    i+=1

scrap(url)

saveCSV() #append mode