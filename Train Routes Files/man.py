# Manav Gagvani
# 12/8/22
import sys
from time import perf_counter, sleep
from math import pi, acos, sin, cos
from heapq import heappush, heappop, _heappop_max
from tkinter import *
from tkinter import messagebox


# Globals used for GUI
START = None
DEST = None
SEARCH = None
MODE = "Dark"
SPEED = 10


def calcd(y1, x1, y2, x2):
    """'
    y1 = lat1, x1 = long1
    y2 = lat2, x2 = long2
    all assumed to be in decimal degrees
    """
    y1 = float(y1)
    x1 = float(x1)
    y2 = float(y2)
    x2 = float(x2)
    R = 3958.76  # miles = 6371 km
    y1 *= pi / 180.0
    x1 *= pi / 180.0
    y2 *= pi / 180.0
    x2 *= pi / 180.0
    # approximate great circle distance with law of cosines
    return acos(sin(y1) * sin(y2) + cos(y1) * cos(y2) * cos(x2 - x1)) * R


def make_graph(
    nodes="rrNodes.txt", node_city="rrNodeCity.txt", edges="rrEdges.txt"
):  # default args
    nodeLoc, nodeToCity, cityToNode, neighbors, edgeCost = {}, {}, {}, {}, {}
    map = {} 
    _len = len

    with open(nodes, "r") as file1:  # reads in the node locations with node IDs
        for line1 in file1:
            line_array = line1.strip().split(" ")
            nodeLoc[line_array[0]] = [line_array[1], line_array[2]]
    with open(node_city, "r") as file2:  # reads in the city names
        for line2 in file2:
            line_array = line2.strip().split(" ")
            if _len(line_array) == 3:  # if there is a space in the city name
                cityToNode[line_array[1] + " " + line_array[2]] = line_array[0]
                nodeToCity[line_array[0]] = line_array[1] + " " + line_array[2]
            else:
                cityToNode[line_array[1].strip()] = line_array[0]
                nodeToCity[line_array[0]] = line_array[1].strip()
    with open(edges, "r") as file3:
        for line3 in file3:
            line_array = line3.strip().split(" ")
            temp1 = nodeLoc[line_array[0]]  # first node
            temp2 = nodeLoc[line_array[1]]  # second node
            r1 = line_array[0]
            r2 = line_array[1]
            if r1 not in neighbors:
                neighbors[r1] = {
                    r2
                }  # instantiates a dict with the first node as the key and the second node as the value
            else:
                neighbors[r1].add(r2)  # add to the adjacency list
            if r2 not in neighbors:
                neighbors[r2] = {r1}
            else:
                neighbors[r2].add(r1)
            edgeCost[(r1, r2)] = calcd(
                temp1[0], temp1[1], temp2[0], temp2[1]
            )  # tuple is key of edgeCost dict
            edgeCost[(r2, r1)] = calcd(temp1[0], temp1[1], temp2[0], temp2[1])
    line_array = []
    with open("north_america_boundaries.txt", "r") as file4:
        for line4 in file4:
            line_array.append(line4.strip().split(" "))
    line_polys = [[]]
    for line in line_array:
        if line[0] != "":
            line_polys[-1].append([float(line[0]), float(line[1])])
        else:
            pass
            # line_polys.append([])
    for a in neighbors:
        for b in neighbors[a]:
            edgeCost[(a, b)] = calcd(
                nodeLoc[a][0], nodeLoc[a][1], nodeLoc[b][0], nodeLoc[b][1]
            )
            edgeCost[(b, a)] = calcd(
                nodeLoc[a][0], nodeLoc[a][1], nodeLoc[b][0], nodeLoc[b][1]
            )
    map_polys = []
    for poly in line_polys:
        map_polys.append([])
        for point in poly:
            point[0] = ((point[0] - 10) / 60) * 800
            point[1] = ((point[1] + 130) / 70) * 1200
            map_polys[-1].append(point[0])
            map_polys[-1].append(point[1])
    for node in nodeLoc:  # checks each
        lat = float(nodeLoc[node][0])  # gets latitude
        long = float(nodeLoc[node][1])  # gets longitude
        modlat = (lat - 10) / 60  # scales to 0-1
        modlong = (long + 130) / 70  # scales to 0-1
        map[node] = [modlat * 800.0, modlong * 1200.0]  # scales to fit 800 x 1200 window
    return [nodeLoc, nodeToCity, cityToNode, neighbors, edgeCost, map, map_polys]


