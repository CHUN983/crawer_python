import requests
from bs4 import BeautifulSoup
import pandas as pd
import copy


#將其變為函示使用

data_list=[]
url='https://mojim.com/twh163395.htm'
header={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36'}

reponse=requests.get(url,headers=header)
soup=BeautifulSoup(reponse.text, 'html.parser')
hb2=soup.find_all('dd', class_='hb2')
hb3=soup.find_all('dd',class_='hb3')
articles=soup.find_all('dl', class_='ha0')
#print(articles)



for a in hb2:
    data={}
    hc1=a.find('span', class_='hc1')
    hc2=a.find('span', class_='hc2')
    hc3=a.find('span', class_='hc3')
    hc4=a.find('span', class_='hc4')

    print(hc1.text)
    i=0
    while(len(hc2.text)!=i and str.isalpha(hc2.text[i])):i+=1
    if(len(hc2.text)!=i):print(hc2.text[i:i+7])
    data['專輯名稱']=hc1.text
    if(len(hc2.text)!=i):data['發行年分']=hc2.text[i:i+7]


    hc3=hc3.select('a')
    for b in hc3:
        print(b.text)
        data['歌名']=b.text
        data_list.append(data)
        data_list=copy.deepcopy(data_list)
        #單純使用data_list.copy.append(data)會有問題
        #出來後歌曲名稱會重複成最後一個歌曲
        #問題:值在append實質上沒被複製，位址還是相同，因此需要複製一份
    hc4=hc4.select('a')
    for b in hc4:
        print(b.text)
        data['歌名']=b.text
        data_list.append(data)
        data_list=copy.deepcopy(data_list)
        #data_list.append(data)
    print('')

for a in hb3:
    data={}
    hc1=a.find('span', class_='hc1')
    hc2=a.find('span', class_='hc2')
    hc3=a.find('span', class_='hc3')
    hc4=a.find('span', class_='hc4')

    print(hc1.text)
    i=0
    while(len(hc2.text)!=i and str.isalpha(hc2.text[i])):i+=1
    if(len(hc2.text)!=i):print(hc2.text[i:i+7])
    data['專輯名稱']=hc1.text
    if(len(hc2.text)!=i):data['發行年分']=hc2.text[i:i+7]


    hc3=hc3.select('a')
    for b in hc3:
        #'提供'在網站上特別寫出來，所以寫個條件判斷是否有提供
        if(b.text=='(提供)'):continue
        print(b.text)
        data['歌名']=b.text
        data_list.append(data)
        data_list=copy.deepcopy(data_list)
        #單純使用data_list.copy.append(data)會有問題
        #出來後歌曲名稱會重複成最後一個歌曲
        #問題:值在append實質上沒被複製，位址還是相同，因此需要複製一份
    hc4=hc4.select('a')
    for b in hc4:
        if(b.text=='(提供)'):continue
        print(b.text)
        data['歌名']=b.text
        data_list.append(data)
        data_list=copy.deepcopy(data_list)
        #data_list.append(data)
    print('')


df= pd.DataFrame(data_list)
df.to_excel('song.xlsx',index=False, engine='openpyxl')
'''
    num,i=1,0
    while(i<len(hc3.text)-1):
        if(str.isdigit(hc3.text[i]) and hc3.text[i+1]=='.'):
            if(num!=1): print('')
            num+=1
            i+=2
        print(hc3.text[i],end='')
        i+=1
    i=0
    if(hc4.text):
        while(i<len(hc4.text)-1):
            if(str.isdigit(hc4.text[i]) and hc4.text[i+1]=='.'):
                print("")
                num+=1
                i+=2
            print(hc4.text[i],end='')
            i+=1
    print("")
    print('')
'''
#本來要直接硬幹，直接把1.2.3.用條件判斷分開，但發現歌曲本身可能會有，像XXX2.0



# for a in article:
#     song= a.find("dl",class_="ha0")
#     print(song.a.text)

#with open('output.html','w',encoding='utf-8') as f:
#    f.write(reponse.text)
