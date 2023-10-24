def change(matrix):
    rows = len(matrix) 
    cols = len(matrix[0])
    
    if rows != cols:
        return matrix  

    for i in range(rows):
        matrix[i][i] = 0
    return matrix

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

result = change(matrix)

for row in result:
    print(row)