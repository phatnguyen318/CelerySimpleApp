# This is simple Celery app calculating area and perimeter of rectangle and insert it into Database.

### Run the requirement installation for virtualenv:
pip install -r requirements.txt

### This project using Celery, Flask, Sqlalchemy, and rabbitmq as broker, Sqlite3 for database.

### Download and Run Rabbitmq using docker:
docker run -it --rm --name rabbitmq -p 5672:5672 -p 15672:15672 rabbitmq:3.10-management


### Run celery:
celery -A celery_app.celery worker --loglevel=info

