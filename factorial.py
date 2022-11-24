def fact(n):
	res = 1	
	for i in range(1,n+1):
		res = res * i
	return res

#Driver code
t = 10
print(fact(t))