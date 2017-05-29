def right_rotation(a,k,n):
	
	for j in range (0,k):
		temp=a[n-1]
		for i in range(0,n-1):
			a[n-i-1]=a[n-i-2]
		a[0]=temp


a=[1,2,3,4,5]

right_rotation(a,1,5)
print(a)
