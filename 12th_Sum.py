# Q1: Find the majority element in a list

# Given a list of numbers, the goal is to find the element 
# that appears more than n/2 times (where n is the length of the list).

nums = [3, 2, 3]  # sample input list

# Step 1: Sort the list so that the majority element will be in the middle
nums.sort()

# Step 2: Calculate the middle index
mid = len(nums) // 2

# Step 3: The element at the middle index is the majority element
print(nums[mid])
