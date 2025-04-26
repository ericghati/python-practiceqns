#Function definition
#This function takes a number and sums the digits of the number
def sum_digits(number):
    #intitialize the sum as zero
    sum = 0

    #while loop to check if number entered is greater than zero
    while number > 0:
        sum += number % 10  # extract last digit and add it to our sum
        number //= 10       # remove last digit after adding to sum, get the remaining number and loop again

    #return the final sum value back to the function
    return sum

#call the function within the print functionality as we pass a test argument
print(sum_digits(999))