def dist_heuristic(n1, n2, graph):
    return calcd(graph[0][n1][0], graph[0][n1][1], graph[0][n2][0], graph[0][n2][1])

def draw_line(canvas, y1, x1, y2, x2, col, line_width=1):
    x1, y1, x2, y2 = float(x1), float(y1), float(x2), float(y2)
    try:
        canvas.create_line(x1, 800 - y1, x2, 800 - y2, fill=col, width=line_width)
    except Exception as e:
        print("Tkinter error: ")
        print(e)
        sys.exit(1)

def draw_line_out(canvas, y1, x1, y2, x2, col, line_width=1):
    '''
    draws line w/ overdraw to prevent weird artifacts
    '''
    x1, y1, x2, y2 = float(x1), float(y1), float(x2), float(y2)
    try:
        # if MODE == "dark":
        #     canvas.create_rectangle(x1, y1, x2, y2, fill='black', outline='black')
        # else:
        #     canvas.create_rectangle(x1, y1, x2, y2, fill='white', outline='white')
        id = canvas.create_line(x1, 800 - y1, x2, 800 - y2, fill=col, width=line_width)
        return id
    except Exception as e:
        print("Tkinter error: ")
        print(e)
        sys.exit(1)


def draw_final_path(ROOT, canvas, path, graph, col="green"):
    # print(path)
    for p in range(len(path) - 1):
        draw_line(canvas, *graph[5][path[p]], *graph[5][path[p + 1]], col, 5)
        ROOT.update()
    sleep(5) # pause for 5 sec
    ROOT.destroy() # close the window

# draws all edges and returns canvas ids corresponding with edges
def draw_all_edges_out(ROOT, canvas, graph, color="white"):
    ROOT.geometry("1200x800")  # sets geometry
    counter = 0
    edge2id = {}
    canvas.pack(fill=BOTH, expand=1)  # sets fill expand
    for n1, n2 in graph[4]:  # graph[4] keys are edge set
        # print(n1, n2, graph[4][(n1, n2)])
        edge2id[(n1, n2)] = draw_line_out(canvas, *graph[5][n1], *graph[5][n2], color)  # graph[5] is map dict
        edge2id[(n2, n1)] = edge2id[(n1, n2)]
        # print("DOES THIS NEVER HAPPEN?????")
        # print(edge2id[(n1, n2)], n1, n2)
    # for poly in graph[6]:
    #     canvas.create_polygon(poly, fill="grey", outline="blue")
    ROOT.update()
    return edge2id

def draw_all_edges(ROOT, canvas, graph, color="white"):
    ROOT.geometry("1200x800")  # sets geometry
    counter = 0
    canvas.pack(fill=BOTH, expand=1)  # sets fill expand
    for n1, n2 in graph[4]:  # graph[4] keys are edge set
        # print(n1, n2, graph[4][(n1, n2)])
        draw_line(canvas, *graph[5][n1], *graph[5][n2], color)  # graph[5] is map dict
    # for poly in graph[6]:
    #     canvas.create_polygon(poly, fill="grey", outline="blue")
    ROOT.update()

