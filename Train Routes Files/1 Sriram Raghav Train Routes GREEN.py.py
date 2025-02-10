from math import pi , acos , sin , cos
import sys
from time import perf_counter
from heapq import heappush, heappop, heapify

def calcd(node1, node2):
   # y1 = lat1, x1 = long1
   # y2 = lat2, x2 = long2
   # all assumed to be in decimal degrees
   y1, x1 = node1
   y2, x2 = node2

   R   = 3958.76 # miles = 6371 km
   y1 *= pi/180.0
   x1 *= pi/180.0
   y2 *= pi/180.0
   x2 *= pi/180.0

   # approximate great circle distance with law of cosines
   return acos( sin(y1)*sin(y2) + cos(y1)*cos(y2)*cos(x2-x1) ) * R
def dijkstra(begin,goal,edges):
    iter,s=(
        list(),
        set()
    )
    heappush(iter, (0,begin))

    
    while iter:
        (between, t) = (
            heappop(iter)
        )
        if goal == t: return between
        else:
            if not t in s:
                s.add(t)
                for k, v in edges[t]:
                    if not v in s: heappush(iter,(k+between,v))
    return None
def astar(begin,goal,edges,nodes):
    s, iter=   set(), list()
    beg = nodes[begin]
    go = nodes[goal]
    VAR = (calcd(beg,go),0,begin)
    heappush(iter, VAR)
    while iter:
        (_, between, t)=heappop(iter)
        if goal==t: return between
        else:
            if t not in s:
                s.add(t)
                for k, v in edges[t]:
                    if not v in s: heappush(iter,(calcd(nodes[v], nodes[goal])+between+k,between+k,v))
    return None
time=perf_counter()
nd=dict()
with open("rrNodes.txt") as rrNodes:
    for line in rrNodes:
        one, two = float(line.split(" ")[1]), float(line.split(" ")[2])
        nd[line.split(" ")[0]]=(one,two)


ed= {}
with open("rrEdges.txt") as rrEdges:
    for rE in rrEdges:
        o,z = rE[:-1].split(" ")[1],rE[:-1].split(" ")[0]
        if not (o in ed):
            # o = splitt[1]
            ed[o]=set()
        if not (z in ed):
            # z = splitt[0]
            ed[z]=set()
            
        dist=calcd(nd[z],nd[o])
        ed[z].add((dist, o))
        ed[o].add((dist, z))


dic= {}
with open("rrNodeCity.txt") as rrNodeCity:
    for r in rrNodeCity:
        red=r.split(" ",  1)
        dic[red[1].strip()]=red[0]

        
print(f"Time to create data structure: {perf_counter()-time}")
startcity, destination= sys.argv[1], sys.argv[2]
count=perf_counter()
print(f"{startcity} to {destination} with Dijkstra: {dijkstra(dic[startcity],dic[destination],ed)} in {perf_counter()-count} seconds.")
count=perf_counter()
print(f"{startcity} to {destination} with A*: {astar(dic[startcity],dic[destination],ed, nd)} in {perf_counter()-count} seconds.")