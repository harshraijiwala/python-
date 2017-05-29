def shorted(l):
	for i in range(0,len(l)):
		for j in range (i+1,len(l)):
			if l[i]>l[j]:
				temp=l[i]
				l[i]=l[j]
				l[j]=temp
		


l=[1,3,8,2,5,9]
shorted(l)
print(l)
