import pickle
import os.path

index = ['addition', 'adjugate', 'algebraic', 'algorithm', 'angle', 'augmented', 'b-coordinates', 'b-matrix', 'basis', 'block', 'cartesian', 'characteristic', 'coefficient', 'coefficients', 'cofactor', 'column-space', 'combination', 'composition', 'consistent', 'coordinate',
"cramer's", 'cross', 'dependent', 'determinant', 'diagonal', 'diagonalizable', 'diagonalization', 'dimension', 'directed', 'dot', 'echelon', 'eigenpair', 'eigenspace', 'eigenvalue', 'eigenvector', 'elementary', 'equal', 'equation', 'equations', 'equivalent', 'expansion', 'field', 'form', 'free', 'fundamental',
'geometric', 'homogeneous', 'hyperplane', 'identity', 'inconsistent', 'inconsistent', 'independent', 'inequality', 'infinite', 'inner', 'inverse', 'invertible', 'invertible', 'k-plane', 'kernel', 'left', 'length', 'line', 'linear', 'linearly', 'lower', 'mapping', 'mappings', 'matrice', 'matrices',
'matrix', 'matrix-vector', 'multiplication', 'multiplicity', 'norm', 'normal', 'nullspace', 'operations', 'operator', 'orthogonal', 'over', 'perpendicular', 'plane', 'points', 'polynomial', 'product', 'projection', 'r', 'range', 'rank', 'reduced', 'reducing', 'right', 'right-hand', 'rotation',
'row', 'rowspace', 'rule', 'scalar', 'set', 'side', 'similar', 'skew-symmetric', 'solution', 'space', 'span', 'standard', 'subspace', 'subspaces', 'system', 'test', 'theorem', 'trace', 'transpose', 'triangle', 'triangular', 'trivial', 'unit', 'upper', 'variable',
 'vector', 'vectors']

d = {};
numDef = 83;
numTheorems = 96;

for word in index:
    d[word] = [];

for i in range(1, numDef):
    textFileName = "defHeadExtract/defHead" + str(i) + ".txt";
    words = [];
    if(os.path.isfile(textFileName)):
        with open(textFileName,'r') as f:
            for line in f:
                for word in line.split():
                    words.append(word);
    else:
        with open ("defBodyExtract/defBody" + str(i), 'rb') as loadTextArr:
            words = pickle.load(loadTextArr);

    for word in words:
        if(word.lower() in d):
            d[word.lower()].append("defBody" + str(i) + ".jpg");

for i in range(1, numTheorems):
    textFileName = "theoremBodyExtract/theoremBody" + str(i);
    with open(textFileName, 'rb') as loadTextArr:
        words = pickle.load(loadTextArr);
        for word in words:
            if(word.lower() in d):
                d[word.lower()].append("theoremBody" + str(i) + ".jpg");

#filter out keywords with no fileNames
d = {k: v for k, v in d.items() if len(v) > 0}
index = [k for k, v in d.items()];

with open("KeyToFileNames", "wb") as keyValueFile:
    pickle.dump(d, keyValueFile);

with open("listOfKeys", "wb") as keysFiles:
    pickle.dump(index, keysFiles);

print(d);
print(index);
