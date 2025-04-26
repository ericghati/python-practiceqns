#function definition
#This function takes a string argument whose characters would be reversed

def reverse_string(string):
    #We initialize the string variable to a string format whic we leave blank
    reversed_string = ""

    #For loop adding one character to the next starting with the first letter and adding the rest to the left per loop
    for char in string:
        reversed_string = char + reversed_string

    #statement to return the final inverted string back to the function
    return reversed_string

#calling the function under print functionality with a test argument
print(reverse_string("python"))