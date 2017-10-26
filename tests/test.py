lists = ["Hiei", 1,4,7]

matrix = []

top_row = [1, 2, 3]
middle_row = [4, 5, 6]
bottom_row = [7, 8, 9]

matrix.append(top_row)
matrix.append(middle_row)
matrix.append(bottom_row)

def check_if_won(): #combinations: 1,2,3 | 4,5,6 | 7,8,9 | 1,4,7 | 2,5,8 | 3,6,9 | 1,5,9 | 7,5,3
    for number in lists:
        indice = [(index, row.index(number)) for index, row in enumerate(matrix) if number in row]
        for v, i in indice: #index of list in matrix, index inside the list

        #Horizontal match
            _i, _v, = 0, 0
            if matrix[v][_i] in lists and matrix[v][_i+1] in lists and matrix[v][_i+2] in lists:
                print("Row match")
                pass #Do won here

            #Vertical match
            elif matrix[_v+1][i] in lists and matrix[_v][i] in lists and matrix[_v+2][i] in lists:
                print("Column match")
                pass #Do won here

            #diagonal \ match
            elif matrix[_v][_i] in lists and matrix[_v+1][_i+1] in lists and matrix[_v+2][_i+2] in lists:
                print("Diagonal \ Match")
                pass #Do won here

            #diagonal / match
            elif matrix[_v+2][_i] in lists and matrix[_v+1][_i+1] in lists and matrix[_v][_i+2] in lists:
                print("Diagonal / Match")
                pass #Do won here

check_if_won()