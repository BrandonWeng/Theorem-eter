import ocr_const as const
import requests
import json
import pickle
from Schema.DAO import uWaterlooMath136FileNamesDAO

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

def process_print(file_src, fileName):
    result = scan_file(filename=file_src, language=const.lang)
    test_file = json.loads(result)
    text = (test_file[const.res][0][const.text])
    text = text.split()
    return text

def getEverting(imagePath):

    session = uWaterlooMath136FileNamesDAO.uWaterlooMath136FileNamesDAO()

    words = process_print(imagePath)
    index = []

    #load list of keywords
    with open ("pickles/listOfKeys", 'rb') as loadKeyWords:
        index = pickle.load(loadKeyWords)

    keyWords = [word for word in words if word in index]
    keyWordsToFileNames = {}

    for word in keyWords:
        filenames = session.getFilenames(word)
        keyWordsToFileNames[word] = filenames

    return keyWordsToFileNames
    #if len(keyWords) == 0




