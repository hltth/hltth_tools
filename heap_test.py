from heapq import heappush, heappop

tasks = []
heappush(tasks, (30, 'work out'))
heappush(tasks, (10, 'wake up'))
heappush(tasks, (15, 0xCAFFE))
heappush(tasks, (20, 'feed cat'))
heappush(tasks, (40, 'write book'))

while tasks:
    _,payload = heappop(tasks)
    print(payload)
