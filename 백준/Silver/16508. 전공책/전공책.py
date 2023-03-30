import heapq
T = list(input())
alpha = []
cnt = []
T.sort()
for t in T:
    if t not in alpha:
        alpha.append(t)
        cnt.append(1)
    else:
        cnt[-1] += 1
        
N = int(input())
books = []
for _ in range(N):
    price, text = input().split()
    text = list(text)
    book_cnt = []
    for a in alpha:
        book_cnt.append(text.count(a))
    books.append((int(price), book_cnt))

queue = []
for i in range(len(books)):
    price, book_cnt = books[i]
    ccnt = [x-y for x,y in zip(cnt,book_cnt)]
    heapq.heappush(queue,((price, ccnt,i)))

answer = -1
while queue:
    price,cnt,idx = heapq.heappop(queue)
    flag = True
    for c in cnt:
        if c > 0:
            flag = False
            break
    if flag:   
        answer = price     
        break
    else:
        for j in range(idx+1, len(books)):
            pprice, book_cnt = books[j]
            ccnt = [x-y for x,y in zip(cnt,book_cnt)]
            heapq.heappush(queue,((pprice+price, ccnt,j)))

print(answer)