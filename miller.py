import math
n=53
t=n-1

for k in range (1,n):
	x=t%math.pow(2,(k))
	
	if x!=0:
		
		m=int( t/math.pow(2,(k-1)))
		print(m)
		break;
	
a=2

c= math.pow(a,m)
print(c)
ans=c%n
print(ans)
b=ans
for i in range (2,7):

	if b==1:
		print("composite")
		break;
	elif b==(-1):
		print("prime")
		break;
	else:
		an=math.pow(ans,i)
		b=an%n
		print(b,an,i,ans)
