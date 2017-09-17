from __future__ import print_function
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base


#T The uWaterlooMath136 table in textbooks
class uWaterlooMath136FileNames(declarative_base()):
    __tablename__ = 'uwaterloomath136filenames'

    keyWord = Column(String, primary_key=True)
    fileNames = Column(String)

    def __init__(self, keyWord, fileNames):
        self.keyWord = keyWord
        self.fileNames = fileNames
