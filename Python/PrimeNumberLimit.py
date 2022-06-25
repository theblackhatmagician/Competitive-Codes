def prime(l,i,n):
    #Update multiples of prime to false
    j = 2
    while(i*j <= n):
        l[i*j] = False
        j += 1
    
    #Find next prime number "i"
    while i+1 <= n:
        if l[i+1] == False:
            i += 1
        else:
            return prime(l,i+1,n)
    
    #return the final if no more number exist
    return l
    
    
    
n = int(input("Enter Limit:"))
if n < 2:
    print("Enter Valid limit!!")
else:
    l = prime([True]*(n+1),2,n)
    for i in range(2,n+1):
        if l[i]:
            print(i,end = " ")
