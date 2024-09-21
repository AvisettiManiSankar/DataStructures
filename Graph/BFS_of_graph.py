# By list used as queue
V = 5
adj = [{1,2,3},{2},{4},{},{}]

visited = [False]*V
bfs_path = []

queue = []
queue.append(0)
visited[0] = True

while queue:
    node = queue.pop(0)
    bfs_path.append(node)
    for neighbor in adj[node]:
        if not visited[neighbor]:
            queue.append(neighbor)
            visited[neighbor] = True

print(bfs_path)


# By queue
from queue import Queue
V = 5
adj = [{1,2,3},{2},{4},{},{}]
visited = [False]*V
bfs_path = []

queue = Queue()
queue.put(0)
visited[0] = True

while not queue.empty():
    node = queue.get()
    bfs_path.append(node)
    for neighbor in adj[node]:
        if not visited[neighbor]:
            queue.put(neighbor)
            visited[neighbor] = True

print(bfs_path)

from collections import deque
V = 5
adj = [{1,2,3},{2},{4},{},{}]
visited = [False]*V
bfs_path = []

queue = deque()
queue.append(0)
visited[0] = True

while queue:
    node = queue.popleft()
    bfs_path.append(node)
    for neighbor in adj[node]:
        if not visited[neighbor]:
            queue.append(neighbor)
            visited[neighbor] = True

print(bfs_path)