import sys
lines = sys.stdin.readlines()
records = []
for line in lines[1:]:
    single_record = line.split()
    records.append(single_record)
def f1(a,b):
    return cmp(a[1],b[1])
records.sort(cmp=f1)
print records[0][0],

def f2(a,b):
    return cmp(b[2],a[2])
records.sort(cmp=f2)
print records[0][0]
