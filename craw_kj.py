from urllib.request import urlopen

import requests
from bs4 import BeautifulSoup


req = requests.get('http://www.gen.go.kr/xboard/board.php?mode=list&tbnum=32&addUrlQuery=&sCat=')

soup = BeautifulSoup(req.text,'html.parser')
title = soup.findAll('td', attrs={'class': 'left subject'})

kj_sub_list = []
kj_ref_list = []
for i in title:

    sub = i.a.text
    # print(type(sub))
    kj_sub_list.append(str(sub))
    ref = i.find("a")["href"]
    print("http://www.gen.go.kr" + i.find("a")["href"])

#
# http://www.jn/html/body/div[2]/div[2]/div[2]/div[2]/div/div[2]/div[2]/table/tbody/tr[2]/td[2]/ae.go.kr/board/list.jne?boardId=BBS_0000282&menuCd=DOM_000000102006001000&contentsSid=252&cpath=
# <a href="/board/view.jne?boardId=BBS_0000282&amp;menuCd=DOM_000000102006001000&amp;orderBy=REGISTER_DATE DESC&amp;startPage=1&amp;dataSid=1867837" title="무안초등학교 기간제교사 채용 공고" class="">무안초등학교 기간제교사 채용 공고</a>