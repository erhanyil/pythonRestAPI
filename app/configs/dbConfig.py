from app import app
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.ext.declarative import declarative_base

# region Connection String

Base = declarative_base()
db = SQLAlchemy(app)

# app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://username:password@localhost/db_name'
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://stdiosoft:XYkm50O5@94.73.151.138/stdiosoft'

db.create_all()
# endregion
