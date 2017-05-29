import math
l="harshsrah"
x=int(len(l)/2)

 
for i in range (0,x):
	
	if l[i] == l[(2*x-i)]:
		flag="true"
	else: 
		flag="false"

if flag=="true":
	print("palindrom")
else:
	print("no")


