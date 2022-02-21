# from unicodedata import name


# def  square(num):
#     return num**2
# my_list = [1,2,3,4,5]

# for item in map(square,my_list):
#     print(item)

# print(list(map(square,my_list)))

# def splicer(mystring):
#     if len(mystring)%2 == 0:
#         return 'EVEN'
#     else:
#         return mystring[0]
# names = ['ganesh','sai','shankar']

# print(list(map(splicer,names)))


def check_even(num):
    return num%2==0
my_num = [1,2,3,4,5,6]

print(list(map(check_even,my_num)))
print('\n')
#filter method

def check_num(n1):
    return n1%2 == 0
my_n = [1,2,3,4,5,6]

print(list(filter(check_num,my_n)))

#filter mehtod enables us to give the output of the desired condition


square=lambda num:num**2

print(square(5))

print(list(map(lambda num:num**2,my_num)))

print(list(filter(lambda num:num%2==0,my_num)))