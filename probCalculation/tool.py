terms = ['B-matrix', "Cramer's", 'I', 'II', 'Inconsistent',
 'Invertible', 'Matrix', 'Of', 'Operator', 'Rule', 'Theorem', 'Vector',
 'a', 'adjugate', 'algebraic', 'algorithm', 'angle', 'augmented', 'basis',
 'b-coordinates', 'block', 'characteristic', 'coefficient', 'coefficients', 'cartesian',
 'cofactor', 'column-space', 'combination', 'consistent', 'coordinate', 'composition',
 'cross', 'determinant', 'diagonal', 'diagonalizable','expansion','consistent','dependent','equal',
 'dimension', 'directed', 'dot', 'eigenpair','diagonalization',
 'eigenspace', 'eigenvalue', 'eigenvector', 'elementary','eigenvalue',
 'elementary', 'equation', 'equivalent', 'four', 'free','range',
 'fundamental', 'geometric', 'homogeneous', 'hyperplane', 'field','inequality','unit',
 'identity', 'independent', 'invertible', 'inverse', 'kernel', 'inconsistent','infinite',
 'k-plane', 'left', 'length', 'line', 'linear', 'linearly', 'lower',
 'mapping', 'mappings', 'matrix', 'matrices', 'matrice', 'matrix-vector', 'multiplication', 'multiplicity',
 'norm', 'normal', 'nullspace', 'of', 'operations', 'orthogonal', 'hyperplane', 'projection',
 'perpendicular', 'plane', 'points', 'polynomial', 'product', 'row', 'set', 'subspaces', 'system','echelon',
 'triangular', 'variable', 'vector', 'R', 'algorithm', 'basis', 'echelon', 'equation', 'equations',
         'equivalent', 'form', 'inner', 'inverse', 'linear', 'matrix', 'of', 'over', 'product', 'range',
         'rank', 'reducing', 'reduced', 'right', 'right-hand', 'rotation', 'operations', 'rowspace', 'scalar',
         'set', 'side', 'similar', 'skew-symmetric', 'solution', 'space', 'span', 'standard', 'subspace',
         'system', 'test', 'trace', 'transpose', 'triangle', 'trivial', 'unit', 'upper', 'vector', 'vectors']

cleaned = sorted(list(set(terms)))
data_dict = {}
for all in cleaned:
    data_dict[all] = 0
print(data_dict)