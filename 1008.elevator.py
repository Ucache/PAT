requests = [int(x) for x in raw_input().split()]
start=0
total=0
for i in range(1,len(requests)):
    if requests[i] - start > 0:
        total = total + (requests[i]-start)*6 + 5
    else:
        total = total + (start-requests[i])*4 + 5
    start = requests[i]
print total
        
