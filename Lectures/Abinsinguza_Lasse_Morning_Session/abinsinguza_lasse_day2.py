"""
Control Structures

Conditional statements (if, elif, else)
Loops (for, while)
Comprehensions (list, dictionary 
comprehensions)
"""

#if , elif, else

age = 23

if age <18:
    print('You are an adult')
elif age > 65:
    print('You are senior citizens')
else:
    print('you are a youth')
    
    
grade = 88

if grade >= 90:
    print('Excellent')
    
elif grade >=80:
    print('very good')
    
elif grade >= 70:
    print('Good')
else: 
    print('Not good')
    
"""
childern under 13 get discount for price = shs 1000
teenagers between 13 and 18 get discount for price =shs 500
Adult 18 and above pay full price = shs 2000
otherwise senior citizen pay sh 5000
"""

new_age = input("what is your age: ")
age= int(new_age)
price = 2000

if age >=60:
    new_price = price + 3000
    print(new_price)
    
elif age >=18:
    new_price = price
    print(new_price)
elif age >=13:
    new_price= price-500
    print(new_price)
else:
    new_price = price-1000
    print(new_price)
    
#Loops (for, while)
"""
for loop iterates over a sequence (list, tuple ], dictionary, set string)
The while loop repeats as long as a condition is true 
"""

#Example

cars = ['Tesla','Audi', 'BMW', 'jeep','RangeRover']

for car in cars :
    print(car)

#Example 4 count 1 to 10

count = 1 
while count <=10:
    print("count 1 to 10:", count)
    count +=1

#Exercise 
"""
1.create your own list of favorite colors using for loop
2.create a reverse of the input 12345 to be 54321 using while loop
"""

#number 1
fav_colors = ['Green', 'Blue','red','Yellow']

for color in fav_colors :
    print (color)
    
# reversed_list = fav_colors[::-1]
#    for col in reversed_list:
#        print(col)
    
#Number 2

count = 5
while count >= 1:
    print(count)
    count -=1