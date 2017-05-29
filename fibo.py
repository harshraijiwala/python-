

def fibo(n):
	if n<=1:
		return n
	else:
		return ( fibo(n-1) + fibo(n-2))

x=input("enter a integer : ")


for i in range(x):
	
	y=fibo(i)
	print (y)



		
