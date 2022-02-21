from random import shuffle


my_list = [' ','0',' ']
def shuffle_list(my_list):
    shuffle(my_list)

    return my_list

def player_guess():
    guess = ''
    while guess not in ['0','1','2']:
        guess = input("Enter the Number From 0 1 and 2!")

    return int(guess)
def check_number(my_list,guess):
    if my_list[guess] == '0':
        print("Correct")
    else:
        print("Wrong")
        print(my_list)

#list
my_list = [' ','0',' ']

mixed_list = shuffle(my_list)

guess = player_guess()

print(check_number(mixed_list,guess))
