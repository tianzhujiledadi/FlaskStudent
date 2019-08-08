# import os
#
# DEBUG=True
# BASE_DIR=os.path.abspath(os.path.dirname(__file__))#路径
# SQLALCHEMY_DATABASE_URI="sqlite:///"+os.path.join(BASE_DIR, "student/Demo.sqlite")
# #app.config["SQLALCHEMY_DATABASE_URI"]="mysql+pymysql://root:root@127.0.0.1:3306/student"+os.path.join(BASE_DIR,"MySQL")
# #app.config["SQLALCHEMY_DATABASE_URI"]="mysql+pymysql://root:root@127.0.0.1:3306/student"
#
# #URI统一资源匹配符；配置数据连接的参数#app.config返回类字典对象，里面用来存放当前app的配置
# SQLALCHEMY_COMMIT_TEARDOWN=True
# #sqlalchemy  commit  teardown请求结束后自动提交数据库修改
# SQLALCHEMY_TRACK_MODIFICATIONS=True