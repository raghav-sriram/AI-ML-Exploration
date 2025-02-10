# Name: Pranav Elavarthi       Data: 10/7/22
from multiprocessing.heap import Heap
import random, pickle, math, time
from math import pi, acos, sin, cos
from tkinter import *
from xml.dom.minicompat import NodeList

class HeapPriorityQueue():
   # copy your PriorityQueue here
   def __init__(self):
      self.queue = ["dummy"]  # we do not use index 0 for easy index calulation
      self.current = 1        # to make this object iterable

   def next(self):            # define what _next_ does
      if self.current >=len(self.queue):
         self.current = 1     # to restart iteration later
         raise StopIteration
    
      out = self.queue[self.current]
      self.current += 1
   
      return out

   def __iter__(self):
      return self

   _next_ = next

   def isEmpty(self):
      return len(self.queue) == 1    # b/c index 0 is dummy

   def swap(self, a, b):
      self.queue[a], self.queue[b] = self.queue[b], self.queue[a]

   # Add a value to the heap_pq
   def push(self, value):
      self.queue.append(value)
      # write more code here to keep the min-heap property
      self.heapUp(len(self.queue) - 1)

   # helper method for push      
   def heapUp(self, k):
      parent = k // 2
      if(parent != 0 and self.queue[parent] > self.queue[k]):
         self.swap(k, parent)
         self.heapUp(parent)

   # helper method for reheap and pop
   def heapDown(self, k, size):
      left = k * 2
      right = k * 2 + 1
      if (left > size):
         return
      if (left == size):
         if (self.queue[k] > self.queue[left]):
            self.swap(k, left)
      else:
         min = left if (self.queue[left] <= self.queue[right]) else right
         if (self.queue[k] > self.queue[min]):
            self.swap(k, min)
            self.heapDown(min, size)
   
   # make the queue as a min-heap            
   def reheap(self):
      pq = HeapPriorityQueue()
      for val in self.queue:
         if val != "dummy":
            pq.push(val)
      self.queue = pq.queue
   
   # remove the min value (root of the heap)
   # return the removed value           
   def pop(self):
      return self.remove(1)
      
   # remove a value at the given index (assume index 0 is the root)
   # return the removed value   
   def remove(self, index):
      self.swap(index, len(self.queue)-1)
      temp = self.queue.pop()
      self.heapDown(index, len(self.queue)-1)
      return temp
   
def calc_edge_cost(y1, x1, y2, x2):
   #
   # y1 = lat1, x1 = long1
   # y2 = lat2, x2 = long2
   # all assumed to be in decimal degrees

   # if (and only if) the input is strings
   # use the following conversions

   y1  = float(y1)
   x1  = float(x1)
   y2  = float(y2)
   x2  = float(x2)
   #
   R   = 3958.76 # miles = 6371 km
   #
   y1 *= pi/180.0
   x1 *= pi/180.0
   y2 *= pi/180.0
   x2 *= pi/180.0
   #
   # approximate great circle distance with law of cosines
   #
   return acos( sin(y1)*sin(y2) + cos(y1)*cos(y2)*cos(x2-x1) ) * R

# NodeLocations, NodeToCity, CityToNode, Neighbors, EdgeCost
# Node: (lat, long) or (y, x), node: city, city: node, node: neighbors, (n1, n2): cost
def make_graph(nodes = "rrNodes.txt", node_city = "rrNodeCity.txt", edges = "rrEdges.txt"):
   nodeLoc, nodeToCity, cityToNode, neighbors, edgeCost = {}, {}, {}, {}, {}
   map = {}   # have screen coordinate for each node location

   # Your code goes here

   with open(nodes) as rrN:
      for line in rrN:
         line = line.strip().split(" ")
         nodeLoc[line[0]] = (line[1],line[2])

   with open(node_city) as rrnc:
      for line in rrnc:
         line = line.strip().split(" ")
         nodeToCity[line[0]] = " ".join(line[1:])
         cityToNode[" ".join(line[1:])] = line[0]

   with open(edges) as edj:
      for line in edj:
         nd1,nd2 = line.strip().split(" ")
         if nd1 in neighbors:
            neighbors[nd1].add(nd2)
         else:
            neighbors[nd1] = {nd2}
         if nd2 in neighbors:
            neighbors[nd2].add(nd1)
         else:
            neighbors[nd2] = {nd1}
         cost = calc_edge_cost(*nodeLoc[nd1], *nodeLoc[nd2])
         edgeCost[(nd1,nd2)] = cost
         edgeCost[(nd2,nd1)] = cost

   for node in nodeLoc: #checks each
      lat = float(nodeLoc[node][0]) #gets latitude
      long = float(nodeLoc[node][1]) #gets long
      modlat = (lat - 10)/60 #scales to 0-1
      modlong = (long+130)/70 #scales to 0-1
      map[node] = [modlat*800, modlong*1200] #scales to fit 800 1200
   
   return [nodeLoc, nodeToCity, cityToNode, neighbors, edgeCost, map]

