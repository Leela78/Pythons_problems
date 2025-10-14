# QLA: Sort Colors (Dutch National Flag Problem)
# Approach: Use three pointers (low, mid, high) to sort 0s, 1s, and 2s in one pass.

nums = [2, 0, 2, 1, 1, 0]   # sample input

n = len(nums)
low = 0        # pointer for 0s
mid = 0        # current element pointer
high = n - 1   # pointer for 2s

# loop until mid crosses high
while mid <= high:
    if nums[mid] == 0:
        # swap nums[low] and nums[mid]
        nums[low], nums[mid] = nums[mid], nums[low]
        low += 1
        mid += 1
    elif nums[mid] == 1:
        # just move mid ahead
        mid += 1
    else:
        # swap nums[mid] and nums[high]
        nums[mid], nums[high] = nums[high], nums[mid]
        high -= 1

print(nums)  # output: [0, 0, 1, 1, 2, 2]
