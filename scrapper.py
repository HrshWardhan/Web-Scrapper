from bs4 import BeautifulSoup
import requests
import urllib
import os
from os.path import basename
import sys

def sav(i,url):
    filename = "random/frame"+str(i)+".png"
    urllib.urlretrieve(url,filename)
def sav1(url,filename):
    urllib.urlretrieve(url,filename)    
def ran():
    if not os.path.exists("random"):
        os.makedirs("random")  
    url = "http://explosm.net/rcg";
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html5lib')
    #print(soup)
    links = soup.find('div',class_="rcg-panels")
    #print(links)
    im = links.find_all('img')
    i = 1;    
    for img in im:
        sav(i,img['src'])
        #print(img['src'])
        i+=1         
def func(str):
    if(str=="January"):
        return 1
    elif(str=="February"):
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
st =  s.split()
if(st[0]=="random"):
    ran()
    sys.exit()
if(st[0]=="latest"):
    if not os.path.exists("latest"):
        os.makedirs("latest")
    num = int(st[1])
    url = "http://explosm.net"
    for i in range(1,num+1):
        response = requests.get(url)
        soup = BeautifulSoup(response.content, 'html5lib')
        na = soup.find('div', id="comic-author").contents
        ka = na[2].split()
        links = soup.find('img',id="main-comic")
        link = "http:"+links['src']
        sav1(link,"latest"+"/"+na[0][4:]+"-"+ka[1]+".png")
        re = soup.find('a' , class_ = "nav-previous")
        url = "http://explosm.net"+re['href']
    sys.exit()    

e = f.readline()
c = f.readline()
creators = c.split()
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
        krl = url
        url+="/"
        url+=cre
        response = requests.get(url)
        soup = BeautifulSoup(response.content, 'html5lib')
        links = soup.findAll('div',class_="row collapse")
        for img in links: 
            cre = img.find('div')
            cro = cre.find('a')
            store(month,year,"http://explosm.net"+cro['href'])
        url = krl    
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
