from student.main import models
db=models.session()
class  BaseModel(models.Model):#学员表
    __abstract__=True#抽象表为True,代表当前类为抽象类，不会被实例化
    id=models.Column(models.Integer,primary_key=True,autoincrement=True)
    def  save(self):
        db.add(self)
        db.commit()
    def  delete_obj(self):#魔术方法
        db.delete(self)
        db.commit()
class  Students(BaseModel):#学员表
    __tablename="students"
    name=models.Column(models.String(32))
    age=models.Column(models.Integer)
    gender=models.Column(models.Integer)#0,男；1女；2其他
Stu_Cou=models.Table(#中间关系表#多对多
    "stu_cou",
    models.Column("id",models.Integer,primary_key=True,autoincrement=True),
    models.Column("course_id",models.Integer, models.ForeignKey("course.id")),
    models.Column("students_id",models.Integer, models.ForeignKey("students.id")))
#flask-sqlalchemy数据库多对多映射表不可以是class类定义表，只能是Table设置的虚表

class  Course(BaseModel):#课程表
    __tablename = "course"
    label = models.Column(models.String(32))
    description=models.Column(models.Text)
    #双向映射
    to_teachers=models.relationship(#relationship关联关系relationship
        'Teachers',#映射类的名称和类名一致#双向映射
        backref='to_course'
    )
    #教师类映射到该表
    #双向映射语法(一对多)：字段名=models.relationship(
        #"映射的类名"，
        #backref="本表名")
    to_student=models.relationship(
        "Students",
        secondary=Stu_Cou,#多对多关系表
        backref=models.backref("to_course",lazy="dynamic"),
        lazy="dynamic"
    )
    #models.relationship当前字段用于一对多或者多对多反向映射
    #第一个参数是映射向的模型名称
    #secondary参数,指向多对多的关系表
    #backref参数指向反向映射字段，反向映射表通过该字段查询当前表内容
    #models.relationship当前字段用于一对多或者多对多反向映射
    #lazy #select访问该字段时候，加载所有的映射数据
    #joined 对关联的两个表students和stu_cou进行join查询
    #dynamic 不加载数据

class  Grade(BaseModel):#成绩表，课程、学员关联此表
    __tablename = "grade"
    grade=models.Column(models.Float)
    course_id=models.Column(models.Integer,models.ForeignKey("course.id"))
    student_id = models.Column(models.Integer, models.ForeignKey("students.id"))
class  Attendance(BaseModel):#考勤表 关联学员
    __tablename = "attendance"
    student_id = models.Column(models.Integer, models.ForeignKey("students.id"))
    att_time=models.Column(models.Date)
    status = models.Column(models.Integer,default=1)#0迟到；1正常出勤；2早退；3请假；4旷课
class  Teachers(BaseModel):#教师表
    __tablename = "teachers"
    name = models.Column(models.String(32))
    age = models.Column(models.Integer)
    gender = models.Column(models.Integer)  # 0,男；1女；2其他
    course_id = models.Column(models.Integer, models.ForeignKey("course.id"))
class  User(BaseModel):
    __tablename="user"
    username=models.Column(models.String(32))
    password=models.Column(models.String(32))
    identity=models.Column(models.Integer)#0学员；1老师
    identity_id=models.Column(models.Integer,nullable=True)


