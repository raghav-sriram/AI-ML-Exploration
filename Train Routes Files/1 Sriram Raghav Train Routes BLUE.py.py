from math import pi , acos , sin , cos
import sys
from time import perf_counter
from time import sleep
from heapq import heappush, heappop, heapify
import tkinter as tk

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

def dijkstra(begin,goal,edges,rthing,cthing,edge):
    iter,s, bfr, num,delay,eta=(
        list(),
        set(),
        dict(),
        0,
        3,
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
        3,
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
start=perf_counter()


minimum_longitude, minimum_latitude=float('inf'),float('inf')
maximum_Latitude, maximum_Long=float('-inf'),float('-inf')
nd={}
with open("rrNodes.txt") as rrNodes:
    for x in rrNodes:
        latitudinal, longitudinal= (
            float(x.split(" ")[1]),
            float(x.split(" ")[2])
        )

        if (maximum_Long < longitudinal): maximum_Long=longitudinal
        if(maximum_Latitude <latitudinal): maximum_Latitude=latitudinal

        if(minimum_latitude>latitudinal): minimum_latitude=latitudinal
        if(minimum_longitude>  longitudinal): minimum_longitude=longitudinal


        temps = (latitudinal, longitudinal)
        nd[x.split(" ")[0]]=(temps[0], temps[1*0-1+2])

ed, edgeToLine = (
    dict(),
    dict()
)
tkrt = tk.Tk() # the root


tkcv = tk.Canvas(tkrt, width=800, bg='white', height=600)
tkcv.pack(expand=True)


with open("rrEdges.txt") as rrEdges:
    for rx in rrEdges:
        o,z = rx[:-1].split(" ")[1],rx[:-1].split(" ")[0]

        if not (z in ed): ed[z]=set()
        if not (o in ed): ed[o]=set()
        between=calcd(nd[z],nd[o])
        (lat1, long1)=nd[z]
        (twolatt, twolongg)=nd[o]
        y=500-1*(lat1-minimum_latitude+(50-abs(minimum_latitude-maximum_Latitude))/2)*10+50
        yy=500-(twolatt-minimum_latitude+(50-abs(minimum_latitude-maximum_Latitude))/2)*10+50
        x=1*(long1-minimum_longitude+(75-abs(maximum_Long-minimum_longitude))/2)*10+25
        xx=1*(twolongg-minimum_longitude+(75-abs(maximum_Long-minimum_longitude))/2)*10+25
        line=tkcv.create_line([(x,y),(xx,yy)],tags="edge")
        edgeToLine[(z,o)]=line
        ed[z].add((calcd(nd[z],nd[o]), o))
        ed[o].add((calcd(nd[z],nd[o]), z))

tkrt.update()

dic=dict()
with open("rrNodeCity.txt") as rrNodeCity: 
    for line in rrNodeCity: dic[line.split(" ",1)[1].strip()]=line.split(" ",1)[0]
print(f"Time to create data structure: {perf_counter()-start}")

startcity, destination= sys.argv[1], sys.argv[2]

def getLine(e, ndu, nd): return e[(nd, ndu)] if not ((ndu, nd) in e) else e[(ndu,nd)]
def reset(rthing,cthing,edge):
    b = "black"
    for e in edge.values(): cthing.itemconfig(e,width=1, fill=b)
    rthing.update()


count=perf_counter()
print(f"{startcity} to {destination} with Dijkstra: {dijkstra(dic[startcity],dic[destination],ed,tkrt,tkcv,edgeToLine)} in {perf_counter()-count} seconds.")
reset(tkrt, tkcv, edgeToLine)
count=perf_counter()
print(f"{startcity} to {destination} with A*: {astar(dic[startcity],dic[destination],ed, nd,tkrt,tkcv,edgeToLine)} in {perf_counter()-count} seconds.")
tkrt.mainloop()