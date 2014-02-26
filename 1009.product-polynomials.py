import sys
lines = sys.stdin.readlines()
r = {}
linesplit0 = lines[0].split()
linesplit1 = lines[1].split()
for pos0 in range(1,len(linesplit0),2):
    for pos1 in range(1,len(linesplit1),2):
        key = int(linesplit0[pos0]) + int(linesplit1[pos1])
        if r.has_key(key):
            r[key] = r[key] + float(linesplit0[pos0+1]) * float(linesplit1[pos1+1])
        else:
            r[key] = float(linesplit0[pos0+1]) * float(linesplit1[pos1+1])
keys = r.keys()
keys.sort()
print len(keys),
for key in reversed(keys):
    if(r[key]==0.0):
        print "0 0.0"
    else:
        print "%d %.1f"%(key,r[key]),
