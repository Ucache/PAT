line1 = [int(x) for x in raw_input().split()]
line2 = [int(x) for x in raw_input().split()]
target = (line1[0] + line2[0])/2 
if (line1[0]+line2[0])%2 != 0:
    target = target + 1
def cal(l1,l2,t):
    p = 0
    p1=0
    p2=0
    tmp=0
    while p1< len(l1) and p2 < len(l2):
        if l1[p1] < l2[p2]:
            tmp = l1[p1]
            p1 = p1 + 1
        else:
            tmp = l2[p2]
            p2 = p2 + 1
        p = p + 1
        if p == t:
            return tmp
    while p1<len(l1):
        p = p + 1
        if p == t:
            return l1[p1]
        p1 = p1 + 1
    while p2<len(l2):
        p = p + 1
        if p == t:
            return l2[p2]
        p2 = p2 + 1

print cal(line1[1:],line2[1:],target)

