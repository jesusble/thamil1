def fibo(n):
result=[]
a,b=0,1
while a<n:
  result.append(a)
  a,b=b,a+b
  return result
  data=int(input("ENter the number"))
  print(fibo(data))
  
