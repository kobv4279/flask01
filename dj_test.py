#conda python3.6.9
#대전 교육청 구직페이지 크롤링해서 mongodb-hire-daejon  테이블에 넣는것
import requests
from bs4 import BeautifulSoup
from pymongo import MongoClient
from datetime import datetime

url = "http://www.dje.go.kr/boardCnts/list.do?boardID=54&m=031001&s=dje"
r = requests.get(url)
bs = BeautifulSoup(r.text,"html.parser")
lists = bs.select("td.link")

for i in lists:
    current_utc_time = round(datetime.utcnow().timestamp()*1000)
    print(i.a.text)

