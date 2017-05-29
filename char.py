#sort character and number from a list

a=['a','b','A',1,2,3]
ch=[]
nu=[]
for i in range (len(a)):
	if (a[i]>='A' and a[i]<='Z') or (a[i]>='a' and a[i] <='z'):
		
		temp=[(a[i])]
		ch=ch+temp
	else:
		temp=[(a[i])]
		nu=nu+temp
		 
print (nu)
print(ch)
