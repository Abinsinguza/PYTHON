# Create a set of 3 favorite beverages
beverages = set(["coffee", "tea", "juice"])

# Output the set
print(beverages)

# Add 2 more items to the beverages set
beverages.add("water")
beverages.add("soda")

# Output the updated set
print(beverages)

# Define the set
mySet = {"oven", "kettle", "microwave", "refrigerator"}

# Check if "microwave" is present
is_microwave_present = "microwave" in mySet

# Output the result
print("Is 'microwave' present in the set?", is_microwave_present)

# Remove "kettle" from the set
mySet.remove("kettle")

# Output the updated set
print(mySet)


# Loop through the set
for item in mySet:
    print(item)
    
   # Define a set of 4 items and a list of 2 items
my_set = {"apple", "banana", "cherry", "date"}
my_list = ["elderberry", "fig"]

# Add elements from the list to the set
my_set.update(my_list)

# Output the updated set
print(my_set)

 # Define two sets
ages = {25, 30, 35}
first_names = {"John", "Jane", "Jack"}

# Join the two sets
combined_set = ages.union(first_names)

# Output the joined set
print(combined_set)