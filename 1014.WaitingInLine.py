(n,m,k,q) = (int(x) for x in raw_input().split())
customers = [int(x) for x in raw_input().split()]
queries = [int(x) for x in raw_input().split()]
starttime=[]
leavetime=[]
windows=[8*60]*n
windowsline=[]
for i in range(n):
    windowsline.append([])

def int2time(t):
    if(starttime[t]>=17*60):
        return "Sorry"
    else:
        s = leavetime[t]
        m = "%02d" % (s%60)
        h = "%02d" % (s/60)
        return  h+':'+m

def findMin():
    minpos =0
    mini = windowsline[0][0]
    for i in range(len(windowsline)):
        if windowsline[i][0] < mini:
            minpos = i
            mini = windowsline[i][0]
    del windowsline[minpos][0]
    return minpos

pre = min(m*n,len(customers))
for i in range(pre):
    leavet = windows[i%n] + customers[i]
    starttime.append(windows[i%n])
    leavetime.append(leavet)
    windows[i%n] = leavet
    windowsline[i%n].append(leavet)

for i in range(pre,len(customers)):
    minpos = findMin()
    leavet = windows[minpos] + customers[i]
    starttime.append(windows[minpos])
    leavetime.append(leavet)
    windows[minpos] = leavet
    windowsline[minpos].append(leavet)

for q in queries:
    print int2time(q-1)