def dijkstra(start, goal, graph):
    ROOT = Tk()  # creates new tkinter window
    ROOT.title(f"Dijikstra - {graph[1][start]} to {graph[1][goal]}")
    ROOT.lift()
    ROOT.attributes("-topmost", True)
    if MODE == "dark":
        canvas = Canvas(ROOT, background="black")  # sets background color
        edge2id = draw_all_edges_out(ROOT, canvas, graph)
    else:
        canvas = Canvas(ROOT, background="white")
        edge2id = draw_all_edges_out(ROOT, canvas, graph, color="black")
    counter = 0

    fringe = []
    closed = {start: (0, [start])}
    heappush(
        fringe, (0, start, [start])
    )  # we still use a heap but we only need to store the cost and the node, not the heuristic
    while len(fringe) > 0:
        v = heappop(fringe)
        if v[1] == goal:
            path, cost = closed[v[1]][1], v[0]
            draw_final_path(ROOT, canvas, path, graph)
            ROOT.destroy()
            return path, cost
        for child in graph[3][v[1]]:
            cost = (
                closed[v[1]][0] + graph[4][(v[1], child)]
            )  # cost is the cost of the parent + the cost of the edge
            if child not in closed or closed[child][0] > cost:
                heappush(fringe, (cost, child, v[2] + [child]))
                closed[child] = (cost, v[2] + [child])
                # print("hello")
                # TODO use edge2id to change color of edge instead of redrawing
                # print(edge2id[(v[1], child)])
                # ADD ANOTHER IF STATEMENTS SO THAT IF COST IS BIGGER
                # THEN COLOR IT IN BUT DONT ACTUALLY HEAP PUSH
                # because the path is not optimal but we still have to color it in
                canvas.itemconfig(edge2id[(v[1], child)], fill="OrangeRed2", width=2)
                draw_line_out(canvas, *graph[5][v[1]], *graph[5][child], "OrangeRed2") # star unpacks the list
            if child in closed:
                canvas.itemconfig(edge2id[(v[1], child)], fill="OrangeRed2", width=2)
                draw_line_out(canvas, *graph[5][v[1]], *graph[5][child], "OrangeRed2")
        counter += 1
        if counter % (SPEED * 600) == 0:
            ROOT.update()
    return None, None

def dijkstra_dfs(start, goal, graph):
    ROOT = Tk()  # creates new tkinter window
    ROOT.title(f"Dijikstra DFS - {graph[1][start]} to {graph[1][goal]}")
    ROOT.lift()
    ROOT.attributes("-topmost", True)
    if MODE == "dark":
        canvas = Canvas(ROOT, background="black")  # sets background color
        edgeid = draw_all_edges_out(ROOT, canvas, graph)
    else:
        canvas = Canvas(ROOT, background="white")
        edgeid = draw_all_edges_out(ROOT, canvas, graph, color="black")
    counter = 0

    fringe = []
    closed = {start: (0, [start])}
    heappush(
        fringe, (0, start, [start])
    )  # we still use a heap but we only need to store the cost and the node, not the heuristic
    while len(fringe) > 0:
        v = _heappop_max(fringe)
        if v[1] == goal:
            path, cost = closed[v[1]][1], v[0]
            draw_final_path(ROOT, canvas, path, graph)
            ROOT.destroy()
            return path, cost
        for child in graph[3][v[1]]:
            cost = (
                closed[v[1]][0] + graph[4][(v[1], child)]
            )  # cost is the cost of the parent + the cost of the edge
            if child not in closed or closed[child][0] > cost:
                heappush(fringe, (cost, child, v[2] + [child]))
                closed[child] = (cost, v[2] + [child])
                # print("hello")
                # print(*tuple(graph[5][v]), *tuple(graph[5][child]))
                canvas.itemconfig(edgeid[(v[1], child)], fill="OrangeRed2", width=2)
                draw_line(canvas, *graph[5][v[1]], *graph[5][child], "OrangeRed2", line_width=2)
            if child in closed:
                canvas.itemconfig(edgeid[(v[1], child)], fill="OrangeRed2", width=2)
                draw_line(canvas, *graph[5][v[1]], *graph[5][child], "OrangeRed2", line_width=2)
        counter += 1
        if counter % (SPEED * 600) == 0:
            ROOT.update()
    return None, None

def dijkstra_Kdfs(start, goal, graph, depth, ROOT, canvas):
    if MODE == "dark":
        edge2id = draw_all_edges_out(ROOT, canvas, graph)
    else:
        edge2id = draw_all_edges_out(ROOT, canvas, graph, color="black")
    counter = 0

    fringe = []
    closed = {start: (0, [start])}
    heappush(
        fringe, (0, start, [start])
    )  # we still use a heap but we only need to store the cost and the node, not the heuristic
    while len(fringe) > 0:
        v = heappop(fringe)
        if v[1] == goal:
            path, cost = closed[v[1]][1], v[0]
            draw_final_path(ROOT, canvas, path, graph)
            ROOT.destroy()
            return path, cost
        # print(v[0], depth)
        if v[0] < depth:
            for child in graph[3][v[1]]:
                cost = (
                    closed[v[1]][0] + graph[4][(v[1], child)]
                )  # cost is the cost of the parent + the cost of the edge
                if child not in closed or closed[child][0] > cost:
                    heappush(fringe, (cost, child, v[2] + [child]))
                    closed[child] = (cost, v[2] + [child])
                    draw_line(canvas, *graph[5][v[1]], *graph[5][child], "OrangeRed2") # star unpacks the list
                    canvas.itemconfig(edge2id[(v[1], child)], fill="OrangeRed2", width=2)
                if child in closed:
                    canvas.itemconfig(edge2id[(v[1], child)], fill="OrangeRed2", width=2)
                    draw_line(canvas, *graph[5][v[1]], *graph[5][child], "OrangeRed2")
        counter += 1
        if counter % int((depth * 0.2 * SPEED)) == 0:
            ROOT.update()
    return None, None

