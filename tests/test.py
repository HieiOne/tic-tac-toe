lists = ["Hiei", 1, 2, 3]

matrix = []

top_row = [1, 2, 3]
middle_row = [4, 5, 6]
bottom_row = [7, 8, 9]

matrix.append(top_row)
matrix.append(middle_row)
matrix.append(bottom_row)

for number in lists[1:]:
    indice = [(index, row.index(number)) for index, row in enumerate(matrix) if number in row]
    for v, i in indice: #index of list in matrix, index inside the list
        #Vertical match
        print(v, i+1)
        print(matrix[v][i+1])
        if matrix[v][i] in lists and matrix[v][i+1] in lists and matrix[v][i+2] in lists:
            print("Row match")
            break
        #Horizontal match

        #\ match

        #/ match

    print(indice)