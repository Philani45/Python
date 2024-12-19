# Original list with duplicates
my_list = [1, 2, 3, 4, 2, 3, 5]

# Remove duplicates using set
unique_items = set(my_list)

# Convert back to list if needed
unique_list = list(unique_items)

print(unique_list)  # Output: [1, 2, 3, 4, 5]
