l=[100,20,800,5,400,68,76]

for i in range (len(l)):
	for j in range (i+1,len(l)):
		if l[i] > l[j]:
			temp=l[i]
			l[i]=l[j]
			l[j]=temp



print (l)
