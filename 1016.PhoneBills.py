charge = [int(x) for x in raw_input().split()]
n = int(raw_input())
records={}

def cal(start,end):
    (month,sday,shour,sminute) = (int(x) for x in start.split(':'))
    (month,eday,ehour,eminute) = (int(x) for x in end.split(':'))
    wholeday = 0
    for i in range(len(charge)):
        wholeday = wholeday + charge[i]*60

    total = 0
    days = 0
    if eday -sday > 0:
        total = total + (eday -sday )*wholeday
        days = (eday - sday)

    stotal = 0
    for i in range(shour):
        stotal = stotal + charge[i]*60
    stotal = stotal + charge[shour]*sminute

    etotal = 0
    for i in range(ehour):
        etotal = etotal + charge[i]*60
    etotal = etotal + charge[ehour]*eminute

    total = total + etotal - stotal
    return days*24*60+(ehour-1)*60+eminute-(shour-1)*60-sminute,total

for i in range(n):
    (name,time,line) = (x for x in raw_input().split())
    if records.has_key(name):
        records[name].append([time,line])
    else:
        records[name] = [[time,line]]

for key in sorted(records.keys()):
    records[key].sort()
    total=0
    isused=False
    for i in range(1,len(records[key])):
        if records[key][i][1] =="off-line" and  records[key][i-1][1] == "on-line":
            if not isused:
                print key,records[key][0][0].split(':')[0]
            isused=True
            print records[key][i-1][0][3:],records[key][i][0][3:],
            (minutes,cost) = cal(records[key][i-1][0],records[key][i][0])
            print "%d $%.2f"%(minutes,cost/100.0)
            total = total + cost
            i = i+2
    if isused:
        print "Total amount: $%.2f"%(total/100.0)
