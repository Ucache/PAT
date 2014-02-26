(s1,s2,n) = (int(x) for x in raw_input().split())
r=[-1]*100000
flag = False
def binary(lo,lt):
    low = 0
    high = len(lt) -1
    common = -1
    while low <=high:
        mid = (low + high)/2
        if lo[mid] == lt[mid]:
            common = lt[mid]
            high = mid -1
        else:
            low = mid + 1
    return common
for i in range(n):
    (ss1,ss2,a) = (x for x in raw_input().split())
    a = int(a)
    ss1 = int(ss1)
    r[ss1] = a
cn1=0
pos1=s1
l1=[]
while pos1 != -1:
    l1.append(pos1)
    cn1 = cn1 + 1
    pos1 = r[pos1]
cn2=0
pos2=s2
l2=[]
while pos2 != -1:
    l2.append(pos2)
    cn2 = cn2 + 1
    pos2 = r[pos2]
    
if len(l1) < len(l2):
    len1 = l2
    len2 = l1
else:
    len1 = l1
    len2 = l2
common = binary(len1[(len(len1)- len(len2)):],len2)
if common == -1:
    print "-1"
else:
    print "%05d"%common
