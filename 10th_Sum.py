from typing import List

# Example array where every number appears twice except one
nums: List[int] = [4, 1, 2, 1, 2]

# We'll store the single number here
# Start with 0 because XOR with 0 doesn't change anything
res = 0

# Go through each number in the array
for num in nums:
    # XOR the current number with the result
    # Numbers that appear twice will cancel each other out
    # The number that appears once will stay
    res ^= num

# Print the number that only appears once
print("The single number is:", res)

# Expected Output:
# The single number is: 4
