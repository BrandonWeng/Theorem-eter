import constants as const
import pickle
import theorem
import calc


def find_weights():
    for i in range(1, const.num_the):
        defname = "defBody%s" % (i)
        defname1 = "defBody%stext" % (i)
        thename = "theoremBody%stext" % (i)
        file = "/Users/mac/Desktop/htn2017/theorm-eter/extracted_theromes+defs/theoremBodyExtract/" + thename
        print(i)
        with open(file, 'rb') as loadText:
            text = pickle.load(loadText);
            print("the calculated score is ")
            print(str(calc.score_calc(text))+'\n')
            print("test:")
            print(text)

find_weights()












