(n,win) = (int(x) for x in raw_input().split())
records = []
windows=[8*60*60]*win
def time2int(time):
    timesp = time.split(':')
    return float(timesp[0])*60*60+float(timesp[1])*60+float(timesp[2])

def findMin(windows):
    mini = windows[0]
    minpos = 0;
    for i in range(len(windows)):
        if windows[i] < mini:
            minpos = i
            mini = windows[i]
    return minpos

cnt = 0
for i in range(n):
    linesp = raw_input().split()
    linesp[0] = time2int(linesp[0])
    linesp[1] = int(linesp[1])*60
    if linesp[0] <= 17*60*60:
        records.append(linesp)
        cnt = cnt + 1
records.sort()

total = 0
for record in records:
    mini = findMin(windows)
    if windows[mini] >= record[0]:
        total = total + (windows[mini] - record[0])
        windows[mini] = windows[mini] + record[1]
    else:
        windows[mini] = record[0] + record[1]

if cnt==0:
    print "0.0"
else:
    print "%.1f"%(total/(60*cnt))
