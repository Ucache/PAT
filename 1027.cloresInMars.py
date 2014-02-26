(r,g,b) = (int(x) for x in raw_input().split())
d = ['A','B','C']
def cal(n):
    r = ""
    if n/13 ==0:
        r = r + '0'
    elif n/13 > 9:
        r = r + d[n/13-10]
    else:
        r = r + str(n/13)
    if n%13 > 9:
        r = r + d[n%13-10]
    else:
        r = r + str(n%13)
    return r
print "#%s%s%s"%(cal(r),cal(g),cal(b))
