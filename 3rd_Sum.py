# Q: Remove duplicates from sorted array and return new length
# A: Use two pointers to overwrite duplicates in-place

nums = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]   # sample input array

i = 0                                   # pointer for unique elements
n = len(nums)                           # total number of elements

for j in range(1, n):                   # start from second element
    if nums[i] != nums[j]:              # found a new unique element
        nums[i + 1] = nums[j]           # place it next to the last unique one
        i += 1                          # move unique pointer forward

print(i + 1)                            # print length of unique array
print(nums[:i + 1])                     # print array with unique elements
