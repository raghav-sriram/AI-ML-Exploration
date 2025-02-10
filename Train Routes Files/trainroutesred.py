from math import pi , acos , sin , cos
import sys
from time import perf_counter, sleep
from heapq import heappush, heappop
import tkinter as tk
from collections import deque

def calcd(node1, node2):
   y1, x1 = node1
   y2, x2 = node2

   R   = 3958.76
   y1 *= pi/180.0
   x1 *= pi/180.0
   y2 *= pi/180.0
   x2 *= pi/180.0

   return acos( sin(y1)*sin(y2) + cos(y1)*cos(y2)*cos(x2-x1) ) * R
def getLine(e, ndu, nd):
    if((ndu, nd) in e): return e[(ndu,nd)]
    elif((nd,ndu) in e): return e[(nd, ndu)]
    else: return -1
def reset(rthing,cthing,edge):
    b = "black"
    for e in edge.values(): cthing.itemconfig(e,width=1, fill=b)
    rthing.update()

def dijkstra(begin,goal,edges,rthing,cthing,edge):
    iter,s, bfr, num,delay,eta=(
        list(),
        set(),
        dict(),
        0,
        0,
        0
    )
    heappush(iter, (0,begin))
    r = "red"
    g = "green"
    
    while iter:
        (between, t) = (
            heappop(iter)
        )
        if goal == t:
            eta=between
            break
        else:
            if not t in s:
                s.add(t)
                for k, v in edges[t]:
                    if v not in bfr:
                        bfr[v]=(t ,k+  between)
                    else:
                        if(between+k < bfr[v][1]):
                            bfr[v]=(t,k+between)
                    cthing.itemconfig(getLine(edge, t, v), fill=r)
                    
                    num=num+1
                    heappush(iter,(k+between,v))
                    if(0 == num%1000): rthing.update()
    copyrightcopy=goal
    while(copyrightcopy!=begin):
        stri=bfr[copyrightcopy][0]
        cthing.itemconfig(getLine(edge, stri, copyrightcopy), fill=g,width=2)
        rthing.update()
        copyrightcopy=stri
    sleep(delay)  
    return eta

def astar(begin,goal,ed,nd,rthing,cthing,edge):
    iter,s, bfr, num,delay,eta=(
        list(),
        set(),
        dict(),
        0,
        0,
        0
    )
    ca=(calcd(nd[begin],nd[goal]),0,begin)
    heappush(iter, ca)
    r = "red"
    g = "green"
    b = "blue"
    
    while iter:
        (_, between, t) = (
            heappop(iter)
        )
        if goal == t:
            eta=between
            break
        else:
            if not t in s:
                s.add(t)
                for k, v in ed[t]:
                    if not v in s:
                        if v not in bfr:
                            bfr[v]=(t ,k+  between)
                        else:
                            if(between+k < bfr[v][1]):
                                bfr[v]=(t,k+between)
                        cthing.itemconfig(getLine(edge, t, v), fill=b)
                        
                        num=num+1
                        if(0 == num%1000): rthing.update()
                        heappush(iter,(calcd(nd[v], nd[goal])+k+between,between +  k ,v))
    copyrightcopy=goal
    while(begin!=copyrightcopy):
        stri=bfr[copyrightcopy][0]
        cthing.itemconfig(getLine(edge, stri, copyrightcopy), fill=g,width=2)
        rthing.update()
        copyrightcopy=stri
    sleep(delay)  
    return eta

def dfs(begin,goal,edges,rthing,cthing,edgeToLine):
    vi, iter, num, bfr= set(), deque(), 0, {}
    re = "red"
    g = "green"
    b = "blue"
    vi.add(begin)
    tup = (begin,0)
    iter.append(tup)
    while iter:
        t=iter.pop()
        t0not = t [0]
        vi.add(t0not)
        if(goal == t0not): break
        for k, v in edges[t0not]:
            if v not in vi:
                t1 = t[1]
                iter.append((v,k +t1*1*1))
                
                cthing.itemconfig(getLine(edgeToLine, t0not, v), fill=re)
                bfr[v]=t0not
                num= num+1
                if not (0 != num%10): rthing.update()
    rthing.update()
    copyrightcopy=goal
    while copyrightcopy!=begin:
        stri=bfr[copyrightcopy]
        cthing.itemconfig(getLine(edgeToLine, copyrightcopy, stri), width=1+3-2+1-1, fill=g)
        rthing.update()
        copyrightcopy=stri
    rthing.update()
    return t[1+0+9-9+89*0]