def dijikstra_iddfs(start, goal, graph):
    INCR = dist_heuristic(start, goal, graph) // 2
    ROOT = Tk()  # creates new tkinter window
    ROOT.title(f"Dijikstra ID-DFS - {graph[1][start]} to {graph[1][goal]}")
    ROOT.lift()
    ROOT.attributes("-topmost", True)
    if MODE == "dark":
        canvas = Canvas(ROOT, background="black")  # sets background color
    else:
        canvas = Canvas(ROOT, background="white")

    max_depth = INCR
    result = (None, None)
    while result[0] == None:
        print(max_depth)
        result = dijkstra_Kdfs(start, goal, graph, max_depth, ROOT, canvas)
        max_depth += INCR # increase the max depth by 100 each iteration
    return result

def bidirectional_dijkstra(start, goal, graph):
    ROOT = Tk()  # creates new tkinter window
    ROOT.title(f"Bidirectional Dijikstra - {graph[1][start]} to {graph[1][goal]}")
    ROOT.lift()
    ROOT.attributes("-topmost", True)
    if MODE == "dark":
        canvas = Canvas(ROOT, background="black")  # sets background color
        edge2id = draw_all_edges_out(ROOT, canvas, graph)
    else:
        canvas = Canvas(ROOT, background="white")
        edge2id = draw_all_edges_out(ROOT, canvas, graph, color="black")
    # Create dictionaries to store the cost and path of the visited nodes for both directions
    closed_start = {start: (0, [start])}
    closed_goal = {goal: (0, [goal])}

    # Create heaps to store the nodes that still need to be visited for both directions
    fringe_start = [(0, start, [start])]
    fringe_goal = [(0, goal, [goal])]

    # Create a set to store nodes that have been visited in both directions
    intersect = set()

    counter = 0

    while len(fringe_start) > 0 and len(fringe_goal) > 0:
        # Pop the node with the smallest cost from the start heap
        v_start = heappop(fringe_start)
        # If the node has been visited from the other direction, return the path and cost
        if v_start[1] in closed_goal:
            print("found thru start")
            # path = v_start[2] + list(reversed(closed_goal[v_start[1]][1]))
            path = v_start[2] + list(reversed(closed_goal[v_start[1]][1][1:]))
            cost = v_start[0] + closed_goal[v_start[1]][0]
            draw_final_path(ROOT, canvas, path, graph)
            ROOT.destroy()
            return path, cost
        intersect.add(v_start[1])
        # Iterate over the children of the node
        for child in graph[3][v_start[1]]:
            if child in intersect:
                continue
            cost = closed_start[v_start[1]][0] + graph[4][(v_start[1], child)]
            if child not in closed_start or closed_start[child][0] > cost:
                heappush(fringe_start, (cost, child, v_start[2] + [child]))
                closed_start[child] = (cost, v_start[2] + [child])
                draw_line(canvas, *graph[5][v_start[1]], *graph[5][child], "OrangeRed2") # star unpacks the list
                canvas.itemconfig(edge2id[(v_start[1], child)], fill="OrangeRed2", width=2)
            if child in closed_start:
                canvas.itemconfig(edge2id[(v_start[1], child)], fill="OrangeRed2", width=2)
                draw_line(canvas, *graph[5][v_start[1]], *graph[5][child], "OrangeRed2")
        # Pop the node with the smallest cost from the goal heap
        v_goal = heappop(fringe_goal)
        # If the node has been visited from the other direction, return the path and cost
        if v_goal[1] in closed_start:
            # print("found thru goal")
            path = v_goal[2] + list(reversed(closed_start[v_goal[1]][1])) # + list(reversed(v_goal[2][1:]))
            # print(v_goal[2], closed_start[v_start[1]][1])
            # path = closed_start[v_start[1]][1][1:] + v_goal[2]
            cost = v_goal[0] + closed_start[v_goal[1]][0]
            draw_final_path(ROOT, canvas, path, graph)
            ROOT.destroy()
            return path, cost
        intersect.add(v_goal[1])
        # Iterate over the children of the node
        for child in graph[3][v_goal[1]]:
            if child in intersect:
                continue
            cost = closed_goal[v_goal[1]][0] + graph[4][(v_goal[1], child)]
            if child not in closed_goal or closed_goal[child][0] > cost:
                heappush(fringe_goal, (cost, child, v_goal[2] + [child]))
                closed_goal[child] = (cost, v_goal[2] + [child])
                draw_line(canvas, *graph[5][v_goal[1]], *graph[5][child], "OrangeRed2") # star unpacks the list
                canvas.itemconfig(edge2id[(v_goal[1], child)], fill="OrangeRed2", width=2)
            if child in closed_goal:
                canvas.itemconfig(edge2id[(v_goal[1], child)], fill="OrangeRed2", width=2)
                draw_line(canvas, *graph[5][v_goal[1]], *graph[5][child], "OrangeRed2")

        # Increment the counter and check if it is divisible by 6000
        counter += 1
        if counter % (200 * SPEED) == 0:
            # Update the Tkinter window
            ROOT.update()

    # If the loop ends without finding the goal node, return None, None
    return None, None


