#Function definition
#This function takes an integer from the user
def check_number():
    number = int(input("Enter number to check: "))

    #We use a modulus operand to check if it has a reminder when divided by 2
    #If it does not, we can infer that its an even number and return a statement to the function

    if number % 2 == 0:
        return "Even number"
    
    #If it has a remainder > 0, we can infer that its an odd number and return a statement to the function
    else: 
        return "Odd number"

#We display the statement returned to the function depending on the condition it passed
print(check_number())