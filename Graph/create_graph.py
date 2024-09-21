N=3
edges = [{2,1}, {2,0}]

adj_list = [[] for _ in range(N)]

for edge in edges:
    u,v = edge
    adj_list[u].append(v)
    adj_list[v].append(u)

print(adj_list)
