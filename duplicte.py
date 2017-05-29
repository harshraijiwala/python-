a=[9,8,0,10,8,9,7,8,6,54,47,6,5,4]

for i in range(len(a)):
	for j in range (i+1, len(a)):
		if a[i]>a[j]:
			temp=a[i]
			a[i]=a[j]
			a[j]=temp


print (a)
l=[]
for i in range (len(a)-1):
	
	if a[i]==a[i+1]:
		temp=[a[i+1]]
		l=l+ temp
			


print (l)

# remove
x=len(a)
print("list A after removing duplicate")
for i in range (0,x-1):
	if a[i]==a[i+1]  or a[i-1] == a[i]:
		
		for y in range (i,x-1):
			a[y]=a[y+1]
		x=x-1	
		print (x)
print(a)



