g={}
vis=[]
def pr(node):
    vis.append(node)
    print(node,end=' ')
    for child in g[node]:
        if(child not in vis):
            pr(child)

p=input().split()
n,e=map(int,p)
for _ in range(e):
    q=input().split()
    x,y=map(int,q)
    if x not in g:
        g[x]=[]
    if y not in g:
        g[y]=[]
    g[x].append(y)
    g[y].append(x)
pr(1)
