#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 12 20:16:45 2021

@author: samac
"""

m=int(input())
mat=[]
lst=[]

for i in range(m):
    
    int_list = [int(x) for x in input().split()]
    mat.append(int_list)
    
#print(mat)

#print(len(mat[0]),m)

r=m
c=len(mat[0])

for i in range(0,r):
    for j in range(0,c):
        if(j<c-3):
            if(mat[i][j]==mat[i][j+1]==mat[i][j+2]==mat[i][j+3]):
                lst.append(mat[i][j])
                
        if(i<r-3):
            if(mat[i][j]==mat[i+1][j]==mat[i+2][j]==mat[i+3][j]):
                lst.append(mat[i][j])
                
        if(j<c-3 and i>=3):
            if(mat[i][j]==mat[i-1][j+1]==mat[i-2][j+2]==mat[i-3][j+3]):
                lst.append(mat[i][j])
                
        if(j>=3 and i>=3):
            if(mat[i][j]==mat[i-1][j-1]==mat[i-2][j-2]==mat[i-3][j-3]):
                lst.append(mat[i][j])
                
                
if(len(lst)==0):
    print("-1")
else:
    print(min(lst))
    