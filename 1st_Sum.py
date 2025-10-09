arr=[-1,2,3,3,4,5,-1,-1,2,3]
l=0
k=4
r=k-1
n=len(arr)
sum = sum(arr[0:k])
max_sum=sum
while(r<n-1):
    sum = sum - arr[l]
    l =l+1
    r =r+1
    sum = sum +arr[r]
    max_sum =max(max_sum,sum)
print(max_sum)    
