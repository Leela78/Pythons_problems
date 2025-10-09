# Find the maximum sum of any subarray of size k using the sliding window method

arr = [-1, 2, 3, 3, 4, 5, -1, -1, 2, 3]  # given array
k = 4                                     # window size (number of elements to consider together)
l = 0                                     # left pointer (start of the window)
r = k - 1                                 # right pointer (end of the window)
n = len(arr)                              # total number of elements in the array

# calculate the sum of the first window (first k elements)
sum = sum(arr[0:k])
max_sum = sum                             # set this as the current maximum sum

# move the window one step at a time until the end of the array
while r < n - 1:
    # remove the element going out of the window (on the left)
    sum = sum - arr[l]
    l += 1                                # move left pointer one step right
    r += 1                                # move right pointer one step right

    # add the new element entering the window (on the right)
    sum = sum + arr[r]

    # update max_sum if we found a bigger sum
    max_sum = max(max_sum, sum)

# print the largest sum found
print(max_sum)
