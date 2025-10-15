# Kadane's Algorithm to find maximum subarray sum

nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]  # example array
max_sum = nums[0]  # initialize max_sum as first element (important for all negative arrays)
sum = 0  # running sum of current subarray
n = len(nums)

for j in range(len(nums)):
    sum += nums[j]               # add current element to running sum
    max_sum = max(max_sum, sum)  # update max_sum if running sum is bigger
    if sum < 0:                  # if running sum becomes negative, discard it
        sum = 0

print("Maximum subarray sum is:", max_sum)
