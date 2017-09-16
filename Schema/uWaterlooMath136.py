from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import sqlalchemy.orm

app = Flask(__name__)
app.config.from_pyfile('../config/cockroach_config.py')
db = SQLAlchemy(app)
sessionMaker = sqlalchemy.orm.sessionmaker(db.engine)


class uWaterlooMath136(db.Model):
    __tablename__ = 'uWaterlooMath136'
    id = db.Column('keyword_id', db.Integer, primary_key=True)
    keyWord = db.column(db.String())
    fileNames = db.column(db.String())

    def __init__(self, keyWord, fileNames):
        self.keyWord = keyWord
        self.fileNames = fileNames



