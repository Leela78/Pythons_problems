# Program to find the missing number in an array of 0..n

# Example input
nums = [3, 0, 1]

# Step 1: Sort the array
nums_sorted = sorted(nums)

# Step 2: Check each index
for i in range(len(nums_sorted)):
    if i != nums_sorted[i]:
        print("Missing number is:", i)
        break
else:
    # If all indices match, the missing number is at the end
    print("Missing number is:", len(nums_sorted))
