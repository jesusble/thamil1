def u(r, size):
	y1 = r[1] - r[0]
	for i in range( 0, size ):
		for j in range( i+1, size ):
			if(r[j] - r[i] > y1): 
				y1 = r[j] - r[i]
	return y1
r = [15, 2, 65, 70, 119]
size1 = len(r)
print ("Maximum difference is", u(r, size1))
