def partition(a,start,end):
	pivot = a[end]
	pindex=start
	 

	for i in range(start, end):
		if a[i] <= pivot:
			t=a[pindex]
			a[pindex] = a[i]
			a[i]=t
			pindex = pindex+1
	
	t = a[pindex]
	a[pindex] = pivot

	a[end] = t
	print(a)

	print("pivot")
	print(pivot)
	print("pindex")	
	print(pindex)
	return pindex


def quicksort(a):
	last = len(a) - 1
	first = 0 
	

	qsorting(a,first,last)

def qsorting(a,first,last):
	
	if first<last:
		split_half=partition(a,first,last)
		print (a)
		qsorting(a,first,split_half-1)
		print(a)
		qsorting(a,split_half+1,last)
		print(a)
				
		

a=[12,3,5,6,44,32,20,98,202, 2 , 345,50,7,87,59]
quicksort(a)
print("\n")
print(a)