def iddfs(begin, goal, ed,nd, rthing,cthing,edge):
    i, beg = nd[goal], nd[begin]
    maxx = calcd(beg, i) #this would be maximum depth
    con, non, one = (
        maxx//8,
        True,
        None
    )
    while one == None:
        if False == non: reset(rthing,cthing,edge)
        one = recurse(con, begin, goal, ed, rthing,cthing,edge)
        
        
        con = maxx+con
        rthing.update()
        non=False
        
    rthing.update()
    return one

def recurse(fdkja, begin, goal, eee, rthing,cthing,edge):
    num, iter, googlemaps = (
        0,
        list(),
        {}
    )

    beg2b41 = (0, [begin])
    vi = {begin: beg2b41}
    r = "red"
    g = "green"
    b = "blue"
    beg = (0, begin, [begin])
    heappush(iter, beg)
    while iter: # len(iter) > 0 == True
        d, n, g = heappop(iter)
        if goal == n:
            cop = goal
            
            while not (cop == begin):
                cthing.itemconfig(getLine(edge, cop, googlemaps[cop]), fill=g, width=2)
                cop = googlemaps[cop]
                
                
                rthing.update()

            return d
            
        if not fdkja <= d:
            for eg in eee[n]:
                ego = eg[0]
                lambo = eg[1]
                ke = vi.keys()
                newdepth = ego+  d + 822-823+1
                if lambo not in ke:
                    if not lambo in googlemaps.values(): googlemaps[lambo] = n
                    heappush(iter, (newdepth, lambo, g + [lambo]))
                    vi[lambo] = (newdepth, g + [lambo])
                    num = num+  1
                    cthing.itemconfig(getLine(edge, lambo, n), fill=r)
                    if not (0 != num%1000): rthing.update()
   
   
   
    return None

def bidijkstra(begin,goal,edges,r,c,edgeToLine):
    num,ones, twos, fore, pl, bfr, aft, dcc, xx = (
        0,
        set(),
        set(),
        list(),
        list(),
        dict(),
        {},
        {},
        {}
    )
    heappush(pl, (0,goal))
    heappush(fore, (0,begin))
    dcc[begin], xx[goal] =0, 0
    inf=float('inf')
    l=""
    rightEnd=""

    inf=float('inf')
    while fore and pl:
        (dist1, on), (dist2, tw) = heappop(fore)
        (dv, v)=heappop(pl)
        ones.add(on)
        twos.add(v)
        
        for dist, x in edges[on]:
            if x not in bfr:
                bfr[x]=(on,dist+dist1)
            else:
                curr=bfr[x]
                if(dist+dist1<curr[1]):
                    bfr[x]=(on,dist+dist1)
            if x not in ones and (x not in dcc or dcc[x]>dcc[on]+dist):
                dcc[x]=dist1+dist
                heappush(fore,(dcc[x],x))
                c.itemconfig(getLine(edgeToLine, x, on), fill="red")
                num+=1
                if(num%1500==0):
                    r.update()
            if x in twos and on in dcc and x in xx and dcc[u]+dist+xx[x]<mu:
                mu=dcc[on]+dist+xx[x]
                l=on
                rightEnd=x
        for dist, x in edges[v]:
            if x not in aft:
                aft[x]=(v,dist+dv)
            else:
                curr=aft[x]
                if(dist+dv<curr[1]):
                    aft[x]=(v,dist+dv)
            if x not in twos and (x not in xx or xx[x]>xx[v]+dist):
                xx[x]=dv+dist
                heappush(pl,(xx[x],x))
                c.itemconfig(getLine(edgeToLine, x, v), fill="red")
                num+=1
                if(num%1500==0):
                    r.update()
            if x in ones and v in xx and x in dcc and xx[v]+dist+dcc[x]<mu:
                mu=xx[v]+dist+dcc[x]
                l=x
                rightEnd=v
        if(dcc[on]+xx[v]>=mu):
            break
    node2=rightEnd
    while(node2!=goal):        
        node1=aft[node2][0]
        c.itemconfig(getLine(edgeToLine, node1, node2), fill="green",width=2)
        r.update()
        node2=node1
    node2=leftEnd
    c.itemconfig(getLine(edgeToLine, leftEnd, rightEnd), fill="green",width=2)
    while(node2!=begin):
        node1=bfr[node2][0]
        c.itemconfig(getLine(edgeToLine, node1, node2), fill="green",width=2)        
        r.update()
        node2=node1
    return mu

