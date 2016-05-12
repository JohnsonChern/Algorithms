# -*- coding: utf-8 -*-
"""
Created on Wed May 11 23:14:05 2016

@author: jcm
"""

import numpy as np

# ---------------------- N Queens Problem  ----------------------#

def queen(n,tag=False):
    # tag is for result output
    x = np.zeros((n,),dtype=int)
    _queen(x, n, 0, tag)
    
def _queen(x, n, k, tag):
    if k >= n:
        if tag == True:
            print x+1
        return
    for i in xrange(n):
        x[k] = i
        if is_ok(x, k) == True:
            _queen(x, n, k+1, tag)
    
def is_ok(x, k):
    for j in xrange(k):
        if x[j] == x[k] or np.abs(x[j]-x[k]) == np.abs(k-j):
            return False
    return True

# --------------------- 0-1 Knapsack Problem -------------------#

def knapsack(c, w, v):
    x = np.zeros((len(w),),dtype=int)
    _knapsack(x, c, w, v, 0)
    pass

def _knapsack(x, c, w, v, k):
    pass

if __name__ == "__main__":
    queen(10)