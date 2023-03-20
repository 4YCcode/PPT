import requests
from bs4 import BeautifulSoup 
import os #更改檔案存放路徑os模組

url='https://www.ptt.cc/bbs/Gossiping/index.html'
web=requests.get('https://www.ptt.cc/bbs/Gossiping/index.html',cookies={'over18':'1'})
web.encoding='utf-8'
soup=BeautifulSoup(web.text,'html.parser') #網頁解析器
# print(web.text)
titles=soup.find_all('div',class_='title')
output=""
# for i in titles:
#     print(i.find('a').get_text())
#     print(i.find('a')['href'])
#     print()
for i in titles:
    output=output+i.find('a').get_text()+'\n'+i.find('a')['href']+'\n'
print(output)
os.chdir('d:/Python-training/project/ppt/') #更改檔案存放路徑
f=open('pptdata.xls','w+')
f.write(output)
f.close()


