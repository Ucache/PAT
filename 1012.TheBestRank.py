(n,q) = (int(x) for x in raw_input().split())
r=[]
rank=[3000]*1100010
ranka=[-1]*1100010
for i in range(n):
    r.append([int(x) for x in raw_input().split()])
    r[i].append((r[i][1]+r[i][2]+r[i][3])/3.0)
for i in range(4):
    tmp = sorted(r,key=lambda rec:rec[(i+3)%4+1],reverse=True);
    lastrank=0
    lastgrade=tmp[0][(i+3)%4+1]
    rank[tmp[0][0]] = 0
    ranka[tmp[0][0]] = i
    for j in range(1,len(tmp)):
        if lastgrade != tmp[j][(i+3)%4+1]: 
            lastrank = j;
            lastgrade = tmp[j][(i+3)%4+1] 
        if lastrank < rank[tmp[j][0]]:
            rank[tmp[j][0]] = lastrank 
            ranka[tmp[j][0]] = i

for i in range(q):
    id = int(raw_input())
    if(rank[id]<3000):
        print rank[id]+1,
        if ranka[id] == 0:
            print 'A'
        elif ranka[id] == 1:
            print 'C'
        elif ranka[id] == 2:
            print "M"
        elif ranka[id] ==3:
            print 'E'
    else:
        print "N/A"
