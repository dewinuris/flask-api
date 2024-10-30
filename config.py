from flask_sqlalchemy import flask_sqlalchemy
from flask import flask

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://pwl:pwl123@localhost/db_flask_api'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']= flask_sqlalchemy


db = SQLAlchemy(app)


app.app_context().push()