from __future__ import print_function
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from config import cockroach_config
from Schema import uWaterlooMath136Score
from sqlalchemy import text


class uWaterlooMath136ScoreDAO(object):
    def __init__(self):
        self.Base = declarative_base()
        self.engine = create_engine(cockroach_config.SQLALCHEMY_DATABASE_URI)
        self.Session = sessionmaker(bind=self.engine)
        self.Base.metadata.create_all(self.engine)
        self.session = self.Session()
        self.schema = uWaterlooMath136Score

    def insert(self, fileNames, score):
        newKeyWord = self.schema.uWaterlooMath136Score(fileNames, score)
        self.session.add(newKeyWord)
        self.session.commit()

    def query(self, textQuery, param={}):
        result = self.session.execute(text(textQuery), param)
        return result

    def closestScores(self,score):
        result = self.session.execute("SELECT filename FROM textbooks.uwaterloomath136score ORDER BY abs(:score - score) ASC LIMIT 5;",{"score":score})
        return result

if __name__ == "__main__":
    math136ScoreDAO = uWaterlooMath136ScoreDAO()

    math136ScoreDAO.query("INSERT INTO textbooks.uwaterloomath136score VALUES ('uWaterlooMath136_2',12), ('uWaterlooMath136_4',99);")

    for keyword in math136ScoreDAO.query("SELECT * from textbooks.uwaterloomath136score;"):
        print(keyword.filename, keyword.score)
    print("-------------------")

    math136ScoreDAO.insert("TEST", 21)

    for keyword in math136ScoreDAO.query("SELECT * from textbooks.uwaterloomath136score;"):
        print(keyword.filename, keyword.score)
