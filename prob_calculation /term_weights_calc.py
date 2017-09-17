import constants as const
import pickle
import theorem
import calc
import os

# resets and calculates the values of the frequency based weight function of key terms
# takes in all the OCR scanned files and processes it, retuning the newly weighed terms

def find_weights():
    nina = 0
    term_dict = {'algebraic': 0, 'augmented': 0, 'rule': 0, 'side': 0, 'eigenvalue': 0, 'skew-symmetric': 0,
                 'right-hand': 0, 'dot': 0, 'theorem': 0, 'invertible': 0, 'lower': 0, 'vector': 0, 'linearly': 0,
                 'perpendicular': 0, 'length': 0, 'operator': 0, 'matrix-vector': 0, 'orthogonal': 0,
                 'polynomial': 0, 'product': 0, 'characteristic': 0, 'inverse': 0, 'cofactor': 0, 'nullspace': 0,
                 'combination': 0, 'composition': 0, 'invertible': 0, 'diagonalization': 0, 'trace': 0,
                 'independent': 0,
                 'adjugate': 0, 'variable': 0, 'normal': 0, 'cross': 0, 'multiplicity': 0, 'coordinate': 0, 'equal': 0,
                 'equivalent': 0, 'matrice': 0, 'vectors': 0, 'vector': 0, 'dimension': 0, 'solution': 0, 'block': 0,
                 'span': 0, 'transpose': 0, 'cartesian': 0, 'free': 0, 'trivial': 0, 'line': 0, 'rank': 0,
                 'form': 0, 'unit': 0, 'consistent': 0, 'subspace': 0, 'coefficient': 0,
                 'similar': 0, 'reducing': 0, 'inconsistent': 0, 'mapping': 0, 'points': 0, 'test': 0, 'angle': 0,
                 'operations': 0, 'homogeneous': 0, 'R': 0, 'subspaces': 0, 'multiplication': 0, 'inconsistent': 0,
                 'rotation': 0, 'row': 0, 'mappings': 0, 'matrix': 0, 'kernel': 0, 'elementary': 0, 'triangle': 0,
                 'directed': 0, 'infinite': 0, 'space': 0, 'equations': 0, "cramers": 0, 'eigenspace': 0,
                 'eigenpair': 0, 'basis': 0, 'expansion': 0, 'scalar': 0, 'eigenvector': 0, 'right': 0,
                 'plane': 0, 'system': 0, 'matrices': 0, 'echelon': 0, 'four': 0, 'reduced': 0, 'identity': 0,
                 'diagonal': 0, 'hyperplane': 0, 'inner': 0, 'coefficients': 0, 'matrix': 0, 'algorithm': 0,
                 'b-coordinates': 0, 'norm': 0, 'rowspace': 0, 'column-space': 0, 'k-plane': 0,
                 'fundamental': 0, 'triangular': 0, 'geometric': 0, 'equation': 0, 'set': 0, 'left': 0,
                 'standard': 0, 'inequality': 0, 'b-matrix': 0, 'upper': 0,
                 'range': 0, 'linear': 0, 'projection': 0, 'dependent': 0, 'field': 0,
                 'diagonalizable': 0, 'determinant': 0,'eigenvalues':0,"cramer's" :0, "cramer":0}
    for i in range(1, const.num_the):
        defname = "defBody%s" % (i)
        defname1 = "defBody%s" % (i)
        thename = "theoremBody%s" % (i)
        file = "/Users/mac/Desktop/htn2017/theorm-eter/extracted_theromes+defs/theoremBodyExtract/" + thename
        print(i)
        with open(file, 'rb') as loadText:
            text = pickle.load(loadText)
            for word in text:
                if word.lower() in term_dict:
                    nina += 1
                    term_dict[word.lower()] += 1
            #print("the calculated score is ")
            #print(str(calc.score_calc(text))+'\n')
            #print("test:")
            print(term_dict)
    print("second")
    for i in range(1, const.num_def):
        textFileName = "/Users/mac/Desktop/htn2017/theorm-eter/extracted_theromes+defs/defHeadExtract/"+"defHead%s"% (i) + '.txt'
        if (os.path.isfile(textFileName)):
            with open(textFileName, 'r') as f:
                for line in f:
                    for word in line.split():
                        if word.lower() in term_dict:
                            print("yes")
                            nina += 1
                            term_dict[word.lower()] += 1
        else:
            with open("/Users/mac/Desktop/htn2017/theorm-eter/extracted_theromes+defs/" +
                              "defBodyExtract/defBody" + str(i), 'rb') as loadTextArr:
                words = pickle.load(loadTextArr);
                for word in words:
                    if (word.lower() in term_dict):
                        term_dict[word.lower()] += 1
                        #d[word.lower()].append("defBody" + str(i) + ".jpg");
    #print(term_dict)
    print(sum(term_dict.values()))

find_weights()












