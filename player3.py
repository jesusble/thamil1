def printRepeating(arr, size):
	print("Repeating elements are ", end = '')
	for i in range (0, size):
		for j in range (i + 1, size):
			if arr[i] == arr[j]:
				print(arr[i], end = ' ')
arr=[4,3,2,4,53,1]
arr_size=len(arr)
printrepeating(arr,arr_size)
