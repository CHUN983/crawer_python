from select import select
import requests
from bs4 import BeautifulSoup
import pandas as pd
import copy

def album_(htm):
    url=htm
    header={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36'}

    reponse=requests.get(url,headers=header)
    soup=BeautifulSoup(reponse.text, 'html.parser')
    hb2=soup.find_all('dd', class_='hb2')
    hb3=soup.find_all('dd',class_='hb3')
    articles=soup.find_all('dl', class_='ha0')
    #print(articles)

    data_list=[]

    for a in hb2:
        data={}
        hc1=a.find('span', class_='hc1')
        hc2=a.find('span', class_='hc2')
        print(hc1.text)
        #先把前面的文字挑掉，然後判斷有無日期
        i=0
        while(len(hc2.text)!=i and str.isalpha(hc2.text[i])):i+=1
        if(len(hc2.text)!=i):print(hc2.text[i:i+7])
        data['專輯名稱']=hc1.text
        if(len(hc2.text)!=i):data['發行年分']=hc2.text[i:i+7]

        data_list.append(data)

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
        
        data_list.append(data)



    df= pd.DataFrame(data_list)
    df.to_excel('album.xlsx',index=False, engine='openpyxl')
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
