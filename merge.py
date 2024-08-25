# Python program for implementation of MergeSort

# Merges two subarrays of arr[].
# First subarray is arr[l..m]
# Second subarray is arr[m+1..r]
size = int(input("please enter the list size: "))
print("") # terminal ekranında karışıklığı gidermek için
my_list = [] # boş bir liste tanımlıyoruz


i = 0
while i<size:
    crew = int(input(f"please enter the {i}. crew: "))
    my_list.append(crew)
    i+=1
#burada dizi boyutumuzu aldık ve içerisini doldurduk

def merge(my_list, l, m, r):
	n1 = m - l + 1
	n2 = r - m

	# create temp arrays
	L = [0] * (n1)
	R = [0] * (n2)

	# Copy data to temp arrays L[] and R[]
	for i in range(0, n1):
		L[i] = my_list[l + i]

	for j in range(0, n2):
		R[j] = my_list[m + 1 + j]

	# Merge the temp arrays back into arr[l..r]
	i = 0	 # Initial index of first subarray
	j = 0	 # Initial index of second subarray
	k = l	 # Initial index of merged subarray

	while i < n1 and j < n2:
		if L[i] <= R[j]:
			my_list[k] = L[i]
			i += 1
		else:
			my_list[k] = R[j]
			j += 1
		k += 1

	# Copy the remaining elements of L[], if there
	# are any
	while i < n1:
		my_list[k] = L[i]
		i += 1
		k += 1

	# Copy the remaining elements of R[], if there
	# are any
	while j < n2:
		my_list[k] = R[j]
		j += 1
		k += 1

# l is for left index and r is right index of the
# sub-array of arr to be sorted


def mergeSort(my_list, l, r):
	if l < r:

		# Same as (l+r)//2, but avoids overflow for
		# large l and h
		m = l+(r-l)//2

		# Sort first and second halves
		mergeSort(my_list, l, m)
		mergeSort(my_list, m+1, r)
		merge(my_list, l, m, r)


# Driver code to test above

n = len(my_list)
print("Given array is")
for i in range(n):
	print("%d" % my_list[i],end=" ")

mergeSort(my_list, 0, n-1)
print("\n\nSorted array is")
for i in range(n):
	print("%d" % my_list[i],end=" ")

# This code is contributed by Mohit Kumr