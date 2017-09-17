import ocr_const as const
import requests
import json
import pickle
from Schema.DAO import uWaterlooMath136FileNamesDAO
from Schema.DAO import uWaterlooMath136ScoreDAO
from probCalculation.wrapper import return_score

def scan_file(filename, overlay=False, api_key=const.api_key, language=const.lang):
    payload = {'isOverlayRequired': overlay,
               'apikey': api_key,
               'language': language,
               }
    with open(filename, 'rb') as f:
        r = requests.post(const.parse_link,
                          files={filename: f},
                          data=payload,
                          )
    return r.content.decode()

def process_print(file_src):
    print(file_src)
    result = scan_file(filename=file_src, language=const.lang)
    print(result)

    test_file = json.loads(result)
    print(test_file)

    text = (test_file[const.res][0][const.text])
    text = text.split()
    return text

def getEverting(imagePath):

    sessionFileName = uWaterlooMath136FileNamesDAO.uWaterlooMath136FileNamesDAO()
    sessionScore = uWaterlooMath136ScoreDAO.uWaterlooMath136ScoreDAO()

    words = process_print(imagePath)
    index = []

    #load list of keywords
    with open("pickles/listOfKeys", 'rb') as loadKeyWords:
        index = pickle.load(loadKeyWords)

    keyWords = [word for word in words if word in index]
    keyWordsToFileNames = {}

    for word in keyWords:
        filenames = sessionFileName.getFilenames(word)
        keyWordsToFileNames[word] = filenames

    score = return_score(imagePath)
    suggested = []

    fiveSuggested = sessionScore.closestScores(score)
    for each in fiveSuggested:
        suggested.append(each.filename)

    keyWordsToFileNames["suggested"] = ",".join(suggested)

    return keyWordsToFileNames


