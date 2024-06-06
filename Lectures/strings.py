# Declare an integer and a string variable
integer_var = 10
string_var = "apples"

# Concatenate the two variables
result = str(integer_var) + " " + string_var

# Output the concatenated result
print(result)

# Define the string
txt = "      Hello,       Uganda!       "

# Remove spaces at the beginning and end
txt = txt.strip()

# Remove spaces in the middle
txt = " ".join(txt.split())

# Output the result
print(txt)

# Convert to uppercase
txt_upper = txt.upper()

# Output the result
print(txt_upper)

# Replace 'U' with 'V'
txt_replaced = txt.replace('U', 'V')

# Output the result
print(txt_replaced)

# Define the string
y = "I am proudly Ugandan"

# Get the 2nd, 3rd, and 4th characters (index 1 to 3)
range_of_chars = y[1:4]

# Output the result
print(range_of_chars)

# Correct the string to avoid syntax error
x = 'All "Data Scientists" are cool!'

# Output the result
print(x)