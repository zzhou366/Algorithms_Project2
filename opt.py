# -*- coding: utf-8 -*-
"""
Created on Mon Apr 19 18:45:21 2021

@author: Tony Zhou
"""
from collections import defaultdict

class Graph:

    def __init__(self, graph):
        self.graph = graph
        self. ROW = len(graph)


    # Using BFS as a searching algorithm 
    def searching_algo_BFS(self, s, t, parent):

        visited = [False] * (self.ROW)
        queue = []

        queue.append(s)
        visited[s] = True

        while queue:

            u = queue.pop(0)

            for ind, val in enumerate(self.graph[u]):
                if visited[ind] == False and val > 0:
                    queue.append(ind)
                    visited[ind] = True
                    parent[ind] = u

        return True if visited[t] else False

    # Applying fordfulkerson algorithm
    def ford_fulkerson(self, source, sink):
        parent = [-1] * (self.ROW)
        max_flow = 0

        while self.searching_algo_BFS(source, sink, parent):

            path_flow = float("Inf")
            s = sink
            while(s != source):
                path_flow = min(path_flow, self.graph[parent[s]][s])
                s = parent[s]

            # Adding the path flows
            max_flow += path_flow

            # Updating the residual values of edges
            v = sink
            while(v != source):
                u = parent[v]
                self.graph[u][v] -= path_flow
                self.graph[v][u] += path_flow
                v = parent[v]

        return max_flow
    
def takeInput():
    dpd_list = {}
    #take first line input
    fl = input()
    fl = fl.split(' ')
    num_mine = int(fl[0])
    num_dpt = int(fl[1])
    
    #take second line input
    mine_value = input()
    mine_value = mine_value.split(' ')
    # for val in mine_value:
    #     if not -2000 <= int(val) <= 2000:
    #         return 0,0
    
    #take the rest of lines of input
    for i in range(num_dpt):
        temp = input()
        temp = temp.split(' ')
        for k in range(len(temp)):
            if k == 0:
                dpd_list[int(temp[0])] = []
            else:
                dpd_list[int(temp[0])].append(int(temp[k]))
                                              
    return mine_value, dpd_list

def construct_Graph(mv,dpt):
    graph = []
    num_profit = 0
    max_profit = 0
    
    #construct first part of graph
    fp = []
    for i in range(len(mv)+2):
        if i == 0:
            fp.append(0)
        elif i == (len(mv)+2)-1:
            fp.append(0)
        else:
            
            if int(mv[i-1]) > 0:
                fp.append(int(mv[i-1]))
                num_profit = num_profit + 1
                max_profit = max_profit + int(mv[i-1])
            else:
                fp.append(0) 
    graph.append(fp)

    # construct second part of graph
    for i in range(len(mv)):
        temp = []
        for k in range(len(mv)+2):
            temp.append(0)
        graph.append(temp)
    for idx in dpt:
        for i in dpt[idx]:
            graph[int(idx)][int(i)] = float('inf')
    for i in range(len(mv)):
        if int(mv[i]) >=0:
            continue
        else:
            graph[i+1][len(mv)+2-1] = abs(int(mv[i]))
            
    
    
    # for idx in dpt:
    #     for i in dpt[idx]:
    #         graph[int(idx)][int(i)] = float('inf')
    
    # # construct the third part of the graph
    # num_cost = int(len(mv)) - num_profit 
    # # for i in range(num_cost):
    # #     temp = []
    # #     for k in range(len(mv)+2):
    # #         temp.append(0)
    # #     graph.append(temp)
    
    # for i in range(num_cost):
    #     graph[i + 1 + num_cost][len(mv)+2-1] = abs(int(mv[i + num_cost]))
        
    # construct the last part graph
    temp = []
    for k in range(len(mv)+2):
        temp.append(0)
    graph.append(temp)
        

     
    return graph,max_profit
            
def driver():
    # case1
    # dpt = {1: [2]}
    # mv = ['4', '-3']
    
    
    # case2
    # dpt = {1: [4, 5], 2: [5], 3: [6]}
    # mv = ['100', '200', '150', '-200', '-100', '-50']
    # case3
    # dpt = {1:[2], 3: [1, 4], 4: [2, 6], 5: [3, 7], 7: [4, 8], 8: [6]}
    # mv = ['1', '-5', '-2', '1', '1', '0', '10', '2']
    mv,dpt = takeInput()
    s = 0
    t = len(mv) + 1
    g,mp = construct_Graph(mv, dpt)
    graph = Graph(g)
    min_cut = graph.ford_fulkerson(s,t)
    output = mp - min_cut
    print(output)
        
    
    
    
            
        
if __name__ == "__main__":
    driver()
    
