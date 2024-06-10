#python besr practices 
"""
-Follow PEP 8
1.Indentation
2.Maximum Line Length
3.Blank Lines
4.Use meaningful names 
"""



#Python operators 
"""
Name of the operators          Symbol with Example
Addition                          x +y
Substraction                      x-y
Multiplication                    x*y
Division                          x/y
Modulus                           x%y
Exponentiation                    x**y
Floor division                    x//y

Name of the operators          Symbol with Example
Equal                             x ==y
Not equal                         x!=y
Greater than                      x > y
Less than                         x < y
Modulus                           x%y
Exponentiation                    x**y
Floor division                    x//

#Example of python Logical operator
Name #Example of python Logical operatorof the operator                        Example               
and                                              and  
or                                                or   
not                                              not   

 #Example of membership operator
 in                            x in y
 not in                         x not in y
    
 #Example of python Bitwise operator  
 Name                                                symbol
 AND                                                      &
 OR                                                      |
 XOR                                                    ^
 NOT  
 
 
 #python cases
 1.snake_case
 2.camelcase
 3.Pascalcase
 4.UPPERCASE
 5.Kebab_case                                                   
                             
"""


#comprehensions(list, dictionary comprehensions)

"""
comprehensions provide a concise way to create list and dictionaries
What is the symbol for
lists            [] square brackets  used to store multi[le items in a single variable
dictionaries     {} curly brackects used to store data values in key:value pair
"""

#Example 1: basic list comprehension 
#create a list of squares in rang of 10

list_of_squares = [x**2 for x in range(10)]
print(list_of_squares)


#Exercise 1: create a list of even squares in the range  of 20

# Create a list of even squares in the range of 20
even_squares = [x**2 for x in range(20) if x % 2 == 0]
print(even_squares)

# Example 2 : Dictionary comprehensions 
# create a dictionary comprehension for favorite cars and count the length of the characters
favorite_cars = ['BMW','Jeep', 'Mercedes','fordraptor']
car_lengths ={car: len(car) for car in favorite_cars}
print(car_lengths)


# Exercise 2: create a list of tuples where each tuple contains a number and its cube for numbers
#between 1 and 10 using a dictionary comprehension

number_cubes_dict = {x: x**3 for x in range(1, 11)}
print(number_cubes_dict)





