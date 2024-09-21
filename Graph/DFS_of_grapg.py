V = 5
adj = [[2,3,1] , [0], [0,4], [0], [2]]

dfs_path = []
stack = []
visited = [False]*V

stack.append(0)
visited[0] = True

while stack:
    node = stack.pop(-1)
    dfs_path.append(node)
    for nighbor in adj[node]:
        if not visited[nighbor]:
            stack.append(nighbor)
            visited[nighbor] = True

print(dfs_path)

def dfs(v, visited, adj, path):
    visited[v] = True
    path.append(v)

    for neighbor in adj[v]:
        if not visited[neighbor]:
            dfs(neighbor, visited, adj, path)


V = 5
adj = [[2, 3, 1], [0], [0, 4], [0], [2]]
visited = [False] * V
path = []

dfs(0, visited, adj, path)

print("DFS path:", path)
