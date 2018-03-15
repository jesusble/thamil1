def findMaximum(arr,low,high):
max=arr[low]
i=[low]
for i in range(high+1):
  if arr[i]>max:
  max=arr[i]
  returnmax
  arr=[1,2,3,4,5,6]
  n=len(arr)
  print("the maximum element is %d",%findmaximum(arr,0,n-1))