def a_star(
    start, goal, graph, heuristic=dist_heuristic
):  # incase we want to change heuristic later

    ROOT = Tk()  # creates new tkinter window
    ROOT.title(f"A* - {graph[1][start]} to {graph[1][goal]}")
    ROOT.lift()
    ROOT.attributes("-topmost", True)
    if MODE == "dark":
        canvas = Canvas(ROOT, background="black")  # sets background color
        edge2id =  draw_all_edges_out(ROOT, canvas, graph, color="white")
    else:
        canvas = Canvas(ROOT, background="white")
        edge2id =  draw_all_edges_out(ROOT, canvas, graph, color="black")

    counter = 0

    fringe = []
    costs = heuristic(start, goal, graph)
    closed = {start: (0, [start])}  # closed set is keys
    heappush(fringe, (costs, start, [start]))
    while len(fringe) > 0:
        v = heappop(fringe)
        if v[1] == goal:
            path, cost = closed[v[1]][1], v[0]
            draw_final_path(ROOT, canvas, path, graph)
            ROOT.destroy()
            # print("path: ", path)
            # print("path length: ", len(path))
            return path, cost
        for child in graph[3][v[1]]:
            cost = closed[v[1]][0] + graph[4][(v[1], child)]
            if child not in closed or closed[child][0] > cost:
                cost2 = heuristic(child, goal, graph)
                heappush(fringe, (cost + cost2, child, v[2] + [child]))
                closed[child] = (cost, v[2] + [child])
                draw_line(canvas, *graph[5][v[1]], *graph[5][child], "firebrick1") # star unpacks the list
                canvas.itemconfig(edge2id[(v[1], child)], fill="firebrick1", width=2)
            if child in closed:
                canvas.itemconfig(edge2id[(v[1], child)], fill="firebrick1", width=2)
                draw_line(canvas, *graph[5][v[1]], *graph[5][child], "firebrick1")
        counter += 1
        if counter % 2000 == 0:
            ROOT.update()
    return None, None