# Retuen the direct distance from node1 to node2
# Use calc_edge_cost function.
def dist_heuristic(n1, n2, graph):
   # Your code goes here
   return calc_edge_cost(graph[0][n1][0], graph[0][n1][1], graph[0][n2][0], graph[0][n2][1])
   
# Create a city path. 
# Visit each node in the path. If the node has the city name, add the city name to the path.
# Example: ['Charlotte', 'Hermosillo', 'Mexicali', 'Los Angeles']
def display_path(path, graph):
   
   # Your code goes here
   print("The whole path ", path)
   print("The length of the whole path: ", len(path))
   li = []
   for node in path:
      if node in graph[1]:
         li.append(graph[1][node])
   print(li)

# Using the explored, make a path by climbing up to "s"
# This method may be used in your BFS and Bi-BFS algorithms.
def generate_path(state, explored, graph):
   path = [state]
   cost = 0
   while explored[state] != 's' and explored[state] != 'g':       #assume the parent of root is "s"
      cost += graph[4][(state, explored[state])]
      state = explored[state]
      path.append(state)
   return (path[::-1], cost)
   # Your code goes here

def drawLine(canvas, y1, x1, y2, x2, col):
   x1, y1, x2, y2 = float(x1), float(y1), float(x2), float(y2)   
   canvas.create_line(x1, 800-y1, x2, 800-y2, fill=col)

# Draw the final shortest path.
# Use drawLine function.
def draw_final_path(ROOT, canvas, path, graph, col='red'):
   
   # Your code goes here
   for i in range(len(path[1:])):
      drawLine(canvas, *graph[5][path[i]], *graph[5][path[i+1]],col)
   ROOT.update()

def draw_all_edges(ROOT, canvas, graph):
   ROOT.geometry("1200x800") #sets geometry
   canvas.pack(fill=BOTH, expand=1) #sets fill expand
   for n1, n2 in graph[4]:  #graph[4] keys are edge set
      drawLine(canvas, *graph[5][n1], *graph[5][n2], 'white') #graph[5] is map dict
   ROOT.update()

def bfs(start, goal, graph, col):
   ROOT = Tk() #creates new tkinter
   ROOT.title("BFS")
   canvas = Canvas(ROOT, background='black') #sets background
   draw_all_edges(ROOT, canvas, graph)

   counter = 0
   frontier, explored = [], {start: "s"}
   frontier.append(start)
   while frontier:
      s = frontier.pop(0)
      if s == goal: 
         path, cost = generate_path(s, explored, graph)
         draw_final_path(ROOT, canvas, path, graph)
         return path, cost
      for a in graph[3][s]:  #graph[3] is neighbors
         if a not in explored:
            explored[a] = s
            frontier.append(a)
            drawLine(canvas, *graph[5][s], *graph[5][a], col)
      counter += 1
      if counter % 1000 == 0: ROOT.update()
   return None

def bi_bfs(start, goal, graph, col):
   ROOT = Tk() #creates new tkinter
   ROOT.title("Bi-BFS")
   canvas = Canvas(ROOT, background='black') #sets background
   draw_all_edges(ROOT, canvas, graph)
   
   counter = 0
   if start == goal: return []
   # TODO 2: Bi-directional BFS Search
   # Your code goes here
   explored = {start:"s"}
   q = [start]
   explored2 = {goal:"g"}
   q2 = [goal]
   while len(q) != 0 and len(q2) !=0:
      a = q.pop(0)
      b = q2.pop(0)

      for c in graph[3][a]:
         if (c not in explored):
            q.append(c)
            explored[c] = a
         drawLine(canvas, *graph[5][a], *graph[5][c], col)
      for d in graph[3][b]:
         if (d not in explored2):
               q2.append(d)
               explored2[d] = b
         drawLine(canvas, *graph[5][b], *graph[5][d], col)
      
      counter += 1
      if counter % 1000 == 0: ROOT.update()
      
      pathcost = ()
      for thing in explored:
         if (thing in explored2):
            pathcost = (generate_path(thing,explored,graph)[0][0:-1] + generate_path(thing,explored2,graph)[0][::-1], generate_path(thing,explored,graph)[1] + generate_path(thing,explored2,graph)[1])
            draw_final_path(ROOT, canvas, pathcost[0], graph)
            return pathcost[0], pathcost[1]
   return None

