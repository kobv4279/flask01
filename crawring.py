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

        kj_sub_list.append(str(sub))
        ref = i.find("a")["href"]

        ref_= "http://www.gen.go.kr/xboard/" + ref
        #print(ref_)
        kj_ref_list.append(ref_)

   # http: // www.gen.go.kr / xboard / board.php?mode = view & number = 378639 & tbnum = 32 & sCat = 0 & page = 1 & keyset = & searchword =

    return kj_sub_list, kj_ref_list

def cn():
    url = 'https://www.jne.go.kr/main/na/ntt/selectNttList.do?mi=265&bbsId=117'
    response = urlopen(url)
    soup = BeautifulSoup(response,'html.parser')
    cn_sub_list =[]
    for i in soup.select("td.al"):
        sub= i.a.get('title','/')

        cn_sub_list.append(str(sub))
        print(cn_sub_list)
    return cn_sub_list

chonbook_sub_list = []
def chonbook():

    # req = requests.get('http://pool.jbe.go.kr/main/program.action?cmsid=110020100000')
    # soup = BeautifulSoup(req.text,'html.parser')
    #
    # html1 = soup.select('td.td.mo_tit')
    # for i in html1:
    #     chonbook_sub_list.append(i.text)
    # return chonbook_sub_list


    req = requests.get('https://www.jbe.go.kr/pool/board/list.jbe?boardId=BBS_0000053&menuCd=DOM_000001802001000000&contentsSid=991&cpath=%2Fpool')
    soup = BeautifulSoup(req.text,'html.parser')

    html1 = soup.select('td.td.title')
    for i in html1:
        chonbook_sub_list.append(i.text)
    return chonbook_sub_list


dj_sub_list=[]
def dj():
    #https://www.dje.go.kr/boardCnts/list.do?boardID=54&m=031001&s=dje
    url = "https://www.dje.go.kr/boardCnts/list.do?boardID=54&m=031001&s=dje"
    r = requests.get(url)
    bs = BeautifulSoup(r.text, "html.parser")
    lists = bs.select("td.link")

    for i in lists:
        print(i.a.text)
        dj_sub_list.append(i.a.text)

    return dj_sub_list

