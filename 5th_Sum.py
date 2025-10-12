# Q: Move all zeros in an array to the end
# A: Two-pointer approach: keep a pointer for the next non-zero and swap elements.

nums = [0, 1, 0, 3, 12]

last_non_zero = 0  # pointer for the next non-zero position

for i in range(len(nums)):
    if nums[i] != 0:
        nums[last_non_zero], nums[i] = nums[i], nums[last_non_zero]
        last_non_zero += 1

print(nums)  # [1, 3, 12, 0, 0]

# Approach Summary:
# - Use a pointer to track where the next non-zero should go.
# - Swap each non-zero with the pointer position
# - Zeros move to the end, non-zeros maintain relative order.
# Time Complexity: O(n)
# Space Complexity: O(1)
