def function1(l,n):
			a = 0
			b = 1
			if len(l)<=1:
				print ("NO SUCH PAIR")
			else:
				while b<len(l):
					if l[b]-l[a]==n:
						print (l[a], l[b])
						a=a+1
						b=b+1
					else:
						b=b+1
			return
	
l = [1,2,3,4,5,6,7,8,9]
n= 3
k = function1(l,n)
