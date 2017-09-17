import calc,pickle
import constants as const

# calls on other functions and returns the theorem/def name with the corresponding value of the calculated frequence score
# returns a dictionary with the theorem/def name as key and score as value.

def thdef_value():
    theorems_defs={}
    for i in range(1, const.num_the):
        thename = "theoremBody%s" % (i)
        file = "/Users/mac/Desktop/htn2017/theorm-eter/extracted_theromes+defs/theoremBodyExtract/" + thename
        with open(file, 'rb') as loadText:
            text = pickle.load(loadText)
            score  = calc.score_calc(text)
        theorems_defs[thename] = score

    for i in range(1, const.num_def):
        thename = "defBody%s"%(i)
        with open("/Users/mac/Desktop/htn2017/theorm-eter/extracted_theromes+defs/" +
                          "defBodyExtract/defBody" + str(i), 'rb') as loadTextArr:
            words = pickle.load(loadTextArr);
        theorems_defs[thename] = score

    print(theorems_defs)
    return theorems_defs

thdef_value()