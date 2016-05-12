# -*- coding: utf-8 -*-
"""
Created on Wed Apr 27 17:06:34 2016

@author: jcm
"""

import numpy as np
import time
from matplotlib import pyplot as plt

mst      = "./experiment8/MST.txt"
shortest = "./experiment8/dijkstra.txt"

def generate_graph(n):
    G = np.random.randint(1, 100,(n,n))
    for i in xrange(n):
        G[i,i] = 0.0
        for j in xrange(0,i):
            G[i,j] = G[j,i]
    s = np.random.randint(0,n)
    return G,s


def dijkstra_readfile(filename):
    f = open(filename, "r")
    n = int(f.readline())
    s = int(f.readline())-1
    adj_mat = np.array([map(float, line.split()) for line in f.readlines()])
    n = len(adj_mat)
    for i in xrange(n):
        for j in xrange(n):
            if i != j and adj_mat[i,j] == 0.:
                adj_mat[i,j] = np.inf
    f.close()
    return adj_mat, n, s
    
def mst_readfile(filename):
    f = open(filename, "r")
    n = int(f.readline())
    adj_mat = np.array([map(float, line.split()) for line in f.readlines()])
    n = len(adj_mat)
    for i in xrange(n):
        for j in xrange(n):
            if i != j and adj_mat[i,j] == 0.:
                adj_mat[i,j] = np.inf
    f.close()
    return adj_mat, n

def dijkstra(G,n,s):
    dist = [ np.inf for i in xrange(n)]
    prec = [ None   for i in xrange(n)]
    visited = []
    dist[s] = 0.0
    while len(visited) != n:
        min_dist = np.inf
        for i in xrange(n):
            if i not in visited:
                if dist[i] < min_dist:
                    min_dist = dist[i]
                    u = i
        visited.append(u)
        for v in xrange(n):
            if v not in visited and G[u,v] + dist[u] < dist[v]:
                dist[v] = G[u,v] + dist[u]
                prec[v] = u

    return dist, prec

def prim(G):
    n = len(G)
    dist = [np.inf for i in xrange(n)]
    prec = [None   for i in xrange(n)]
    ans  = []
    dist[0] = 0.0
    visited = []
    while len(visited) < n:
        min_dist = np.inf
        for v in xrange(n):
            if v not in visited:
                if dist[v] < min_dist:
                    min_dist = dist[v]
                    u = v
        visited.append(u)
        for v in xrange(n):
            if v not in visited and G[u,v] < dist[v]:
                dist[v] = G[u,v]
                prec[v] = u
    for i in xrange(n):
        if prec[i] is not None:
            ans.append((i,prec[i]))
    return ans

def kruskal(G):
    n    = len(G)
    sets = [[i] for i in xrange(n)]
    ans  = []
    edge = []
    for i in xrange(n):
        for j in xrange(i+1,n):
            edge.append({"w":G[i,j], "uv":(i,j)})
    edge.sort(key=lambda e: e["w"])
    for e in edge:
        if len(ans) is n-1:
            return ans
        u,v = e["uv"]
        if sets[u] != sets[v]:
            # if there are more elements in sets[v], exchange u,v
            # this is to cut the expense of unite two sets
            if len(sets[u]) < len(sets[v]):
                u,v = v,u
            for w in sets[v]:
                sets[u].append(w)
            for w in sets[v]:
                sets[w] = sets[u]
            ans.append((u,v))
    return "NO MST!"

if __name__ == "__main__":
    n = 10
    p_running = np.zeros((n,))
    k_running = np.zeros((n,))
    for i in xrange(n):
        print i+1
        G,s = generate_graph(2**(i+1))
        start = time.clock()
        prim(G)
        end = time.clock()
        p_running[i] = end - start
        start = time.clock()
        kruskal(G)
        end = time.clock()
        k_running[i] = end - start
    plt.plot(np.linspace(1,n,n), np.log(p_running*10**5), linewidth=2, color='red', label="Prim")
    plt.plot(np.linspace(1,n,n), np.log(k_running*10**5), linewidth=2, color='blue', label="Kruskal")
    plt.title("Prim, Kruskal Algorithm Running Time")
    plt.legend(loc=2)
    plt.show()
    





















