
def factorial (number,):
    if int(number) <= 1 :
        return 1;
    else:
       return int(factorial( number - 1) * number)
number = int(input("add number to factorial"))
print(factorial(number))
