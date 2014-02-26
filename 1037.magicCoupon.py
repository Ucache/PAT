n = raw_input()
a = [int(x) for x in raw_input().split()]
n = raw_input()
b = [int(x) for x in raw_input().split()]
a.sort()
b.sort()
total=0
for i in range(min(len(a),len(b))):
    if a[i]<0 and b[i]<0:
        total = total + a[i] * b[i]
for i in range(min(len(a),len(b))):
    if a[len(a)-1-i]>0 and b[len(b)-1-i]>0:
        total = total + a[len(a)-1-i] * b[len(b)-1-i]
print total
