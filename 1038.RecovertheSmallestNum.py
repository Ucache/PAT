n = [x for x in raw_input().split()]
del n[0]
n.sort()
for i in range(1,len(n)):
    if n[i-1][0] == n[i][0]:
        if n[i]+n[i-1] < n[i-1]+n[i]:
            tmp = n[i]
            n[i] = n[i-1]
            n[i-1] = tmp
result=''
for i in n:
    result += i
print int(result)
