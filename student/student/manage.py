#manage.py调动main.py
from student.views import app
from student.models import models
if __name__ == '__main__':
    models.create_all()
    app.run()
    #app.run(host="0.0.0.0",post=8000,debug=True)