from random import randint

computer=randint(0,10)

guess_limit = 5

print('Enter The Number:-')


for i in range(guess_limit):
    number = int(input())
    if number == computer :
       print("you won !")
    elif number < computer :
        print("Number is less than ")
    elif number > computer :
        print("Number is greater")
        guess_limit -=1
    elif guess_limit!=1:
        print("You have {} moves left".format(guess_limit-1))
        
        
    
# attempt = 5
# for i in range(5):
#     user_input = int(input('Enter Number: '))

#     if user_input == 7:
#         print('You won!')
#         break
#     else:
#         print(f'Try again! {attempt-1} attempts left.')
#         attempt -= 1
#         continue