import pickle
from Schema.DAO import uWaterlooMath136FileNamesDAO

session = uWaterlooMath136FileNamesDAO.uWaterlooMath136FileNamesDAO()

with open("../pickles/KeyToFileNames", 'rb') as loadKeyToFileDict:
    d = pickle.load(loadKeyToFileDict);
    for key,value in d.items():
        session.insert(key, ",".join(value))




