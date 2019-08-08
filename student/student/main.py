import pymysql
from  flask import Flask
import  os
from flask import session
from flask_sqlalchemy import SQLAlchemy
from flask_wtf.csrf import CSRFProtect#CsrfProtrct在1.0之后移除
app=Flask(__name__)#__name__当前文件
csrf=CSRFProtect(app)
# BASE_DIR=os.path.abspath(os.path.dirname(__file__))#路径
# app.config['SQLALCHEMY_DATABASE_URI']="sqlite:///"+os.path.join(BASE_DIR,"Demo.sqlite")
# #app.config["SQLALCHEMY_DATABASE_URI"]="mysql+pymysql://root:root@127.0.0.1:3306/student"+os.path.join(BASE_DIR,"MySQL")
# #app.config["SQLALCHEMY_DATABASE_URI"]="mysql+pymysql://root:root@127.0.0.1:3306/student"
#
# #URI统一资源匹配符；配置数据连接的参数#app.config返回类字典对象，里面用来存放当前app的配置
# app.config["SQLALCHEMY_COMMIT_TEARDOWN"]=True
# #sqlalchemy  commit  teardown请求结束后自动提交数据库修改
# app.config["SQLALCHEMY_TRACK_MODIFICATIONS"]=True
#如果设置成True(默认情况),flask_SQLALchemy 将会追踪对象的修改并且发送信号
#app.config["SECRET"]="123456"
#app.config.from_pyfile("settings.py")#from_pyfile调用文件
app.config.from_object("config.DebugConfig")#调用config文件中的DebugConfig函数
models=SQLAlchemy(app)#关联sqlalchemy和flask应用
