n = int(raw_input())

def cal(n):
    lists = [0]*10
    while n:
        lists[n%10] = lists[n%10] + 1
        n = n / 10
    return lists

double = n*2
if cal(n) == cal(double):
    print "Yes"
else:
    print "No"
print double
