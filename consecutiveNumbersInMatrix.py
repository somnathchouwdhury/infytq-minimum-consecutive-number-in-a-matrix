#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 12 20:16:45 2021

@author: samac
"""

#input no of rows from user
m=int(input())

#arrays for storing matrix and consecutive numbers
mat,lst=[],[]


#input space seperated matrix of m rows
for i in range(m):
    
    int_list = [int(x) for x in input().split()]
    mat.append(int_list)
    
#print(mat)

#print(len(mat[0]),m)

# r represents rows and c for column 
r=m
c=len(mat[0])


#checking the consecutive numbers
for i in range(0,r):
    for j in range(0,c):
        if(j<c-3):#c-3 because it should not search beyond the matrix

            if(mat[i][j]==mat[i][j+1]==mat[i][j+2]==mat[i][j+3]):#condition for checking if number repeats itself in column
                lst.append(mat[i][j])
                
        if(i<r-3):#r-3 because it should not search beyond the matrix
            
            if(mat[i][j]==mat[i+1][j]==mat[i+2][j]==mat[i+3][j]):#condition for checking if number repeats itself in a row
                lst.append(mat[i][j])
                
        if(j<c-3 and i>=3):#since minimum repetation is 4 diagonal repeatation should shart beyond 3,3
            if(mat[i][j]==mat[i-1][j+1]==mat[i-2][j+2]==mat[i-3][j+3]):#condition for checking if number repeats itself in diagonal(left)
                lst.append(mat[i][j])
                
        if(j>=3 and i>=3):#since minimum repetation is 4 diagonal repeatation should end beyond c-3,r-3
            if(mat[i][j]==mat[i-1][j-1]==mat[i-2][j-2]==mat[i-3][j-3]):#condition for checking if number repeats itself in diagonal(right)
                lst.append(mat[i][j])
                
                
if(len(lst)==0):
    print("-1")
else:
    print(min(lst))
    
