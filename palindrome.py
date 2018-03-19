num=input("Enter any number")
sum1=0
n=num
whlie num!=0:
 rem=num%10
 sum1=sum1*10+rem
 num=num/10
if sum1==n:
 print("yes")
else:
 print("no")
