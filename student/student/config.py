import os
BASE_DIR = os.path.abspath(os.path.dirname(__file__))  # 路径
class BaseConfig(object):
    #object是python中所有类的父类，默认可以不写
    # URI统一资源匹配符；配置数据连接的参数#app.config返回类字典对象，里面用来存放当前app的配置
    SQLALCHEMY_COMMIT_ON_TEARDOWN = True
    # sqlalchemy  commit  teardown请求结束后自动提交数据库修改
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    SECRET_KEY="123456"#涉及到加盐算法secret秘密，机密
class DebugConfig(BaseConfig):#debug调试模式
    DEBUG=True
    #SQLALCHEMY_DATABASE_URI="sqlite:///"+os.path.join(BASE_DIR,"Demo.sqlite")
    SQLALCHEMY_DATABASE_URI="mysql+pymysql://root:root@127.0.0.1:3306/student"
class OnlineConfig(BaseConfig):#online上线模式
    DEBUG=False
    SQLALCHEMY_DATABASE_URI="sqlite:///"+os.path.join(BASE_DIR,"Demo.sqlite")
