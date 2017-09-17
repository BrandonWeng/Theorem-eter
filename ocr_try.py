import ocr_const as const
import requests
import json

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
    result= scan_file(filename=file_src, language=const.lang)
    test_file = json.loads(result)
    text = test_file[const.res][0][const.text].split()
    print(text)
    print(test_file[const.res][0][const.text])
    #print(json.dumps(test_file, indent=4, sort_keys=True))
    return text




