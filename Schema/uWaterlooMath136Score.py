from __future__ import print_function
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base


#T The uWaterlooMath136 table in textbooks
class uWaterlooMath136Score(declarative_base()):
    __tablename__ = 'uwaterloomath136score'

    fileName = Column(String, primary_key=True)
    score = Column(Integer)

    def __init__(self, fileName, score):
        self.fileName = fileName
        self.score = score
