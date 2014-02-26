n = int(raw_input())
books=[]
def get(books,query):
    lists=[]
    for i in range(len(books)):
        if query in books[i]:
            lists.append(books[i][0])
    return lists

for i in range(n):
    item = []
    for j in range(6):
        item.append(raw_input())
    books.append(item)
print books
q = int(raw_input())
for i in range(q):
    query = raw_input()
    print query
    results = get(books,query.split()[1].strip())
    if len(results) == 0:
        print "Not Found"
    else:
        for single in results:
            print single 
