a="abcaw"
b="bca"


for i in range(0,len(a)):
	temp=a[i]
	for j in range (0,len(b)):
		if temp == b[j]:
			
			a = a.replace(temp, '0')
			b = b.replace(temp, '0')
			
	
			
		elif temp == a[j+1]:
			a = a.replace(temp,'0')
			

a=a.replace('0','')

b=b.replace('0','')
strip_for_anagram = len(a)+len(b)
print (strip_for_anagram)

	
