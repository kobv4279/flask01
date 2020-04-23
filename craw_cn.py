from urllib.request import urlopen

import requests
from bs4 import BeautifulSoup
url = 'http://www.jne.go.kr/board/list.jne?boardId=BBS_0000282&menuCd=DOM_000000102006001000&contentsSid=252&cpath='
response = urlopen(url)
soup = BeautifulSoup(response,'html.parser')
cn_sub_list =[]
cn_ref_list = []
for i in soup.select("td.subjectEtc"):
    sub= i.a.get('title','/')
    ref = i.find("a")["href"]
    ref1 = "http://www.jne.go.kr/" + ref
    cn_sub_list.append(str(sub))
    cn_ref_list.append(ref1)

print(cn_ref_list)