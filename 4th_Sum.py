# Q: Rotate an array to the right by k steps
# A: Use reverse method (reverse all → first k → rest)

def reverse(nums, left, right):
    while left < right:
        nums[left], nums[right] = nums[right], nums[left]  # swap elements
        left += 1                                          # move left pointer
        right -= 1                                         # move right pointer

nums = [1, 2, 3, 4, 5, 6, 7]
k = 3
n = len(nums)
k = k % n                     # adjust k if larger than n

reverse(nums, 0, n - 1)       # reverse whole array
reverse(nums, 0, k - 1)       # reverse first k elements
reverse(nums, k, n - 1)       # reverse remaining part

print(nums)  
