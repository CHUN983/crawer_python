import imp
import requests
from bs4 import BeautifulSoup
import crawer_album
import crawer_song

url='https://mojim.com/twzc1.htm'
header={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36'}
responses=requests.get(url, headers=header)


soup=BeautifulSoup(responses.text, 'html.parser')
s_listA=soup.find('ul', class_='s_listA')
s_listA=s_listA.select('li')
for a in s_listA:
    a=a.find('a')
    htm='https://mojim.com'
    htm=htm+a['href']
    print(htm)
    crawer_song.song_(htm)

