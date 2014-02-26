(n,base) = (int(x) for x in raw_input().split())
def s(n,base):
    r=[]
    while n:
        r.append(n%base)
        n = n / base
    return r
def check(r):
    for i in range(len(r)/2):
        if r[i] != r[len(r)-1-i]:
            return "No"
    return "Yes"
if n == 0:
    print "Yes"
    print "0"
else:
    r = s(n,base)
    print check(r)
    for i in reversed(r):
        print i,

