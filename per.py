result=[]
current=0
def permute(string,start,end):
	#current=0
	if start ==end-1:
		if not string in result:
			result.append(string)
	else:
		for current in range(start,end):
			x=list(string)
			temp=x[start]            
			x[start]=x[current]
			x[current]=temp
			
			permute(''.join(x),start+1,end)
			temp=x[start]
			x[start]=x[current]
			x[current]=temp
			
s="abc"
permute(s,0,len(s))
print(result)
