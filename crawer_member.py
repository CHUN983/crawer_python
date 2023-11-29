import requests
from bs4 import BeautifulSoup
import copy
import pandas as pd

url='https://zh.wikipedia.org/zh-tw/%E7%BE%8E%E7%A7%80%E9%9B%86%E5%9C%98'
user={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36'}
response=requests.get(url,headers=user)

soup=BeautifulSoup(response.text, 'html.parser')
plainlist=soup.find('div', class_='plainlist')
plainlist=plainlist.select('li')

data_list1=[]
data_list2=[]

for a in plainlist:
    data={}
    i=0
    while(a.text[i]!='（'): i+=1
    print(a.text[:i])
    data['成員本名']=a.text[:i]
    data_list2.append(data)
    tmp=i+1
    while(a.text[i]!='）'):
        if(a.text[i]=='、'):
            print(a.text[tmp:i])
            data['成員樂團位置']=a.text[tmp:i]
            data_list1.append(data)
            data_list1=copy.deepcopy(data_list1)
            tmp=i+1
        i+=1
    print(a.text[tmp:i])
    data['成員樂團位置']=a.text[tmp:i]
    data_list1.append(data)
    data_list1=copy.deepcopy(data_list1)
    #有些位置沒有連結= =
    # role=a.select('a')
    # for b in role:
    #     print(b.text)

df_1= pd.DataFrame(data_list1)
df_1.to_excel('location.xlsx',index=False, engine='openpyxl')

df_2= pd.DataFrame(data_list2)
df_2.to_excel('member.xlsx',index=False, engine='openpyxl')
