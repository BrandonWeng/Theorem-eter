import constants as const
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
    result  = scan_file(filename=file_src, language=const.lang)
    test_file = json.loads(result)
    print(test_file)
    text = (test_file[const.res][0][const.text])
    print(text)
    return text