def a_star(start, goal, graph, col, heuristic=dist_heuristic):
   ROOT = Tk() #creates new tkinter
   ROOT.title("A-Star")
   canvas = Canvas(ROOT, background='black') #sets background
   draw_all_edges(ROOT, canvas, graph)
   
   if start == goal: return []
   
   frontier = HeapPriorityQueue()
   explored = {start : 0}
   cost = 0
   frontier.push((heuristic(start,goal,graph), start, []))   
   counter = 0
   while frontier.isEmpty() == False:
      state = frontier.pop()
      if state[1] not in state[2]:
         path = state[2] + [state[1]]
         #cost += explored[state[1]]
         if state[1] == goal:
            draw_final_path(ROOT, canvas, path, graph)
            cost = explored[state[1]]
            return path, cost
         for a in graph[3][state[1]]:
            drawLine(canvas, *graph[5][state[1]], *graph[5][a], col)
            if a not in explored or (explored[state[1]] + graph[4][state[1],a] + heuristic(a,goal,graph) < explored[a]+heuristic(a,goal,graph)):
               explored[a] = explored[state[1]] + graph[4][state[1],a]
               frontier.push((explored[a] + heuristic(a,goal,graph), a, path))  
      counter += 1
      if counter % 1000 == 0: ROOT.update()
   return None

def bi_a_star(start, goal, graph, col, heuristic=dist_heuristic):
   ROOT = Tk() #creates new tkinter
   ROOT.title("Bi-A-Star")
   canvas = Canvas(ROOT, background='black') #sets background
   draw_all_edges(ROOT, canvas, graph)
   
   if start == goal: return []
   
   frontier = HeapPriorityQueue()
   frontier2 = HeapPriorityQueue()
   explored = {start : 0}
   explored2 = {goal : 0}
   frontier.push((heuristic(start,goal,graph), start, []))   
   frontier2.push((heuristic(goal,start,graph), goal, []))
   counter = 0
   while frontier.isEmpty() == False and frontier2.isEmpty() == False:
      state = frontier.pop()
      state2 = frontier2.pop()
      path = []
      path2 = []
      if state2[1] not in state2[2]:
         path2 = state2[2] + [state2[1]]
      if state[1] not in state[2]:
         path = state[2] + [state[1]]


      if state[1] in explored2 and state2[1] in explored:
         draw_final_path(ROOT,canvas, path + path2[::-1], graph)
         cost = explored[state[1]] + explored2[state2[1]]
         return path + path2[::-1], cost
      
      for a in graph[3][state[1]]:
            drawLine(canvas, *graph[5][state[1]], *graph[5][a], col)
            if a not in explored or (explored[state[1]] + graph[4][state[1],a] + heuristic(a,goal,graph) < explored[a]+heuristic(a,goal,graph)):
               explored[a] = explored[state[1]] + graph[4][state[1],a]
               frontier.push((explored[a] + heuristic(a,goal,graph), a, path))  

      for a in graph[3][state2[1]]:
            drawLine(canvas, *graph[5][state2[1]], *graph[5][a], col)
            if a not in explored2 or (explored2[state2[1]] + graph[4][state2[1],a] + heuristic(a,start,graph) < explored2[a]+heuristic(a,start,graph)):
               explored2[a] = explored2[state2[1]] + graph[4][state2[1],a]
               frontier2.push((explored2[a] + heuristic(a,start,graph), a, path2))  
 

      counter += 1
      if counter % 1000 == 0: ROOT.update()
   return None
   

