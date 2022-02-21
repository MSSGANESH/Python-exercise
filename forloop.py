my_list = [1,2,3]
for item in my_list:
    print(item)


"""
print formatting
name = "Ganesh"
age = 19

print(f'{name} is {age} years old')
"""

index_count = 0
for letter in 'abcde':
   print('At index {} the letter is {}'.format(index_count, letter))
   index_count += 1

# enumerate method--> it gives the index value automaticlly
word = 'abcde'
for item in enumerate(word):
    print(item)