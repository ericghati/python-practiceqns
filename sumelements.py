#Function definition
#args parameter to take a undefined number of numerical elements
def sum_list_elements(*numbers):
     list = []
     #AAdding each argument entered into a list
     for number in numbers:
          list.append(number)
     #Loop to add each individual number to the list
     total = 0
     for number in list:
          total = total + number
        
     return total

#Calling the function
print(sum_list_elements(3,4,5))
