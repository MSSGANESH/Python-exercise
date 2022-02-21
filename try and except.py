Text = input("Enter Your Username :-")



try:
    username = int(Text)
    print('Your Username is :- ', username)
except:
    print('Your User name should only contain Digits')
