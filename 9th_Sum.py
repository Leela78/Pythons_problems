# This program finds the maximum number of consecutive 1s in a list

nums = [1, 0, 1, 1, 0, 1, 0, 1, 1, 1, 1, 1]

count = 0       # To keep track of current streak of 1s
max_count = 0   # To store the maximum streak of consecutive 1s

# Loop through each element in the list
for i in range(len(nums)):
    if nums[i] != 0:          # If the current element is 1
        count += 1            # Increase the current streak count
        max_count = max(count, max_count)  # Update max if current streak is longer
    else:
        count = 0             # Reset count when a 0 is found

# Display the final result
print(f"The max consecutive ones is: {max_count}")
