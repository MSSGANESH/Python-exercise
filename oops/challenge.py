from bank import Amount
     

a = Amount('Ganesh',500)

print(a.owner)
print(a.balance)
print (a.deposit(200))
print(a.balance)
print(a)