s=int(input())
e=int(input())
step=int(input())
def celsius(fah):
    ans=5/9*(fah-32)
    return int(ans)
for i in range(s,e+1,step):
    print(i,"\t",celsius(i))