def bidirectional_a_star(start, goal, graph, heuristic=dist_heuristic):
    ROOT = Tk()  # creates new tkinter window
    ROOT.title(f"Bidirectional A* - {graph[1][start]} to {graph[1][goal]}")
    ROOT.lift()
    ROOT.attributes("-topmost", True)
    if MODE == "dark":
        canvas = Canvas(ROOT, background="black")  # sets background color
        edge2id =  draw_all_edges_out(ROOT, canvas, graph, color="white")
    else:
        canvas = Canvas(ROOT, background="white")
        edge2id =  draw_all_edges_out(ROOT, canvas, graph, color="black") # sets background color to white

    counter = 0
    # Set up the fringe for both the forward and backward searches
    forward_fringe = []
    backward_fringe = []

    # Set up the closed sets for both the forward and backward searches
    forward_closed = {start: (0, [start])}
    backward_closed = {goal: (0, [goal])}

    # Set up the cost estimates for both the forward and backward searches
    forward_cost = heuristic(start, goal, graph)
    backward_cost = heuristic(goal, start, graph)

    # Add the starting points to the fringes
    heappush(forward_fringe, (forward_cost, start, [start]))
    heappush(backward_fringe, (backward_cost, goal, [goal]))

    while len(forward_fringe) > 0 and len(backward_fringe) > 0:
        # Expand the next node in the forward search
        forward_v = heappop(forward_fringe)
        for child in graph[3][forward_v[1]]:
            cost = forward_closed[forward_v[1]][0] + graph[4][(forward_v[1], child)]
            if child not in forward_closed or forward_closed[child][0] > cost:
                draw_line(canvas, *graph[5][forward_v[1]], *graph[5][child], "firebrick1") # star unpacks the list
                canvas.itemconfig(edge2id[(forward_v[1], child)], fill="firebrick1", width=2)
                cost2 = heuristic(child, goal, graph)
                heappush(forward_fringe, (cost + cost2, child, forward_v[2] + [child]))
                forward_closed[child] = (cost, forward_v[2] + [child])
                # Check if the child node has been explored in the backward search
                if child in backward_closed:
                    print("found thru forward")
                    # We have found a path!
                    path1 = forward_closed[child][1]
                    path2 = backward_closed[child][1][::-1]  # Reverse the path from the backward search
                    path = path1 + path2[1:]  # Concatenate the two paths and remove the overlapping node
                    cost = forward_closed[child][0] + backward_closed[child][0]
                    draw_final_path(ROOT, canvas, path, graph)
                    ROOT.destroy()
                    return path, cost
            if child in forward_closed:
                canvas.itemconfig(edge2id[(forward_v[1], child)], fill="firebrick1", width=2)
                draw_line(canvas, *graph[5][forward_v[1]], *graph[5][child], "firebrick1")

        # Expand the next node in the backward search
        backward_v = heappop(backward_fringe)
        for child in graph[3][backward_v[1]]:
            cost = backward_closed[backward_v[1]][0] + graph[4][(backward_v[1], child)]
            if child not in backward_closed or backward_closed[child][0] > cost:
                draw_line(canvas, *graph[5][backward_v[1]], *graph[5][child], "firebrick1") # star unpacks the list
                canvas.itemconfig(edge2id[(backward_v[1], child)], fill="firebrick1", width=2)
                cost2 = heuristic(child, start, graph)
                heappush(backward_fringe, (cost + cost2, child, backward_v[2] + [child]))
                backward_closed[child] = (cost, backward_v[2] + [child])
                # Check if the child node has been explored in the forward search
                if child in forward_closed:
                    # We have found a path!
                    print("found thru backwards")
                    path2 = forward_closed[child][1]
                    path1 = backward_closed[child][1][::-1]  
                    path = path2 + path1[1:]  # Concatenate the two paths and remove the overlapping node
                    cost = forward_closed[child][0] + backward_closed[child][0]
                    draw_final_path(ROOT, canvas, path, graph)
                    ROOT.destroy()
                    return path, cost
            if child in backward_closed:
                canvas.itemconfig(edge2id[(backward_v[1], child)], fill="firebrick1", width=2)
                draw_line(canvas, *graph[5][backward_v[1]], *graph[5][child], "firebrick1")
        counter += 1
        if counter % (SPEED * 100) == 0:
            ROOT.update()
    # If we reach this point, it means that we have explored all nodes in both fringes
    # without finding a path, so we return None
    return None, None


