def convertToBinary(n1):
   if n1 > 1:
       convertToBinary(n1//2)
   print(n1 % 2,end = '')
dec = 34
convertToBinary(dec) 
  
