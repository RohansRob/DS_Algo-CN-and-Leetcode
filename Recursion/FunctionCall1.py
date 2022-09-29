def fact(n):
    if n == 0 :
        return 1
    return n * fact(n-1)

# def fact1(n):
#     if n == 0:
#         return 1
#     SmallOuput = fact(n-1)
#     return n * SmallOutput     
#

n = int(input())
fact(n)