# -*- coding: utf-8 -*-
"""
Created on Tue Apr 26 12:41:24 2016

@author: jcm
"""

import numpy as np


"""
----------------------- Longest Common Sequence -----------------------
"""

def lcs(x, y):
    m = len(x)
    n = len(y)
    a = np.zeros((m+1,n+1), dtype=int)
    b = [[0 for j in xrange(n+1)] for i in xrange(m+1)]
    for i in xrange(1,m+1):
        for j in xrange(1,n+1):
            if x[i-1] == y[j-1]:
                a[i,j] = a[i-1,j-1]+1
                b[i][j] = "e"
            elif a[i-1,j] > a[i,j-1]:
                a[i,j] = a[i-1,j]
                b[i][j] = "d"
            else:
                a[i,j] = a[i,j-1]
                b[i][j] = "r"
    path = ""
    i = m
    j = n
    while i>0 and j>0:
        if b[i][j] is "r":
            j -= 1
        elif b[i][j] is "d":
            i -= 1
        else:
            i -= 1
            j -= 1
            path = x[i]+path
    return a[m,n], path

"""
-------------------------- Max Subarray -----------------------------
"""
def max_subarray(A):
    max_ending_here = max_so_far = A[0]
    start = 0
    end = 1
    for i in xrange(1,len(A)):
        if max_ending_here <= 0:
            # tag of whether the largest sum ending at the last
            # position is negative.
            tag = True
        else:
             tag = False
        max_ending_here = max(A[i], max_ending_here + A[i])
        if max_ending_here > max_so_far:
            max_so_far = max_ending_here
            end = i + 1
            if tag:
                start = i
    return max_so_far,A[start:end],start,end
    
"""
------------ Matrix Chain Multiplication with Memorization ------------
"""
def mcm_memorized(dim):
    n = len(dim)-1
    a = np.full((n+1,n+1),-1,dtype=int)
    b = np.zeros((n+1,n+1),dtype=int)
    return mcm_memorized_aux(dim,a,b,0,n),a,b

def mcm_memorized_aux(dim, a, b, i, j):
    if a[i,j] >= 0:
        return a[i,j]
    if j - i <= 1:
        a[i,j] = 0
        return 0
        return a[i,j]
    nm = np.inf # number of multiplications
    for k in xrange(i+1,j):
        temp = dim[i]*dim[j]*dim[k]\
             + mcm_memorized_aux(dim,a,b,i,k)\
             + mcm_memorized_aux(dim,a,b,k,j)
        if temp < nm:
            nm = temp
            mk = k
    a[i,j] = nm
    b[i,j] = mk
    return nm

"""
------------ Matrix Chain Multiplication with Dynamic Programming ------------
"""
def mcm_dp(dim):
    n = len(dim)-1
    a = np.zeros((n+1,n+1),dtype=int)
    b = np.copy(a)
    for l in xrange(2,n+1): # l is the lenght of chains
        for i in xrange(0,n-l+1):
            j = i + l
            nm = np.inf # number of multiplications
            for k in xrange(i+1,j):
                temp = dim[i]*dim[j]*dim[k] + a[i,k] + a[k,j]
                if temp < nm:
                    nm = temp
                    mk = k # pisition for minimum number of multiplications
            a[i,j] = nm
            b[i,j] = mk
    return a[0,n],a,b

def print_mcm_scheme(b,i,j):
    if j-i == 1:
        return "A%s" % j
    return "("+print_mcm_scheme(b,i,b[i,j])+print_mcm_scheme(b,b[i,j],j)+")"