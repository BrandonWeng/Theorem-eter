from __future__ import print_function
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from config import cockroach_config
from Schema import uWaterlooMath136FileNames
from sqlalchemy import text


class uWaterlooMath136FileNamesDAO(object):
    def __init__(self):
        self.Base = declarative_base()
        self.engine = create_engine(cockroach_config.SQLALCHEMY_DATABASE_URI)
        self.Session = sessionmaker(bind=self.engine)
        self.Base.metadata.create_all(self.engine)
        self.session = self.Session()
        self.schema = uWaterlooMath136FileNames

    def insert(self, keyWord, fileNames):
        newKeyWord = self.schema.uWaterlooMath136FileNames(keyWord, fileNames)
        self.session.add(newKeyWord)
        self.session.commit()

    def query(self, textQuery, param={}):
        result = self.session.execute(textQuery, param)
        return result

    def getFilenames(self, keyword):
        result = self.session.execute("SELECT filenames FROM textbooks.uwaterloomath136filenames where keyword=:param;", {"param":keyword})
        for first in result:
            return first.filenames



if __name__ == "__main__":
    math136FileNameDAO = uWaterlooMath136FileNamesDAO()
    print(math136FileNameDAO.getFilenames("basis"))

    # math136FileNameDAO.query("INSERT INTO textbooks.uwaterloomath136filenames VALUES ('basis', 'uWaterlooMath136_1,uWaterlooMath136_2'), ('angular', 'uWaterlooMath136_3,uWaterlooMath136_4');")
    # for keyword in math136FileNameDAO.query("SELECT * from textbooks.uwaterloomath136filenames;"):
    #     print(keyword.keyword, keyword.filenames)
    # print("-------------------")
    #
    # math136FileNameDAO.insert("TEST","TEST2,TEST3,TEST4")
    #
    # for keyword in math136FileNameDAO.query("SELECT * from textbooks.uwaterloomath136filenames;"):
    #     print(keyword.keyword, keyword.filenames)
