#Function definition
#Function called factorial_recursive takes an argument and computes its factorial using recursion
def factorial_recursive(number):
    
    #if condition to account for a 0 or 1
    if number == 0 or number == 1:
        return 1
    #recursive step that begins with our number and is multiplied by the next numbers factorial and so on
    else:
        total =  number * factorial_recursive(number - 1)
        return total

#Calling the function within print functionality with a test argument
print(factorial_recursive(3))
