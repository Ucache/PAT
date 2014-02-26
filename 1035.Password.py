n = int(raw_input())
d={'1':'@','0':'%','l':'L','O':'o'}
r=[]
def check(p):
    s=''
    for i in p:
        if d.has_key(i):
            s += d[i]
        else:
            s += i
    return s
for i in range(n):
    (name,password) = (x for x in raw_input().split())
    if password != check(password):
        r.append([name,check(password)])

if len(r) == 0:
    if n==1:
        print "There is 1 account and no account is modified"
    else:
        print "There are %d accounts and no account is modified"%n
else:
    print len(r)
    for item in r:
        print item[0],item[1]

