# Python Practice questions


# Name: Eric Chacha 
# Admission Number: 191652

Question 1 : Sum all elements in a list.

In this code I decided to implement a function that allows us to add element in a list called sum_list_elements
I decided to use *args, to allow us to enter any number of positional arguments.
I initialized the list where values will be added
I then used a for loop for every value entered when calling the function, to append it into the list
Used another for loop now to add  values within the created list
Return the result back to the function.

We also call the function at the end



QUESTION 2: Check if a number is even or odd..
I used a function that would check if a number is even or odd called: check_number
The Function allows a user to enter any number they would like to check.
After entering it, its divided by 2 to see if we'll get a remainder from that number, if we dont, we infer that its an even number. If the remainder is > 0, we infer that it is odd.
I used an if else condition to check which condition was  met after that operation. 
For each condition a statement would be returned depending on the nature of our result.
Finally I placed the function within the print functionality to display the statement returned. 

QUESTION 3: Compute factorial using a loop
I used a functoin that would compute factorial of a given number called compute_factorial
The function allows a user to enter a number they would like to get the factorial for.
0 and 1 numbers automatically lead to a return value of 1
It then initializes a total variable with the same value as the number entered to multiply it by the sequence below it.
We then create a FOR loop to iterate multiplication of numbers within our range of numbers.
We finally returned the total after exiting the loop bakc to our function
The value returned is then displayed at the end under the print functionality, as we call the function.

QUESTION 4: Reverse a string (without using [::-1] or built-in methods).
I used a  function that would reverse a string using a for loop called reverse_string
The string argument is passed in the function and the for loop seperateds the characters in the string and adds one after another to the left of th initial charachter.
This therefore reverses the string.
The final string result is then returned to the function.
The function can then be called and a string argument to be reversed passed.

QUESTION 5: Factorial (Recursive)
I used  a function called factorial_recursive that computes factorial of a number recursively
0 and 1 numbers automatically lead to a return value of 1
Then theres the recursive operation that begins with our number which is multiplied by the factorial of the next and so on
The function is then called in a print functionality as an  argument is passed.

QUESION 6: Sum of Digits of a Number
I used a function called sum_digits which takes a number and get the sum of the digits of those numbers
It intializes our sum as zero
It then starts computing the sum by adding digits from the right to our sum and removing that digit when done until  all digits are cleared and we finally have 0.
The final sum is then returned to the function.  
The function is then called under a print functionality with a test argument passed
