n, m, s = map(int, input().split())
adj =  {}
for i in range(n+1):
   adj[i] = set()
for _ in range(m):
   a, b = map(int, input().split())
   adj[a].add(b)
   adj[b].add(a)

# DFS
stack = [s]
chk = set()
while stack:
   v = stack.pop()
   if v in chk: continue
   print(v, end=' ')
   chk.add(v)
   for u in sorted(adj[v], reverse=True):
      stack.append(u)
print()

#BFS
que = [s]
chk = set()
chk.add(s)
print(s,end=' ')
while que:
   v = que.pop(0)
   for u in sorted(adj[v]):
      if u in chk : continue
      print(u,end=' ')
      que.append(u)
      chk.add(u)
print()