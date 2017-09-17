import pickle
from Schema.DAO import uWaterlooMath136FileNamesDAO
from probCalculation import the_def_score_pairs
from Schema.DAO import uWaterlooMath136ScoreDAO

sessionFileName = uWaterlooMath136FileNamesDAO.uWaterlooMath136FileNamesDAO()
sessionScore = uWaterlooMath136ScoreDAO.uWaterlooMath136ScoreDAO()
fileScorePair = the_def_score_pairs.the_def_score_paris

with open("../pickles/KeyToFileNames", 'rb') as loadKeyToFileDict:
    d = pickle.load(loadKeyToFileDict);
    for key,value in d.items():
        files = []

        for each in value:
            files.append(each.split(".")[0])

        sessionFileName.insert(key, ",".join(files))

#
# for key,value in fileScorePair.items():
#     sessionScore.insert(key,value)