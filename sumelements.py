#Function definition
#args parameter to take a undefined number of numerical elements
def sum_list_elements(*numbers):
     list = []
     #Loop to add each individual number to the list

     for number in numbers:
          list.append(number)

     #Use of built in funciton sum to add all the values within our list 
     sum_numbers = sum(list)
     
     #Print function to display our final result
     print(sum_numbers)

#Calling the function
sum_list_elements()