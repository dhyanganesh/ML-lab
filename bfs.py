import heapq

def bfs(g,start,goal):
    front=[(0,start)]
    exp=set()
    
    while front:
        cost,cur=heapq.heappop(front)
        
        if cur == goal:
            return cost
        
        exp.add(cur)
        print(f'Explored node is {cur}')
        
        for n,ncost in g[cur]:
            if n not in exp and n not in [data[1] for data in front]:
                heapq.heappush(front,(cost+ncost,n))
                print(f"Added node {n} to front with cost {ncost}")
        
    return None

graph={ 'A':[('B',2),('C',1)],
        'B':[('D',3)],
        'C':[('D',5),('B',1)],
        'D':[],
      }

start=input("enter start node:")
goal=input("enter goal node:")

cost=bfs(graph,start,goal)

if cost is None:
    print(f'There is no path from {start} to {goal}')
else:
    print(f'Cost from {start} to {goal} is {cost}')
