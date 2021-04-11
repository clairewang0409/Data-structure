# Python program for implementation of Insertion Sort

# Function to do insertion sort
def insertionSort(arr):

	# Traverse through 1 to len(arr)
	for i in range(1, len(arr)):

		key = arr[i]

		j = i-1
		while j >=0 and key < arr[j] :
				arr[j+1] = arr[j]
				j -= 1
		arr[j+1] = key


arr = [12, 11, 13, 5, 6, 0, 1 ,58 ,121, 3]
print(arr)
insertionSort(arr)
print ("Sorted array is:")
for i in range(len(arr)):
	print ("%d" %arr[i])

