from flask import render_template, redirect  # redirect重定向
from student.main import app, session
from student.models import Students, Course, Teachers, User
from flask import request, jsonify
import hashlib
from student.forms import TeacherForm
from student.main import csrf


# @app.route('/student/',methods=["GET","POST"])#前后台必须加斜杠
@app.route('/loginvalid/')
def loginValid(fun):
    def inner(*args, **kwargs):
        username = request.cookies.get("user_name")
        session_name = session.get("username")
        if username and session_name and session_name == spw(username):
            user = User.query.filter_by(username=username).first()
            if user:
                return fun(*args, **kwargs)
        return redirect("/login/")

    return inner

@app.route('/student/')
def student():
    print("函数调用成功")
    student_list = Students.query.all()
    return render_template("student.html", **locals())
    return render_template("student.html", student_list=student_list)

@app.route('/add/')
def add():
    course = Course()
    course.label = "python"
    course.description = "python是最好的语言"
    course.save()
    teacher = Teachers()
    teacher.name = "lys"
    teacher.age = "18"
    teacher.gender = 0
    teacher.course_id = 1
    teacher.save()


@app.route('/register/', methods=["GET", "POST"])
def register():  # 已经导入request包不用再在参数里添加
    if request.method == "POST":
        form_data = request.form
        username = form_data.get("username")
        password = form_data.get("password")
        identity = form_data.get("identity")
        user = User()
        user.username = username
        user.password = spw(password)
        user.identity = identity
        user.save()
        return redirect('/login/')
    return render_template('register.html', **locals())
@csrf.exempt#exempt免除、豁免exempt,exempt #免除单个视图的csrf校验
@app.route('/login/', methods=["GET", "POST"])
def login():
    if request.method == "POST":
        form_data = request.form
        username = form_data.get("username")
        password = form_data.get("password")
        user = User.query.filter_by(username=username).first()
        if spw(password) == user.password:
            response = redirect('/index/')
            response.set_cookie("user_name", str(username))
            session["username"] = spw(username)
            return response
    return render_template('login.html', **locals())
def spw(password):
    md5 = hashlib.md5()
    md5.update(password.encode())
    return md5.hexdigest()  # 返回加密的密码
@app.route('/index/', methods=["GET", "POST"])
@loginValid
def index():
    return render_template('index.html', **locals())
@app.route('/logout/', methods=["GET", "POST"])
def logout():
    response = redirect("/login/")
    for key in request.cookies:
        response.delete_cookie(key)
        print(key)
    del session["username"]
    return response

@csrf.exempt
@app.route("/add_teacher", methods=["GET", "POST"])
def add_teacher():
    teacherForm = TeacherForm()
    if request.method == "POST":
        name = request.form.get("name")
        age = request.form.get("age")
        gender = request.form.get("gender")
        print(name, age, gender)
        teacher = Teachers()  # 增加数据
        teacher.name = name
        teacher.age = int(age)
        teacher.gender = int(gender)
        # teacher.course_id =1
        teacher.save()
        teacher = Teachers.query.filter_by(name=name).first()
        print(teacher)
    return render_template("add_teacher.html", **locals())
@app.route("/userValid/",methods=["GET","POST"])
def UserValid():
    result = {
        "code": "",
        "data": ""
    }
    if request.method=="POST":
        #data = request.args.get("username")#get获取参数方法
        data=request.form.get("username")#post获取参数方法
        if data:
            user = User.query.filter_by(username=data).first()
            if user:
                result["code"] = 400
                result["data"] = "用户名已经存在"
            else:
                result["code"] = 200
                result["data"] = "用户名未被注册，可以使用"
    else:
        result["code"] = 400
        result["data"] = "请求方法错误"
    return jsonify(result)
