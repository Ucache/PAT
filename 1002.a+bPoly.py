line1 = [x for x in raw_input().split()]
line2 = [x for x in raw_input().split()]
r=[0.0]*1001

def cal(line):
    for i in range(1,len(line),2):
        r[int(line[i])] = r[int(line[i])] + float(line[i+1])
cal(line1)
cal(line2)

cnt =0
for i in r:
    if i != 0.0:
        cnt = cnt + 1
print cnt,

pos = len(r)-1
while pos>=0:
    if r[pos] > 0.0:
        print "%d %.1f"%(pos,r[pos]),
    pos = pos -1