def tri_directional(city1, city2, city3, graph, col, heuristic=dist_heuristic):

   # Your code goes here
   ROOT = Tk() #creates new tkinter
   ROOT.title("Tri-A-Star")
   canvas = Canvas(ROOT, background='black') #sets background
   draw_all_edges(ROOT, canvas, graph)
   
   pathab, costab = tri_helper(city1, city2, graph, col, ROOT, canvas, heuristic)
   pathbc, costbc = tri_helper(city2, city3, graph, col, ROOT, canvas, heuristic)
   pathac, costac = tri_helper(city1, city3, graph, col, ROOT, canvas, heuristic)
   finc, finp = min([(costab+costbc, pathab+pathbc), (costbc+costac, pathbc+pathac[::-1]), (costac+costab, pathac[::-1]+pathab)])
   draw_final_path(ROOT, canvas, finp, graph)

   return finp, finc

def tri_helper(start, goal, graph, col, root, canvas, heuristic=dist_heuristic):
   if start == goal: return []
   
   frontier = HeapPriorityQueue()
   frontier2 = HeapPriorityQueue()
   explored = {start : 0}
   explored2 = {goal : 0}
   frontier.push((heuristic(start,goal,graph), start, []))   
   frontier2.push((heuristic(goal,start,graph), goal, []))
   counter = 0
   while frontier.isEmpty() == False and frontier2.isEmpty() == False:
      state = frontier.pop()
      state2 = frontier2.pop()
      path = []
      path2 = []
      if state2[1] not in state2[2]:
         path2 = state2[2] + [state2[1]]
      if state[1] not in state[2]:
         path = state[2] + [state[1]]


      if state[1] in explored2 and state2[1] in explored:
         cost = explored[state[1]] + explored2[state2[1]]
         return path + path2[::-1], cost
      
      for a in graph[3][state[1]]:
            drawLine(canvas, *graph[5][state[1]], *graph[5][a], col)
            if a not in explored or (explored[state[1]] + graph[4][state[1],a] + heuristic(a,goal,graph) < explored[a]+heuristic(a,goal,graph)):
               explored[a] = explored[state[1]] + graph[4][state[1],a]
               frontier.push((explored[a] + heuristic(a,goal,graph), a, path))  

      for a in graph[3][state2[1]]:
            drawLine(canvas, *graph[5][state2[1]], *graph[5][a], col)
            if a not in explored2 or (explored2[state2[1]] + graph[4][state2[1],a] + heuristic(a,start,graph) < explored2[a]+heuristic(a,start,graph)):
               explored2[a] = explored2[state2[1]] + graph[4][state2[1],a]
               frontier2.push((explored2[a] + heuristic(a,start,graph), a, path2))  
 

      counter += 1
      if counter % 1000 == 0: root.update()
   return None

def main():
   start, goal = input("Start city: "), input("Goal city: ")
   third = input("Third city for tri-directional: ")
   graph = make_graph("rrNodes.txt", "rrNodeCity.txt", "rrEdges.txt")  # Task 1
   
   """

   cur_time = time.time()
   path, cost = bfs(graph[2][start], graph[2][goal], graph, 'yellow') #graph[2] is city to node
   if path != None: display_path(path, graph)
   else: print ("No Path Found.")
   print ('BFS Path Cost:', cost)
   print ('BFS duration:', (time.time() - cur_time))
   print ()
   
   cur_time = time.time()
   path, cost = bi_bfs(graph[2][start], graph[2][goal], graph, 'green')
   if path != None: display_path(path, graph)
   else: print ("No Path Found.")
   print ('Bi-BFS Path Cost:', cost)
   print ('Bi-BFS duration:', (time.time() - cur_time))
   print ()
   
   
   cur_time = time.time()
   path, cost = a_star(graph[2][start], graph[2][goal], graph, 'blue')
   if path != None: display_path(path, graph)
   else: print ("No Path Found.")
   print ('A star Path Cost:', cost)
   print ('A star duration:', (time.time() - cur_time))
   print ()
   
   """
   
   cur_time = time.time()
   path, cost = bi_a_star(graph[2][start], graph[2][goal], graph, 'orange')
   if path != None: display_path(path, graph)
   else: print ("No Path Found.")
   print ('Bi-A star Path Cost:', cost)
   print ("Bi-A star duration: ", (time.time() - cur_time))
   print ()
   
   print ("Tri-Search of ({}, {}, {})".format(start, goal, third))
   cur_time = time.time()
   path, cost = tri_directional(graph[2][start], graph[2][goal], graph[2][third], graph, 'pink')
   if path != None: display_path(path, graph)
   else: print ("No Path Found.")
   print ('Tri-A star Path Cost:', cost)
   print ("Tri-directional search duration:", (time.time() - cur_time))
   
   mainloop() # Let TK windows stay still