def reverse_a_star(
    start, goal, graph, heuristic=dist_heuristic
):  # incase we want to change heuristic later

    ROOT = Tk()  # creates new tkinter window
    ROOT.title(f"Reverse A* - {graph[1][start]} to {graph[1][goal]}")
    ROOT.lift()
    ROOT.attributes("-topmost", True)
    if MODE == "dark":
        canvas = Canvas(ROOT, background="black")  # sets background color
        edge2id = draw_all_edges_out(ROOT, canvas, graph)
    else:
        canvas = Canvas(ROOT, background="white")
        edge2id = draw_all_edges_out(ROOT, canvas, graph, "black")

    counter = 0

    fringe = []
    costs = heuristic(start, goal, graph)
    closed = {start: (0, [start])}  # closed set is keys
    heappush(fringe, (costs, start, [start]))
    while len(fringe) > 0:
        v = _heappop_max(fringe) # pick the WORST node
        if v[1] == goal:
            path, cost = closed[v[1]][1], v[0]
            draw_final_path(ROOT, canvas, path, graph)
            ROOT.destroy()
            # print("path: ", path)
            # print("path length: ", len(path))
            return path, cost
        for child in graph[3][v[1]]:
            cost = closed[v[1]][0] + graph[4][(v[1], child)]
            if child not in closed or closed[child][0] > cost:
                cost2 = heuristic(child, goal, graph)
                heappush(fringe, (cost + cost2, child, v[2] + [child]))
                closed[child] = (cost, v[2] + [child])
                draw_line(canvas, *graph[5][v[1]], *graph[5][child], "firebrick1") # star unpacks the list
                canvas.itemconfig(edge2id[(v[1], child)], fill="firebrick1", width=2)
            if child in closed:
                canvas.itemconfig(edge2id[(v[1], child)], fill="firebrick1", width=2)
                draw_line(canvas, *graph[5][v[1]], *graph[5][child], "firebrick1")
        counter += 1
        if counter % (1000 * SPEED) == 0:
            ROOT.update()
    return None, None


def main():
    """
    info about graph
    0: node id: (lat, long)
    1: node id: city name
    2: city name: node id
    3: node id: set of neighbor node ids
    4: (node id, node id): edge cost
    5: scaled coordinates
    """
    SEARCHES = {
    "1": (dijkstra, "Dijikstra"),
    "2": (bidirectional_dijkstra, "Bidirectional Dijikstra"),
    "3": (dijkstra_dfs, "Dijikstra DFS"),
    "4": (dijikstra_iddfs, "Dijikstra ID-DFS"),
    "5": (a_star, "A*"),
    "6": (reverse_a_star, "Reverse A*"),
    "7": (bidirectional_a_star, "Bidirectional A*")
    }
    if len(sys.argv) > 1:
        start, goal = sys.argv[1], sys.argv[2]
    else:
        start = input("Start city: ")
        goal = input("Goal city: ")
    cur_time = perf_counter()
    graph = make_graph("./rrNodes.txt", "./rrNodeCity.txt", "./rrEdges.txt")
    if start not in graph[2]:
        raise NameError(f"Given start city ({start}) not in graph")
    if goal not in graph[2]:
        raise NameError(f"Given start city ({goal}) not in graph")
    # for a in graph:
    #     for i, (k,v) in enumerate(a.items()):
    #         if i < 5:
    #             print(k, v)
    print(f"Time to create graph: {(perf_counter() - cur_time)}")

    # Get the search from user input
    search = input("Search type (1: Dijikstra, 2: Bidirectional Dijikstra, 3: Dijikstra DFS, 4: Dijikstra ID-DFS, 5: A*, 6: Reverse A*, 7: Bidirectional A*): ")
    if search not in SEARCHES:
        raise NameError(f"Invalid search type ({search})")
    search, name = SEARCHES[search]
    # Run the search
    cur_time = perf_counter()
    path, cost = search(graph[2][start], graph[2][goal], graph)
    print(
        f"{start} to {goal} with {name}: {cost} in {(perf_counter() - cur_time)} seconds."
    )

    # assert cost_0 == cost_1  # sanity check

# global for gui
SEARCHES = {
    "1": (dijkstra, "Dijikstra"),
    "2": (bidirectional_dijkstra, "Bidirectional Dijikstra"),
    "3": (dijkstra_dfs, "Dijikstra DFS"),
    "4": (dijikstra_iddfs, "Dijikstra ID-DFS"),
    "5": (a_star, "A*"),
    "6": (reverse_a_star, "Reverse A*"),
    "7": (bidirectional_a_star, "Bidirectional A*")
}
GRAPH = make_graph("./rrNodes.txt", "./rrNodeCity.txt", "./rrEdges.txt")

