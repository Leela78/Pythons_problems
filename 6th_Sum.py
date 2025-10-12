# Q: Perform Linear Search in an array
# A: Scan the array element by element to find the target

arr = [1, 3, 4, 6, 7, 8]  # example array
k = 123                     # element to search

for i in range(len(arr)):
    if arr[i] == k:                       # check if current element matches target
        print(f"Element found at index: {i} successfully")  # element found
        break                             # stop search after finding
else:
    print(f"Element {k} is not found")   # runs only if loop completes without break
