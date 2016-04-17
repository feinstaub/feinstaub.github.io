#
# Matrix / "2-Dimensionale Arrays":
#

# Methode 1
# (http://stackoverflow.com/questions/6667201/how-to-define-two-dimensional-array-in-python)
#

# Herleitung:

print([ i for i in range(5) ])
# [0, 1, 2, 3, 4]

print([ i + 5 for i in range(5) ])
# [5, 6, 7, 8, 9]

print([ 0 for i in range(5) ])
# [0, 0, 0, 0, 0]

print([ i for i in range(5) ] * 3)
# [0, 1, 2, 3, 4, 0, 1, 2, 3, 4, 0, 1, 2, 3, 4]

print([ [ i for i in range(5) ] for i in range(3) ])
# [[0, 1, 2, 3, 4], [0, 1, 2, 3, 4], [0, 1, 2, 3, 4]

# Definition einer mxn-Matrix
# siehe https://de.wikipedia.org/wiki/Matrix_%28Mathematik%29
# m Zeilen, n Spalten
# 3x5-Matrix (3 Zeilen, 5 Spalten)

matrix = [ [ 0 for i in range(5) ] for i in range(3) ]
#                             n                   m

print(matrix)
# [[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]]
# oder anders formatiert:
# [ [0, 0, 0, 0, 0],
#   [0, 0, 0, 0, 0],
#   [0, 0, 0, 0, 0] ]

for y in range(3):
    for x in range(5):
        matrix[y][x] = y * 10 + x

print(matrix)
# [[0, 1, 2, 3, 4], [10, 11, 12, 13, 14], [20, 21, 22, 23, 24]]
# oder anders formatiert:
# [ [ 0,  1,  2,  3,  4],
#   [10, 11, 12, 13, 14],
#   [20, 21, 22, 23, 24] ]

print(matrix[1][2])
# 12


# Methode 2
# (/usr/share/doc/packages/python3-qt5-devel/examples/widgets/tetrix.py)
#

m = 3
n = 5
# 3x5-Matrix (3 Zeilen, 5 Spalten)
matrix = [ 0 for i in range(m * n) ]

print(matrix)
# [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

for y in range(m):
    for x in range(n):
        matrix[y * n + x] = y * 10 + x

print(matrix)
# [0, 1, 2, 3, 4, 10, 11, 12, 13, 14, 20, 21, 22, 23, 24]
# oder anders formatiert:
# [ 0,  1,  2,  3,  4,
#  10, 11, 12, 13, 14,
#   20, 21, 22, 23, 24]

print(matrix[1 * n + 2])
# 12
