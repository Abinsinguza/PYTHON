# Define the dictionary
Shoes = {
    "brand": "Nick",
    "color": "black",
    "size": 40
}

# Print the value of the shoe size
print(Shoes["size"])

# Change the value of "brand" to "Adidas"
Shoes["brand"] = "Adidas"

# Output the updated dictionary
print(Shoes)

# Add the key/value pair "type": "sneakers"
Shoes["type"] = "sneakers"

# Output the updated dictionary
print(Shoes)

# Return a list of all the keys
keys_list = list(Shoes.keys())

# Output the list of keys
print(keys_list)

# Return a list of all the values
values_list = list(Shoes.values())

# Output the list of values
print(values_list)

# Check if "size" exists in the dictionary
is_size_key_present = "size" in Shoes

# Output the result
print("Is 'size' key present?", is_size_key_present)

# Loop through the dictionary
for key, value in Shoes.items():
    print(f"{key}: {value}")
    
 # Remove "color" from the dictionary
Shoes.pop("color")

# Output the updated dictionary
print(Shoes)   

# Empty the dictionary
Shoes.clear()

# Output the empty dictionary
print(Shoes)

# Define a new dictionary
my_dict = {
    "name": "Alice",
    "age": 30,
    "city": "New York"
}

# Make a copy of the dictionary
my_dict_copy = my_dict.copy()

# Output the copied dictionary
print(my_dict_copy)

# Define a nested dictionary
nested_dict = {
    "person1": {
        "name": "Alice",
        "age": 30
    },
    "person2": {
        "name": "Bob",
        "age": 25
    }
}

# Output the nested dictionary
print(nested_dict)