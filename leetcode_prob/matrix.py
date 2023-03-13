
matrix = [[0,0,0,0,1], [0,0,1,1,1], [1,1,1,1,1], [0,0,0,0,0]]

one = 0
final = 0
for i in matrix:
    print(i, end=None)
    one = i.count(1)
    final = final + one
print(final)

