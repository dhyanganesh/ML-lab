import heapq

def astar(g,start,goal,h):
    front=[(0+h[start],start)]
    exp=set()
    cost={start:0}
    parent={start:None}
    
    while front:
        fcost,cur=heapq.heappop(front)
        
        if cur == goal:
            path=[]
            while cur is not None:
                path.append(cur)
                cur=parent[cur]
            path.reverse()
            return path,fcost
        
        exp.add(cur)
        for n,ncost in g[cur]:
            imcost=cost[cur]+ncost
            
            if n in exp and imcost >= cost.get(n,float('inf')):
                    continue
                    
            if n not in [data[1] for data in front] or imcost < cost.get(n,float('inf')):
                cost[n]=imcost
                parent[n]=cur
                heapq.heappush(front,(imcost+h[n],n))
    return None

graph={
    'A':[('B',2),('C',1)],
    'B':[('D',3)],
    'C':[('B',1),('D',5)],
    'D':[],
}

h={
    'A':10,
    'B':7,
    'C':5,
    'D':6,
}

start=input("enter the start node: ")
goal=input("enter the goal node: ")

result=astar(graph,start,goal,h)

if result is None:
    print(f'Path does not exists from {start} to {goal}')
else:
    print(f'The path from {start} to {goal} is',end=" : ")
    for i in range(len(result[0])):
        print(result[0][i],end=" -> ")
    print(f'with minimum cost {result[1]}')