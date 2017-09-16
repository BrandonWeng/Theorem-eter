terms = ['B-matrix', "Cramer's", 'I', 'II', 'Inconsistent',
 'Invertible', 'Matrix', 'Of', 'Operator', 'Rule', 'Theorem', 'Vector',
 'a', 'adjugate', 'algebraic', 'algorithm', 'angle', 'augmentai', 'basis',
 'b-coordinates', 'block', 'characteristic', 'coefficient', 'coefficients',
 'cofactor', 'columns-pace', 'combination', 'consistent', 'coordinate', 'cornpcsition',
 'crcss', 'determinant', 'diagonal', 'diagonalizable',
 'dimension', 'directed', 'dot', 'eigenpair',
 'eigenspace', 'eigenvalue', 'eigenvector', 'elementary',
 'elementuy', 'equation', 'equivalent', 'four', 'free',
 'fundamental', 'gmmetric', 'homogeneous', 'hyperplane',
 'identity', 'independent', 'invertible', 'inveræ', 'kerrEI',
 'k•plane', 'left', 'length', 'line', 'linear', 'linearly', 'lower',
 'mapping', 'mappings', 'matrix', 'matrix-vector', 'multiplication', 'multiplicity',
 'norm', 'normal', 'nullspace', 'of', 'operaticns', 'orthogmal', 'orthogonal', 'parallelotope',
 'perpendicular', 'plane', 'points', 'polynomial', 'product', 'row', 'set', 'subspaces', 'system',
 'triangular', 'variable', 'vector', 'R', 'algorithm', 'basis', 'echelon', 'equation', 'equations',
         'equivalent', 'form', 'inner', 'inverse', 'linear', 'matrix', 'of', 'over', 'product', 'range',
         'rank', 'reducing', 'reducui', 'right', 'right-hand', 'rotation', 'row', 'rowspace', 'scalar',
         'set', 'side', 'similar', 'skew-symmetric', 'solution', 'space', 'span', 'standard', 'subspace',
         'system', 'test', 'trace', 'transpose', 'triangular', 'trivial', 'unit', 'upper', 'vector', 'vectors']

len_terms = 133
print(len(terms))


frequency_weights = {'subspace': 0.015651438240270727, 'scalar': 0.018401015228426396, 'polynomial': 0.00655668358714044,
 'multiplication': 0.015228426395939087, 'consistent': 0.00655668358714044, 'unique': 0.006133671742808798,
 'augment': 0.008248730964467006, 'correspond': 0.018612521150592216, 'diagonalizable': 0.004653130287648054,
 'inverse': 0.010363790186125212, 'coordinate': 0.0071912013536379014, 'coefficient': 0.015651438240270727,
 'written': 0.006133671742808798, 'rref': 0.005287648054145516, 'orthogonal': 0.004653130287648054,
 'onto': 0.005287648054145516, 'product': 0.008037225042301184, 'matrice': 0.01988155668358714,
 'det': 0.03003384094754653, 'space': 0.023900169204737733, 'system': 0.04674280879864636,
 'rank': 0.007402707275803722, 'mapping': 0.006133671742808798, 'subset': 0.004864636209813875,
 'column': 0.016074450084602367, 'plane': 0.010998307952622674, 'elementary': 0.014170896785109983,
 'Echelon': 0.018612521150592216, 'dependent': 0.005287648054145516, 'eigenvector': 0.007825719120135364,
 'basis': 0.0327834179357022, 'equation': 0.041666666666666664, 'invertible': 0.0133248730964467, 'span': 0.020516074450084604,
 'row': 0.050761421319796954, 'set': 0.037436548223350255, 'vector': 0.09412013536379019, 'independent': 0.01311336717428088,
 'combination': 0.00951776649746193, 'dimension': 0.004864636209813875, 'linear': 0.06852791878172589, 'matrix': 0.09856175972927242,
 'solution': 0.0522419627749577, 'normal': '', 'eigenvalue': 0.006979695431472081, 'projection': 0.005287648054145516,
 'determinant': 0.01311336717428088, 'multiple': 0.005922165820642978, 'homogeneous': 0.01924703891708968,
 'standard': 0.016074450084602367, 'cofactor': 0.0071912013536379014}

#OCR
api_key = "c62edc075488957"
lang = 'eng'
text = "ParsedText"
res = "ParsedResults"
parse_link = 'https://api.ocr.space/parse/image'




