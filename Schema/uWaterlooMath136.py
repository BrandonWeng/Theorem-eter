from __future__ import print_function
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base


#T The uWaterlooMath136 table in textbooks
class uWaterlooMath136(declarative_base()):
    __tablename__ = 'uwaterloomath136'

    keyWord = Column(String, primary_key=True)
    fileNames = Column(String)
    score = Column(Integer)

    def __init__(self, keyWord, fileNames, score):
        self.keyWord = keyWord
        self.fileNames = fileNames
        self.score = score
