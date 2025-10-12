# Program to find the missing number in an array of 0..n

# Example input
nums = [1,0,3]

# Step 1: Sort the array
k = sorted(nums)

# Step 2: Check each index
for i in range(len(nums)):
    if i != k[i]:
        print("Missing number is:", i)
        break
else:
    # If all indices match, the missing number is at the end
    print("Missing number is:", len(nums))
