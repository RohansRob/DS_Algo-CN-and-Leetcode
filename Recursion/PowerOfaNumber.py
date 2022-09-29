# Sample Input 1 : 3 4

def power(x,n):
    if n==0 or x==1:
        return 1
    return x*power(x,n-1)

ip=list(map(int,input().split()))
x=ip[0]
n=ip[1]
op=power(x,n)
print(op)
