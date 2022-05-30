from flask import Flask
from flask_celery import make_celery
from flask_sqlalchemy import SQLAlchemy
from random import randint, random 



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

"""@app.route('/calculatearea')
def calarea():
    return area()"""

"""def area():
    for i in range(7):
        a = Results.query.filter_by(a).first()
        b = Results.query.filter_by(b).first()
        dientich = a * b
        result = Results(area=dientich)
        db.session.add(result)
    db.session.commit()
    return 'Done cal area'"""

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
    


if __name__ == '__main__':
    app.run(debug=True)