from urllib.request import urlopen

import requests
from bs4 import BeautifulSoup

def kj():
    req = requests.get('http://www.gen.go.kr/xboard/board.php?mode=list&tbnum=32&addUrlQuery=&sCat=')
    soup = BeautifulSoup(req.text,'html.parser')
    title = soup.findAll('td', attrs={'class': 'left subject'})

    kj_sub_list = []
    kj_ref_list = []
    for i in title:

        sub = i.a.text
        # print(type(sub))
        kj_sub_list.append(str(sub))

        ref = str("http://www.gen.go.kr/xboard/" + i.a['href'])
        kj_ref_list.append(str(ref))

    return kj_sub_list

    #     ref = i.find("a")["href"]
    #     ref1 = "http://www.gen.go.kr/xboard/" + ref
    #     kj_ref_list.append(str(ref1))
    #
    # return kj_sub_list, kj_ref_list


def cn():
    url = 'http://www.jne.go.kr/board/list.jne?boardId=BBS_0000282&menuCd=DOM_000000102006001000&contentsSid=252&cpath='
    response = urlopen(url)
    soup = BeautifulSoup(response,'html.parser')
    cn_sub_list =[]

    cn_ref_list = []

    for i in soup.select("td.subjectEtc"):
        sub= i.a.get('title','/')

        cn_sub_list.append(str(sub))

        print(cn_sub_list)



    return cn_sub_list

chonbook_sub_list = []
def chonbook():
    req = requests.get('http://pool.jbe.go.kr/main/program.action?cmsid=110020100000')
    soup = BeautifulSoup(req.text,'html.parser')

    html1 = soup.select('td.td.mo_tit')
    for i in html1:
        chonbook_sub_list.append(i.text)
    return chonbook_sub_list


