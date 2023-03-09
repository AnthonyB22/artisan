number1 = 20
number2 = 30
def multiSum(number_1, number_2): #def is a function, it holds statements, data, and variables
    if number_1 * number_2 <= 1000: # the if statement runs, if the number is equal or less to 1000, it will mutliply the numbers.
        return number_1 * number_2
    
    else: # this line is for when the if statement is above 1000 it will add 1000
        return number_1 + number_2 
    
Jordans = multiSum(25, 50) # i picked jordan, the jordan is calling the function and its statement, the numbers are values.
print(Jordans) # the jordan statement is being called.