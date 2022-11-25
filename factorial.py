#!/usr/bin/python3
def fact(n):
    #Expected output is -1 ... but I have changed it to 1 to get wrong ans in test cases
    if (n < 0):
        return 1
    else :
        res = 1	
        for i in range(1,n+1):
            res = res * i
        return res

#Driver code
t = 10
print(fact(t))
