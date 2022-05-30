from flask import Flask
from flask_celery import make_celery
from flask_sqlalchemy import SQLAlchemy
from random import randint 



app = Flask(__name__)
app.config['CELERY_BROKER_URL'] = 'amqp://localhost//'
app.config['CELERY_BACKEND'] = 'db+sqlite:///db.sqlite3'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite3'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


celery = make_celery(app)
db = SQLAlchemy(app)

class Results(db.Model):
    rec_id = db.Column('id', db.Integer, primary_key=True)
    a = db.Column('a', db.Integer)
    b = db.Column('b', db.Integer)
    area = db.Column('area', db.Integer)
    perimeter = db.Column('perimeter', db.Integer)
    
    


@app.route('/insertData')
def insertData():
    insert.delay()
    return 'I sent an async request to insert data into database'


"""@celery.task(name='celery_app.cal_area')
def cal_area():
    return area()"""

@app.route('/calculate_area')
def calculate_area():
    cal_area.delay()
    return 'I sent an async request to calculate area of the rectangle'

@app.route('/calculate_perimeter')
def calculate_perimeter():
    cal_perimeter.delay()
    return 'I sent an async request to calculate perimeter of the rectangle'




@celery.task(name='celery_app.insert') 
def insert():
    for i in range(50):
        a = randint(1,50)
        result = Results(a=a)
        b = randint(1,50)
        result2 = Results(b=b)
        db.session.add(result)
        db.session.add(result2)
        
    db.session.commit()
    
@celery.task(name='celery_app.cal_area')
def cal_area():
    for a, b in range(id):
        dientich = a*b
        result = Results(area=dientich)
        db.session.add(result)
    db.session.commit()
        

@celery.task(name='celery_app.cal_perimeter')
def cal_perimeter():
    for a, b in range(id):
        chuvi = (a+b)*2
        result = Results(perimeter=chuvi)
        db.session.add(result)
    db.session.commit()
    


if __name__ == '__main__':
    app.run(debug=True)