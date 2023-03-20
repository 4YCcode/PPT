
import requests
from bs4 import BeautifulSoup

web=requests.get('https://water.taiwanstat.com/')
soup=BeautifulSoup(web.text,'html.parser')
reservoir=soup.select('.reservoir')
for i in reservoir:
    print(i.find('h3').get_text(),end=" ") #取得內容h5 tag的文字
    print(i.find('h5').get_text(),end=" \n")
    
    
    