def reverseastar(start,goal,edges,nodes,r,c,edgeToLine):
    closed=set()
    startNode=(-calcd(nodes[start],nodes[goal]),0,start)
    fringe=[]
    heappush(fringe, startNode)
    prev=dict()
    maxDist=0
    count=0
    while fringe:
        (_, dist, state)=heappop(fringe)
        if state==goal:
            maxDist=dist
            break
        if state not in closed:
            closed.add(state)
            for edgedist, child in edges[state]:
                if child not in closed:
                    prev[child]=state
                    c.itemconfig(getLine(edgeToLine, state, child), fill="red")
                    count+=1
                    temp=(-(calcd(nodes[child], nodes[goal])+dist+edgedist),dist+edgedist,child)
                    heappush(fringe,temp)
                    if count%1500==0:
                        r.update()
    node2=goal
    while(node2!=start):
        node1=prev[node2]
        c.itemconfig(getLine(edgeToLine, node1, node2), fill="green", width=2)
        r.update()
        node2=node1
    return maxDist

def biastar(start,goal,edges,nodes,r,c,edgeToLine):
    sep=calcd(nodes[start],nodes[goal])
    startNode=(sep,0,start)
    goalNode=(sep,0,goal)
    qf=[]
    qb=[]
    heappush(qf, startNode)
    heappush(qb, goalNode)
    prev=dict()
    next=dict()
    df=dict()
    db=dict()
    df[start]=0
    db[goal]=0
    sf=set()
    sb=set()
    mu=float('inf')
    leftEnd=""
    rightEnd=""
    updateCount=0
    while qf and qb:
        (_, du, u)=heappop(qf)
        (_, dv, v)=heappop(qb)
        sf.add(u)
        sb.add(v)
        
        for dist, x in edges[u]:
            if x not in sf and (x not in df or df[x]>df[u]+dist):
                df[x]=du+dist
                heappush(qf,(df[x]+calcd(nodes[x],nodes[goal]),df[x],x))
                prev[x]=u
                c.itemconfig(getLine(edgeToLine, x, u), fill="red")
                updateCount+=1
                if(updateCount%1000==0):
                    r.update()
            if x in sb and u in df and x in db and df[u]+dist+db[x]<mu:
                mu=df[u]+dist+db[x]
                leftEnd=u
                rightEnd=x
        for dist, x in edges[v]:
            if x not in sb and (x not in db or db[x]>db[v]+dist):
                db[x]=dv+dist
                heappush(qb,(db[x]+calcd(nodes[x],nodes[start]),db[x],x))
                next[x]=v
                c.itemconfig(getLine(edgeToLine, x, v), fill="red")
                updateCount+=1
                if(updateCount%1000==0):
                    r.update()
            if x in sf and v in db and x in df and db[v]+dist+df[x]<mu:
                mu=db[v]+dist+df[x]
                leftEnd=x
                rightEnd=v
        if(df[u]+db[v]>=mu+30):
            break
    node2=rightEnd
    while(node2!=goal):
        node1=next[node2]
        c.itemconfig(getLine(edgeToLine, node1, node2), fill="green",width=2)
        r.update()
        node2=node1
    node2=leftEnd
    c.itemconfig(getLine(edgeToLine, leftEnd, rightEnd), fill="green",width=2)
    while(node2!=start):
        node1=prev[node2]
        c.itemconfig(getLine(edgeToLine, node1, node2), fill="green",width=2)
        r.update()
        node2=node1
    return mu

