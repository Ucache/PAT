h = raw_input();
n = len(h)
if n % 2 == 0:
    start = 4
else:
    start = 3
for i in range(start,n,2):
    if (n+2-i)/2 <= i:
        a = (n+2-i)/2
        b = i
        break
pos = 0
for i in range(a-1):
    print h[pos],
    if b > 3:
        print " "*(b-4),
    print h[len(h)-1-pos]
    pos = pos + 1
print h[a-1:a+b-1]
