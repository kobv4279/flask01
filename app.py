#python 3.8.2

from flask import Flask, render_template,request, url_for
import crawring


app = Flask(__name__)
ip='0.0.0.0'

kj_sub_list,kj_ref_list = crawring.kj()
cn_sub_list = crawring.cn()
chonbook_sub_list = crawring.chonbook()
dj_sub_list = crawring.dj()
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