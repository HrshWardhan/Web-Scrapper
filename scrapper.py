from bs4 import BeautifulSoup
import requests
import urllib
import os
from os.path import basename
def func(str):
    if(str=="January"):
        return 1
    elif(str=="Feburaury"):
        return 2
    elif(str=="March"):
        return 3    
    elif(str=="April"):
        return 4
    elif(str=="May"):
        return 5
    elif(str=="June"):
        return 6
    elif(str=="July"):
        return 7
    elif(str=="August"):
        return 8
    elif(str=="September"):
        return 9
    elif(str=="October"):
        return 10 
    elif(str=="November"):
        return 11
    elif(str=="December"):
        return 12           
f = open("inp.txt","r")
s = f.readline()
e = f.readline()
c = f.readline()
creators = c.split()
st =  s.split()
en = e.split()
m1 = func(st[0])
m2 = func(en[0])
y1 = int(st[1])
sto = y1
y2 = int(en[1])
def store(month,year,url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html5lib')
    imgUrp = soup.find('img',id="main-comic")
    imgUrl = imgUrp['src']
    sur = url
    url="http:"+imgUrl
    #print(imgUrl)
    response = requests.get(url)
    na = soup.find('div', id="comic-author").contents
    ka = na[2].split()
    #filename = str(year)+"/"+str(month)+"/"+sur.split('/')[-2]+".png"
    filename = str(year)+"/"+str(month)+"/"+na[0][4:]+"-"+ka[1]+".png"
    #print(filename)
    urllib.urlretrieve(url,filename)
def parse(month , year):
    url = "http://explosm.net/comics/archive/"+str(year)+"/";
    if(month<10):
        url+="0"
    url+=str(month)
    for cre in creators:
        url+="/"
        url+=cre
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html5lib')
    links = soup.findAll('div',class_="row collapse")
    for img in links: 
        cre = img.find('div')
        cro = cre.find('a')
        store(month,year,"http://explosm.net"+cro['href'])
path =  os.getcwd() 
while(y1<=y2):
    if not os.path.exists(str(y1)):
        os.makedirs(str(y1))    
    if(y1==sto):
        for i in range(m1,13):
            os.chdir(path+"/"+str(y1))
            if not os.path.exists(str(i)):
                os.makedirs(str(i))
            os.chdir(path)    
            parse(i,y1)
            
    elif(y1==y2):
        for i in range(1,13):
            os.chdir(path+"/"+str(y1))
            if not os.path.exists(str(i)):
                os.makedirs(str(i))
            os.chdir(path)    
            parse(i,y1)
    else:
        for i in range(1,m2+1):
            os.chdir(path+"/"+str(y1))
            if not os.path.exists(str(i)):
                os.makedirs(str(i))
            os.chdir(path)    
            parse(i,y1) 
    y1+=1            
