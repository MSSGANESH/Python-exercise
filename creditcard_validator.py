def luhn_checksum(card_number):
    def digits_of(n):
        return [int(d) for d in str(n)]
    digits = digits_of(card_number)
    odd_digits = digits[-1::-2]
    print(odd_digits)
    even_digits = digits[-2::-2]
    print(even_digits)
    checksum = 0
    checksum += sum(odd_digits)
    print(checksum)
    for d in even_digits:
        checksum += sum(digits_of(d*2))
    
    return checksum % 10
    


if luhn_checksum(input("Please Enter Your Card Number:-"))==0:
    print('Valid') 
else :
    print('Invalid')