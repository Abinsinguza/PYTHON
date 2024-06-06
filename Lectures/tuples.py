# Define the tuple
x = ("samsung", "iphone", "tecno", "redmi")

# Output your favorite phone brand (example: "samsung")
favorite_brand = "samsung"
print(f"My favorite phone brand is: {favorite_brand}")

# Print the 2nd last item using negative indexing
print(x[-2])

# Update "iphone" to "itel"
x_list = list(x)  # Convert tuple to list
x_list[1] = "itel"  # Update the item
x = tuple(x_list)  # Convert list back to tuple

# Output the updated tuple
print(x)

# Add "Huawei" to the tuple
x = x + ("Huawei",)

# Output the updated tuple
print(x)

# Loop through the tuple
for phone in x:
    print(phone)
    
  # Remove the first item
x = x[1:]

# Output the updated tuple
print(x)  

# Create a tuple of cities in Uganda
cities_in_uganda = tuple(["Kampala", "Entebbe", "Jinja", "Gulu", "Mbarara"])

# Output the tuple
print(cities_in_uganda)

# Unpack the tuple
city1, city2, city3, city4, city5 = cities_in_uganda

# Output the unpacked values
print(city1, city2, city3, city4, city5)

# Print the 2nd, 3rd, and 4th cities
print(cities_in_uganda[1:4])

# Tuples of first names and second names
first_names = ("John", "Jane", "Jack")
second_names = ("Doe", "Smith", "Brown")

# Join the two tuples
full_names = first_names + second_names

# Output the joined tuple
print(full_names)

# Create a tuple of colors
colors = ("red", "green", "blue")

# Multiply the tuple by 3
colors_multiplied = colors * 3

# Output the multiplied tuple
print(colors_multiplied)

# Define the tuple
thistuple = (1, 3, 7, 8, 7, 5, 4, 6, 8, 5)

# Count the number of times 8 appears
count_8 = thistuple.count(8)

# Output the count
print(count_8)

