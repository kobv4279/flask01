#!/usr/bin/python
# -*- coding: utf-8 -*-

#conda python3.6.9
import requests
from bs4 import BeautifulSoup
from pymongo import MongoClient
from flask_pymongo import PyMongo
from datetime import datetime
import random
from flask import app
from flask import request, render_template, redirect, url_for

client = MongoClient(host="localhost",port=27017)
db = client.hire
col = db.memotable



mongo = PyMongo(app)

@app.route("/write", methods=["GET","POST"])
def board_write():
    if request.method == "POST":
        name =  request.form.get("name")
        title = request.form.get("title")
        contents = request.form.get("contents")
        print(name, title, contents)

        current_utc_time = round(datetime.utcnow().timestamp()*1000)
        #utc는 ms로 반환하므로 1000을 곱한후 소수점을 없애기위해 반올림 round함수로
        #utc는 협정세계표준시
        #mongo라는 db에 board라는 컬렉션(db이름)을 board라는 객체에 집어넣음
        board = mongo.db.board
        post = {
            "name":name,
            "title":title,
            "contents":contents,
            "pubdate":current_utc_time,
            "view":0,
        }

        x = board.insert_one(post)
        print(x.inserted_id)
        return redirect(url_for("board_view", idx= x.inserted_id))
    else:
        return render_template("write.html")


    for l in lists:
        current_utc_time = round(datetime.utcnow().timestamp()*1000)

        try:
            title = l.select_one("h3.LC20lb.DKV0Md").text
            contents = l.select_one("div.s").text
            col.insert_one({
                "name":"테스트",
                "title":title,
                "contents":contents,
                "view":0,
                "pubdate":current_utc_time
            })
        except:
            pass
