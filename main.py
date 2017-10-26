#!/usr/bin/python3

users_list = []

def create_users(value):
    for new_user in range(value):
        user = []
        name = input("What's your name: ")
        user.append(name)
        users_list.append(user)

def victory(numbers_list):
    #combinations: 1,2,3 | 4,5,6 | 7,8,9 | 1,4,7 | 2,5,8 | 3,6,9 | 1,5,9 | 7,5,3
    #gonna try to calculate distance instead of making 8 fucking If's
    lists = ["Hiei", 1, 2, 4, 5, 9]
    print(numbers_list[1:]) #Skip name element
    

def game():
    while True:
        for user in range(len(users_list)):
            number = int(input("What number do you pick: "))
            users_list[user].append(number)
            victory(users_list[user])


top_row = [1, 2, 3]
middle_row = [4, 5, 6]
bottom_row = [7, 8, 9]

print(' '.join(str(value) for value in top_row))
print(' '.join(str(value) for value in middle_row))
print(' '.join(str(value) for value in bottom_row))


create_users(2) #Change this number to create more users (2)
game()