if __name__ == '__main__':
   main()


''' Sample output
 ----jGRASP exec: python Lab10_railroad_Kim_2019_2020.py
Start city: Charlotte
Goal city: Los Angeles
Third city for tri-directional: Chicago
The number of explored nodes of BFS: 19735
The whole path: ['3700421', '3700258', '3700256', '3700004', '3700076', '3700075', '0000530', '4500272', '4500042', '4500270', '4500231', '4500069', '4500023', '4500233', '4500094', '4500095', '4500096', '4500097', '4500234', '4500225', '4500104', '4500082', '4500164', '4500015', '4500181', '4500167', '0000533', '1300133', '1300197', '1300132', '1300146', '1300198', '1300204', '1300208', '1300087', '1300279', '1300088', '1300369', '1300459', '1300458', '1300090', '1300460', '1300107', '1300210', '1300398', '1300099', '0000031', '0100343', '0100342', '0100341', '0100084', '0100506', '0100012', '0100325', '0100345', '0100331', '0100520', '0100354', '0100355', '0100042', '0100566', '0100356', '0100357', '0100456', '0100103', '0100515', '0100264', '0100032', '0100263', '0100102', '0100033', '0100062', '0100129', '0100513', '0100061', '0000461', '2800154', '2800153', '2800032', '2800150', '2800031', '2800108', '2800247', '2800191', '2800156', '2800169', '2800001', '2800162', '2800163', '2800164', '2800125', '2800030', '2800028', '0000419', '2200078', '2200143', '2200039', '2200274', '2200379', '2200080', '2200273', '2200205', '2200112', '2200037', '2200076', '2200311', '0000411', '0500250', '0500019', '0500248', '0500005', '0500020', '0500134', '0000573', '4800439', '4800085', '4800410', '4801165', '4800956', '4801086', '4800081', '4800584', '4800082', '4800084', '4800309', '4800898', '4801101', '4800271', '4800578', '4800274', '4800881', '4800882', '4800167', '4800483', '4800464', '4800168', '4801228', '4800170', '4801230', '4800172', '4800462', '4800461', '4800230', '4800199', '4800832', '4800831', '4800198', '4801190', '4800830', '4800197', '4800200', '4800302', '4800648', '4800763', '4800286', '4800759', '4800758', '4800649', '4800675', '4801214', '4800285', '4800674', '4800757', '4800673', '4800672', '4800535', '4800280', '4800279', '4801134', '4800896', '4800357', '0009483', '9100020', '9100502', '9100501', '9100505', '9100507', '9100504', '9100503', '9100515', '9100153', '9100122', '9100478', '9100448', '9100442', '9100477', '9100476', '9100479', '9100436', '9100124', '9100150', '9100427', '9100012', '9100485', '9100484', '9100081', '9100486', '9100007', '9100117', '9100006', '9100116', '9100080', '9100438', '9100001', '0009063', '0600129', '0600577', '0600041', '0600579', '0600117', '0600039', '0600646', '0600797', '0600747', '0600516', '0600750', '0600584', '0600746', '0600585', '0600586', '0600042', '0600770', '0600434', '0600689', '0600464', '0600688', '0600384', '0600588', '0600460', '0600408', '0600799', '0600402', '0600766', '0600686', '0600079', '0600080', '0600086', '0600684', '0600425', '0600088', '0600759', '0600427', '0600316']
The length of the whole path: 243
['Charlotte', 'Hermosillo', 'Mexicali', 'Los Angeles']
BFS Path Cost: 2965.7640233572088
BFS duration: 288.9429421424866

The number of explored nodes of Bi-BFS: 12714
The whole path: ['3700421', '3700258', '3700256', '3700004', '3700076', '3700075', '0000530', '4500272', '4500042', '4500270', '4500231', '4500069', '4500023', '4500233', '4500094', '4500095', '4500096', '4500097', '4500234', '4500225', '4500104', '4500082', '4500164', '4500015', '4500181', '4500167', '0000533', '1300133', '1300197', '1300132', '1300146', '1300198', '1300204', '1300208', '1300087', '1300279', '1300088', '13003
'''