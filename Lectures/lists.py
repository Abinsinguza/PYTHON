# Create a list with 5 items
names = ["Alice", "Bob", "Charlie", "David", "Eve"]

# Output the 2nd item
print(names[1])

# Change the first item to a new value
names[0] = "Alex"

# Output the updated list
print(names)

# Add a sixth item to the list
names.append("Frank")

# Output the updated list
print(names)

# Add "Bathel" as the 3rd item
names.insert(2, "Bathel")

# Output the updated list
print(names)

# Remove the 4th item
names.pop(3)

# Output the updated list
print(names)

# Print the last item using negative indexing
print(names[-1])

# Create a new list with 7 items
new_list = ["John", "Paul", "George", "Ringo", "Mick", "Keith", "Charlie"]

# Print the 3rd, 4th, and 5th items
print(new_list[2:5])

# List of countries
countries = ["USA", "Canada", "UK", "Australia", "Germany"]

# Make a copy of the list
countries_copy = countries.copy()

# Output the copied list
print(countries_copy)

# Loop through the list of countries
for country in countries:
    print(country)
    
# List of animal names
animals = ["Dog", "Cat", "Elephant", "Zebra", "Lion"]

# Sort in ascending order
animals_ascending = sorted(animals)
print("Ascending:", animals_ascending)

# Sort in descending order
animals_descending = sorted(animals, reverse=True)
print("Descending:", animals_descending)

# Output animal names with the letter 'a'
animals_with_a = [animal for animal in animals if 'a' in animal.lower()]
print("Animals with 'a':", animals_with_a)

# List of first names and second names
first_names = ["John", "Jane", "Jack"]
second_names = ["Doe", "Smith", "Brown"]

# Join the two lists
full_names = [f"{first} {second}" for first, second in zip(first_names, second_names)]
print(full_names)