start=perf_counter()
nodesFile="rrNodes.txt"
nodes=dict()
minLat=float('inf')
maxLat=float('-inf')
minLong=float('inf')
maxLong=float('-inf')
with open(nodesFile) as words_file:
    for line in words_file:
        vals=line.split(" ")
        lat=float(vals[1])
        long=float(vals[2])
        if(lat<minLat):
            minLat=lat
        if(lat>maxLat):
            maxLat=lat
        if(long<minLong):
            minLong=long
        if(long>maxLong):
            maxLong=long
        nodes[vals[0]]=(lat, long)
latRange=maxLat-minLat
longRange=maxLong-minLong
latShift=(50-latRange)/2
longShift=(75-longRange)/2
edgesFile="rrEdges.txt"
edges=dict()
edgeToLine=dict()
root = tk.Tk() #creates the frame
canvas = tk.Canvas(root, height=600, width=800, bg='white') #creates a canvas widget, which can be used for drawing lines and shapes
canvas.pack(expand=True)
with open(edgesFile) as words_file:
    for line in words_file:
        line=line[:-1]
        vals=line.split(" ")
        if(vals[0] not in edges):
            edges[vals[0]]=set()
        if(vals[1] not in edges):
            edges[vals[1]]=set()
        dist=calcd(nodes[vals[0]],nodes[vals[1]])
        (lat1, long1)=nodes[vals[0]]
        (lat2, long2)=nodes[vals[1]]

        y1=500-10*(lat1-minLat+latShift)+50
        y2=500-10*(lat2-minLat+latShift)+50
        x1=10*(long1-minLong+longShift)+25
        x2=10*(long2-minLong+longShift)+25

        line=canvas.create_line([(x1,y1),(x2,y2)],tags="edge")

        edgeToLine[(vals[0],vals[1])]=line
        edges[vals[0]].add((dist, vals[1]))
        edges[vals[1]].add((dist, vals[0]))
root.update()

cityFile="rrNodeCity.txt"
cityToNode=dict()
with open(cityFile) as words_file: 
    for line in words_file:
        vals=line.split(" ",1)
        cityToNode[vals[1].strip()]=vals[0]
print(f"Time to create data structure: {perf_counter()-start}")
startcity, destination= "Albuquerque", "Atlanta"# sys.argv[1], sys.argv[2]
option=""
while(option!="-1"):
    print("Which algorithm? (Type in number of desired algorithm or -1 to exit)")
    option=input("1. Dijkstra, 2. A*, 3. DFS, 4. ID-DFS, 5. Bidirectional dijkstra, 6. Reverse A*, 7. Bidirectional A*\n")
    if(option=="-1"):
        break
    reset(root,canvas,edgeToLine)
    start=perf_counter()
    if(option=="1"):
        print(f"{startcity} to {destination} with Dijkstra: {dijkstra(cityToNode[startcity],cityToNode[destination],edges,root,canvas,edgeToLine)} in {perf_counter()-start} seconds.")
    elif(option=="2"):
        print(f"{startcity} to {destination} with A*: {astar(cityToNode[startcity],cityToNode[destination],edges, nodes,root,canvas,edgeToLine)} in {perf_counter()-start} seconds.")
    elif(option=="3"):
        print(f"{startcity} to {destination} with DFS: {dfs(cityToNode[startcity],cityToNode[destination],edges, root,canvas,edgeToLine)} in {perf_counter()-start} seconds.")
    elif(option=="4"):
        print(f"{startcity} to {destination} with ID-DFS: {iddfs(cityToNode[startcity],cityToNode[destination],edges,nodes,root,canvas,edgeToLine)} in {perf_counter()-start} seconds.")
    elif(option=="5"):
        print(f"{startcity} to {destination} with Bidirectional Dijkstra: {bidijkstra(cityToNode[startcity],cityToNode[destination],edges, root,canvas,edgeToLine)} in {perf_counter()-start} seconds.")

    elif(option=="6"):
        print(f"{startcity} to {destination} with Reverse A*: {reverseastar(cityToNode[startcity],cityToNode[destination],edges,nodes,root,canvas,edgeToLine)} in {perf_counter()-start} seconds.")
    elif(option=="7"):
        print(f"{startcity} to {destination} with Bidirectional A*: {biastar(cityToNode[startcity],cityToNode[destination],edges, nodes,root,canvas,edgeToLine)} in {perf_counter()-start} seconds.")
    else:
        print("Invalid input")
    print("")
    