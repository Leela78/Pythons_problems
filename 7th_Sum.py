"""
This small program merges two arrays (lists) and removes duplicate elements.
It shows the unique values after combining both arrays.

Example:
- arr1 = [1,2,3,4,5]
- arr2 = [2,3,4,4,5]
- Merged array = [1,2,3,4,5,2,3,4,4,5]
- Unique values = {1,2,3,4,5}
"""

# First array
arr1 = [1, 2, 3, 4, 5]

# Second array
arr2 = [2, 3, 4, 4, 5]

# Merge both arrays into one
org = arr1 + arr2

# Convert merged array to a set to remove duplicates and print the result
print(set(org))  # Output: {1, 2, 3, 4, 5}
