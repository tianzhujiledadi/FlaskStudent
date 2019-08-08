from flask_wtf import Form#定义表单单的父类
import wtforms#wtfforms  #定义字段
from wtforms import  validators#validators验证器validators验证器validators验证器validators
from student.models import Course
course_list=[(c.id,c.label) for  c in Course.query.all()]
class TeacherForm(Form):
    name=wtforms.StringField("教师姓名",
                              render_kw={
                                  "class":"form-control",
                                  "placeholder":"教师姓名"
                              },
                              validators={
                                  validators.DataRequired("姓名不可以")
                              })
    age=wtforms.IntegerField("教师年龄",
                             render_kw={#固定语法render_kw;render_kw;render_kw;render_kw
                                 "class":"form-control",#CSS样式
                                 "placeholder":"教师年龄",#占位符placeholder;placeholder;placeholder
                             },
                             validators=[#validators验证器，validators
                                 validators.DataRequired("年龄不可以为空")
                             ])#required必须的required;required;data数据data;
    gender = wtforms.SelectField("教师性别",
        choices=[('0','男'),('1','女'),('2','其他')],#这里必需是字符串类型1
        render_kw={
            "class":"form-control",
        })

    course=wtforms.SelectField(#选择框
        "学科",
        choices=course_list,
        render_kw={
            "class":"form-control",
        }
    )
    """
    form 字段的参数
    label=None,表单的标签
    validators=None,校验，传入校验的方法
    filter=tuple(),过滤
    description='',描述
    id=None,html  id
    default=None,默认值
    widget=None,
    render_kw=None,
    """

