num=int(input("Enter num:"))
while(num!=0):
 rev=rev*10;
 rev=rev+num%10;
 num=num/10;
 print("reverse number:",rev)
