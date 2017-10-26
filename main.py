#!/usr/bin/python3

users_list = []
symbols = ["X", "O"]

def create_users(value):
    n = 0
    for new_user in range(value):
        user = []
        name = input("\nWhat's your name: ")
        symbol = symbols[n]
        n = 1
        user.append(name)
        user.append(symbol)
        users_list.append(user)

def change_value(number, symbol): #create variable to pass X or O
    if number in top_row:
        index = top_row.index(number)
        top_row[index] = symbol
    elif number in middle_row:
        index = middle_row.index(number)
        middle_row[index] = symbol
    elif number in bottom_row:
        index = bottom_row.index(number)
        bottom_row[index] = symbol

def print_board():
    print(' '.join(str(value) for value in top_row))
    print(' '.join(str(value) for value in middle_row))
    print(' '.join(str(value) for value in bottom_row))

def victory(lists): #combinations: 1,2,3 | 4,5,6 | 7,8,9 | 1,4,7 | 2,5,8 | 3,6,9 | 1,5,9 | 7,5,3
    for number in lists:
        indice = [(index, row.index(number)) for index, row in enumerate(matrix) if number in row]
        for v, i in indice: #index of list in matrix, index inside the list

            #Horizontal match
            _i, _v, = 0, 0 #Optional variables to turn columns or rows to 0, to avoid out of range
            if matrix[v][_i] in lists and matrix[v][_i+1] in lists and matrix[v][_i+2] in lists:
                print("\nRow match", end='\n')
                print("CONGRATULATIONS, User", lists[0], "Has won!!!!")
                return 9

            #Vertical match
            elif matrix[_v+1][i] in lists and matrix[_v][i] in lists and matrix[_v+2][i] in lists:
                print("\nColumn match", end='\n')
                print("CONGRATULATIONS, User", lists[0], "Has won!!!!")
                return 9

            #diagonal \ match
            elif matrix[_v][_i] in lists and matrix[_v+1][_i+1] in lists and matrix[_v+2][_i+2] in lists:
                print("\nDiagonal \ Match", end='\n')
                print("CONGRATULATIONS, User", lists[0], "Has won!!!!")
                return 9

            #diagonal / match
            elif matrix[_v+2][_i] in lists and matrix[_v+1][_i+1] in lists and matrix[_v][_i+2] in lists:
                print("\nDiagonal / Match", end='\n')
                print("CONGRATULATIONS, User", lists[0], "Has won!!!!")
                return 9
    else:
        return 1
    

def game():
    value = 0
    while value < 9:
        for user in range(len(users_list)):                     
            print("\nUser's", users_list[user][0], "turn")
            number = int(input("What number do you pick: "))
            print("\n")
            symbol = users_list[user][1]
            users_list[user].append(number)
            change_value(number, symbol)
            print_board()
            value += victory(users_list[user])
            if value >= 9:
                print("\nWe have a draw here!! nice game")
                break
            else:
                continue
            
matrix = []
top_row = [1, 2, 3]
middle_row = [4, 5, 6]
bottom_row = [7, 8, 9]

matrix.append(top_row)
matrix.append(middle_row)
matrix.append(bottom_row)

print_board()

create_users(2) #Change this number to create more users (2)
game()
