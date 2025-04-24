#Function definition
#This function allows the user to enter the number they would like to see their factorial 
#It then computes the factiorial and returns the result
def compute_factorial():
    #allows the user to enter the number they would like to see their factorial
    number = int(input("Enter the factorial number: "))

    #initialize total with same value as number
    total = number
    #loop for numbers within our set range
    for i in range(1, number):
        #multiplying the numbers consecutively in their order
        total *= i
    #statement to return the result back to the function
    return total

#Displaing the value associated with the function
print(compute_factorial())
        

