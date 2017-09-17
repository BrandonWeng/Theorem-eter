from __future__ import print_function
from sqlalchemy import create_engine, Column, Integer
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from config import cockroach_config
from Schema import uWaterlooMath136
from sqlalchemy import text


class uWaterlooMath136DAO(object):
    def __init__(self):
        self.Base = declarative_base()
        self.engine = create_engine(cockroach_config.SQLALCHEMY_DATABASE_URI)
        self.Session = sessionmaker(bind=self.engine)
        self.Base.metadata.create_all(self.engine)
        self.session = self.Session()
        self.schema = uWaterlooMath136

    def insert(self, keyWord, fileNames, score):
        newKeyWord = self.schema.uWaterlooMath136(keyWord, fileNames, score)
        self.session.add(newKeyWord)
        self.session.commit()

    def query(self, textQuery, param={}):
        result = self.session.execute(text(textQuery), param)
        return result


if __name__ == "__main__":
    math136DAO = uWaterlooMath136DAO()
    #math136DAO.query("DROP TABLE textbooks.uwaterloomath136")
    math136DAO.query("CREATE TABLE textbooks.uwaterloomath136 (keyWord STRING, fileNames STRING, score INTEGER);")
    math136DAO.query("INSERT INTO textbooks.uwaterloomath136 VALUES ('basis', 'uWaterlooMath136_1,uWaterlooMath136_2',12), ('angular', 'uWaterlooMath136_3,uWaterlooMath136_4',99);")

    for keyword in math136DAO.query("SELECT * from textbooks.uwaterloomath136;"):
        print(keyword.keyword, keyword.filenames, keyword.score)
    print("-------------------")

    math136DAO.insert("TEST","TEST2,TEST3,TEST4", 21)

    for keyword in math136DAO.query("SELECT * from textbooks.uwaterloomath136;"):
        print(keyword.keyword, keyword.filenames, keyword.score)
