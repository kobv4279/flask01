# conda python=3.6.9

import math

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
# app.config["MONGO_URI"]= "mongodb://localhost:27017/hire"
# mongo = PyMongo(app)

kj_sub_list,kj_ref_list = crawring.kj()
cn_sub_list = crawring.cn()
chonbook_sub_list = crawring.chonbook()
dj_sub_list = crawring.dj()



#
#
# #이 패키지에 귀속이 되게 함 board와 memeber를 가져오는 방법
# from .common import login_required, allowed_file, rand_generator
# from .filter import format_datetime
# from . import board
# from . import member


#
# #.common의.은 현재 경로라는 뜻임
#
# app.register_blueprint(board.blueprint)
# app.register_blueprint(member.blueprint)
#
from .crawring import *
from .test_daejoun import *
from . import crawring
from . import test_daejoun