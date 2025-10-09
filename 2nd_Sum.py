# Find two numbers in the array that add up to a given target using the two-pointer method

arr = [2, 4, 7, 3]        # original array
s = sorted(arr)            # sort the array so we can use two pointers
target_number = 7          # the number we want the sum to match

left = 0                   # start pointer (beginning of the list)
right = len(s) - 1         # end pointer (end of the list)

print(f"Sorted array is: {s}")

# keep checking until the two pointers meet
while left < right:
    sum = s[left] + s[right]   # add the two numbers

    # if the sum matches the target, we found the pair
    if sum == target_number:
        print(f"The indices of target number are: [{left}, {right}]")
        print(f"The values are: {s[left]} + {s[right]} = {target_number}")
        break

    # if the sum is smaller, move the left pointer to the right (to increase the sum)
    elif sum < target_number:
        left += 1

    # if the sum is bigger, move the right pointer to the left (to decrease the sum)
    else:
        right -= 1

# if no pair found after the loop
else:
    print(f"No two numbers found in {arr} that sum to {target_number}.")
