import heapq
def solution(book_time):
    answer = 0
    books = []
    for s, e in book_time:        
        s = 100*int(s[0:2])+int(s[3:5])        
        e = 100*int(e[0:2])+int(e[3:5])
        heapq.heappush(books,(s,e))
        
    rooms = [-1]
    while books:
        s,e = heapq.heappop(books)
        e += 10
        if e % 100 >= 60:
            e += 40
            
        min_room = heapq.heappop(rooms)
        heapq.heappush(rooms, e)
        if s < min_room:
            heapq.heappush(rooms, min_room)
    
    return len(rooms)