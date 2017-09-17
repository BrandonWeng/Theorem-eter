import ocr_const as const
import requests
import json
import pickle

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
    result = scan_file(filename=file_src, language=const.lang)

    test_file = json.loads(result)

    text = (test_file[const.res][0][const.text]);
    print(text);

process_print("theorems/theoremBody" + str(3) + ".jpg");

# for i in range(1, 96):
#     print("Theorem" + str(i));
    #theoremBody22.jpg
    # process_print("theorems/theoremBody" + str(i) + ".jpg", "theoremBody" + str(i));

# process_print("definitions/defBody6.jpg");

# with open ("defBody6text", 'rb') as loadText:
#     text = pickle.load(loadText);
#     print("test:");
#     print(text);
#
# with open ("defBody6", 'rb') as loadTextList:
#     textList = pickle.load(loadTextList);
#     print("textList:");
#     print(textList);
