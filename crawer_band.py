import requests
from bs4 import BeautifulSoup
import pandas as pd
import copy

url='https://mojim.com/twzc1.htm'
header={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36'}
responses=requests.get(url, headers=header)


soup=BeautifulSoup(responses.text, 'html.parser')
s_listA=soup.find('ul', class_='s_listA')
s_listA=s_listA.select('li')
data_list=[]
for a in s_listA:
    data={}
    a=a.find('a')
    htm='https://mojim.com'
    htm=htm+a['href']
    print(a.text)
    data["樂團名稱"]=a.text
    responses_=requests.get(htm,headers=header)
    soup_=BeautifulSoup(responses_.text,'html.parser')
    hb0= soup_.find('dd', class_='hb0')
    i=0
    if(hb0 and hb0.text):
        while(not str.isdigit(hb0.text[i:i+4]) and i!=len(hb0.text)):
            i+=1
        print(hb0.text[i:i+4])
        data['出道年分']=hb0.text[i:i+4]
    else:
        print("null")
        data['出道年分']=''
    data_list.append(data)

df=pd.DataFrame(data_list)
df.to_excel('band.xlsx', index=False, engine='openpyxl')
