#python 3.8.2
from flask import Flask, render_template,request, url_for
from flask import render_template
from flask_pymongo import PyMongo
from datetime import datetime
from bson.objectid import ObjectId
from flask import abort
from flask import redirect
from flask import url_for
import time
import crawring


app = Flask(__name__)
ip='0.0.0.0'
app.config["MONGO_URI"]= "mongodb://localhost:27017/hire"
mongo = PyMongo(app)

kj_sub_list,kj_ref_list = crawring.kj()
cn_sub_list = crawring.cn()
chonbook_sub_list = crawring.chonbook()
dj_sub_list = crawring.dj()

#utc 시간을 현재 시간에 맞게 구현하기
@app.template_filter("formatdatetime")
def format_datetime(value):
    if value is None:
        return ""

    now_timestamp = time.time()
    offset = datetime.fromtimestamp(now_timestamp) - datetime.utcfromtimestamp(now_timestamp)
    #시간차이 = datetime형 현재시간 - datetime형 utc 시간
    #현재 타임기준으로 datetime 객체 만듬
    value = datetime.fromtimestamp((int(value) / 1000)) + offset
    return value.strftime('%Y-%m-%d %H:%M:%S')

#
# @app.route("/list")
# def lists():
#     board = mongo.db.board
#     datas = board.find({})
#     return render_template("list.html", datas = datas)
#

@app.route("/view/<idx>")
def board_view(idx):
    #idx = request.args.get("idx")
    #idx는 몽고디비의 id값이다 이것을 get방식으로 바다서
    if idx is not None:
        board = mongo.db.board
        data = board.find_one({"_id":ObjectId(idx)})    #id값이 idx인것을 찾아서 data에 넣겠다

        if data is not None:
            result = {
                "id":data.get("_id"),
                "name":data.get("name"),
                "contents":data.get("contents"),
                "pubdate":data.get("pubdate"),
                "view":data.get("view")
            }
            #이 데이타를 html로 표기해주어야 한다
            return render_template("view.html",result=result)

    return abort(404)

    #request method가 POST인경우 form에서 얻어옴 -url상 노출 안됨
    #request method가 GET 인경우 form에서 얻오울수없다 -url상 노출


@app.route("/write", methods=["GET","POST"])
def board_write():
    if request.method == "POST":
        name = request.form.get("name")
        contents = request.form.get("contents")
        print(name, contents)

        current_utc_time = round(datetime.utcnow().timestamp()*1000)
        #utc는 ms로 반환하므로 1000을 곱한후 소수점을 없애기위해 반올림 round함수로
        #utc는 협정세계표준시
        #mongo라는 db에 board라는 컬렉션(db이름)을 board라는 객체에 집어넣음
        board = mongo.db.board
        post = {
            "name":name,
            "contents":contents,
            "pubdate":current_utc_time,
            "view":0,
        }

        x = board.insert_one(post)
        print(x.inserted_id)
        return redirect(url_for("board_view", idx= x.inserted_id))
    else:
        return render_template("index.html")


@app.route('/')

def hello():
    return render_template('index.html',
                           title='깜슈니',
                           sub = kj_sub_list,
                           ref= kj_ref_list,
                           ref_len=len(kj_ref_list))
    print(ref)
@app.route('/about')
def about():
    return 'about page'

@app.route('/cn',methods = ['POST', 'GET'])
def result1():
   if request.method == 'POST':
      result = request.form

      return render_template("cn.html", result=result,
                             sub = cn_sub_list)

@app.route('/kj',methods = ['POST'])
def kj_():
   if request.method == 'POST':
      result = request.form

      return render_template("kj.html", result=result,
                             sub = kj_sub_list,
                             ref= kj_sub_list,
                             ref_len=len(kj_ref_list))


@app.route('/chonbook.html',methods = ['POST', 'GET'])
def result3():
   if request.method == 'POST':
      result = request.form

      return render_template("chonbook.html", result=result,
                             sub = chonbook_sub_list)


@app.route('/dj.html',methods = ['POST', 'GET'])
def result_dj():
   if request.method == 'POST':
      result = request.form

      return render_template("dj.html", result=result,
                             sub = dj_sub_list)


if __name__ == '__main__':
    app.debug = True
    app.run(host="0.0.0.0")
    #app.run(debug=True)