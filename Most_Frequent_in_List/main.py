# Get input from the user as a string, with elements separated by commas
any_string = input("Input your list separated by , :").split(",")

# Use the max function to find the element that appears most frequently in the list
# First, convert the list to a set to remove duplicates
# Then, use the count method to count how many times each element appears in the original list
# Finally, use the key argument to tell the max function to compare elements based on their count
most_common = max(set(any_string), key=any_string.count)

# Print the most common element
print(most_common)