def start_handler(event):
    global START
    START = event 

def end_handler(event):
    global DEST
    DEST = event

def search_handler(event):
    global SEARCH
    for search in SEARCHES.values():
        if event == search[1]:
            SEARCH = search[0]
            break

def lightmode_handler():
    global MODE
    MODE = "light"

def darkmode_handler():
    global MODE
    MODE = "dark"

def runner():
    global START, DEST, SEARCH, MODE
    if START is None or DEST is None or SEARCH is None:
        messagebox.showerror("Error", "Please select a start, end, and search type")
        return
    if START == DEST:
        messagebox.showwarning("Warning", "Start and end are the same")
        return
    SEARCH(GRAPH[2][START], GRAPH[2][DEST], GRAPH)
    

def gui_main():
    # read in graph
    graph = make_graph("./rrNodes.txt", "./rrNodeCity.txt", "./rrEdges.txt")

    # Set up the window
    window = Tk()
    window.title("Manav Gagvani - Train Routes")
    window.resizable(width=False, height=False)

    info = Frame(master=window, borderwidth=1)
    info.grid(row=0, column=0, padx=5, pady=5) # i, j, padx, pady
    infolabel = Label(master=info, text="Select Start and Destination Cities")
    infolabel.pack()

    start = Frame(master=window, borderwidth=1)
    start.grid(row=0, column=1, padx=5, pady=5) # i, j, padx, pady
    startlabel = Label(master=start, text="Start:")
    start_str = StringVar(window)
    startdropdown = OptionMenu(start, start_str, *graph[1].values(), command=start_handler)
    startlabel.pack()
    startdropdown.pack()

    dest = Frame(master=window, borderwidth=1)
    dest.grid(row=0, column=2, padx=5, pady=5) # i, j, padx, pady
    destlabel = Label(master=dest, text="Destination:")
    dest_str = StringVar(window)
    destdropdown = OptionMenu(dest, dest_str, *graph[1].values(), command=end_handler)
    destlabel.pack()
    destdropdown.pack()

    searchinfo = Frame(master=window, borderwidth=1)
    searchinfo.grid(row=1, column=0, padx=5, pady=5) # i, j, padx, pady
    searchinfolabel = Label(master=searchinfo, text="Select Search Type")
    searchinfolabel.pack()

    search = Frame(master=window, borderwidth=1)
    search.grid(row=1, column=1, padx=5, pady=5) # i, j, padx, pady
    searchlabel = Label(master=search, text="Dijikstra Variants:")
    search_str = StringVar(window)
    searchdropdown = OptionMenu(search, search_str, *[SEARCH[1] for SEARCH in SEARCHES.values()][:4], command=search_handler)
    searchlabel.pack()
    searchdropdown.pack()

    search2 = Frame(master=window, borderwidth=1)
    search2.grid(row=1, column=2, padx=5, pady=5) # i, j, padx, pady
    searchlabel2 = Label(master=search2, text="A* Variants:")
    searchdropdown2 = OptionMenu(search2, search_str, *[SEARCH[1] for SEARCH in SEARCHES.values()][4:], command=search_handler)
    searchlabel2.pack()
    searchdropdown2.pack()

    colormode = Frame(master=window, borderwidth=1)
    colormode.grid(row=2, column=0, padx=5, pady=5) # i, j, padx, pady
    lightmodebtn = Button(master=colormode, text="Light Mode", command=lightmode_handler, pady=5)
    darkmodebtn = Button(master=colormode, text="Dark Mode", command=darkmode_handler, pady=5)
    lightmodebtn.pack()
    darkmodebtn.pack()

    speed = Frame(master=window, borderwidth=1)
    speed.grid(row=2, column=1, padx=5, pady=5) # i, j, padx, pady
    speedlabel = Label(master=speed, text="Speed:")
    speedslider = Scale(master=speed, from_=1, to=10, orient=HORIZONTAL)
    speedlabel.pack()
    speedslider.pack()

    go = Frame(master=window, borderwidth=1)
    go.grid(row=2, column=2, padx=5, pady=5) # i, j, padx, pady
    gobtn = Button(master=go, text="Go!", command=runner)
    gobtn.pack()

    # Run the application
    window.mainloop()

if __name__ == "__main__":
    gui_main()