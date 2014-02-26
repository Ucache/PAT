from operator import itemgetter,attrgetter
(n,c) = (int(x) for x in raw_input().split())
lists=[]
for i in range(n):
    lists.append([x for x in raw_input().split()])
for item in sorted(lists, key=itemgetter(c-1,0)):
    for i in item:
        print i,
    print 
