"""
================================================================================
NUMPY / MATRIX OPERATIONS (IMAGE 4 & 5)
================================================================================
Matrix A = 
[[2, 4, 6],
 [8, 0, 1],
 [3, 5, 7]]
Functional updates for Matrix A
1) Add row at last
2) Add column at last
3) Add row at pos1
4) Add column at pos2
"""
A = [[2, 4, 6], 
     [8, 0, 1], 
     [3, 5, 7]]

xlist_A = [
    (A.append([10, 11, 12]), A.copy())[1],                                      
    (A[0].append(13), A[1].append(14), A[2].append(15), A.copy())[3],           
    (A.insert(1, [16, 17, 18, 19]), A.copy())[1],                                
    (A[0].insert(2,19), A[1].insert(2,20), A[2].insert(2,21), A.copy())[3]       
]

for i, x in enumerate(xlist_A):
    print(f"{i+1}. {x}")

print("=================================================================================")
########################################################################################

"""
--------------------------------------------------------------------------------
Matrix B (4x4) = 
[[1, 2, 3, 4],
 [5, 6, 7, 8],
 [9, 10, 11, 12],
 [13, 14, 15, 16]]
1) 2nd row
2) 3rd column
3) Rows 3 and 4
4) First 2  columns
5) Sub-matrix [10..16]
6) Elements [5,8], [13,16]
7) Diagonal
8) Anti-diagonal
"""
B = [[1, 2, 3, 4], 
     [5, 6, 7, 8], 
     [9, 10, 11, 12], 
     [13, 14, 15, 16]]

xlist_B = [
    B[1],                                                                       
    [row[2] for row in B],                                                      
    B[2:],                                                                      
    [row[:2] for row in B],                                                      
    [row[1:] for row in B[1:]],                                                 
    [[B[1][0], B[1][3]], [B[3][0], B[3][3]]],                                    
    [B[i][i] for i in range(len(B))],                                           
    [B[i][len(B)-1-i] for i in range(len(B))]                                   
]

for i, x in enumerate(xlist_B):
    print(f"{i+1}. {x}")

print("=================================================================================")
########################################################################################

"""
================================================================================
MATRIX SLICING & MANIPULATION (IMAGE 6)
================================================================================
Matrix C (3x3)
Add col [0,0,0] last
Add col [5,5,5] pos 1
Add row [1..5] last
Add row [6..10] pos 2
Add col [10..50] last
"""
C = [[1, 1, 1], [1, 1, 1], [1, 1, 1]]

xlist_C = [
    ([C[i].append(0) for i in range(3)], C.copy())[1],                          
    ([C[i].insert(1, 5) for i in range(3)], C.copy())[1],                        
    (C.append([1, 2, 3, 4, 5]), C.copy())[1],                                   
    (C.insert(2, [6, 7, 8, 9, 10]), C.copy())[1],                                
    ([C[i].append(val) for i, val in enumerate([10,20,30,40,50])], C.copy())[1]  
]

for i, x in enumerate(xlist_C):
    print(f"{i+1}. {x}")

print("=================================================================================")
########################################################################################

"""
Matrix D (5x5)
Slice specific rows
Step slicing columns
Sub-matrix [6,7,8], [16,17,18]
Diagonal
Anti-diagonal
Selective elements
Elements 10, 15, 20
Elements [8,9], [18,19]
Last row
Sub-matrix[2,4]..
"""
D = [[1, 2, 3, 4, 5], [6, 7, 8, 9, 10], [11, 12, 13, 14, 15], [16, 17, 18, 19, 20], [21, 22, 23, 24, 25]]

xlist_D = [
    [D[0], D[2], D[4]],                                                         
    [[row[0], row[2], row[4]] for row in D],                                    
    [D[1][:3], D[3][:3]],                                                       
    [D[i][i] for i in range(5)],                                                
    [D[i][4-i] for i in range(5)],                                              
    [[D[i][j] for j in [0, 2, 4]] for i in [0, 2, 4]],
    [D[i][4] for i in range(1,4)],                              
    [D[i][2:4] for i in range(1,4,2)],                                          
    D[4],                                                                       
    [D[i][1:4:2] for i in [0, 2, 4]]                                            
]

for i, x in enumerate(xlist_D):
    print(f"{i+1}. {x}")

print("=================================================================================")
########################################################################################

"""
Matrix E (3x3)
a) Replace 60 with 6
b) Rows 1 and 2
c) Sub-matrix [50,6..]
d) Diagonal
e)Anti-diagonal
f) Middle column
g) Middle column
h) 40 and 6
i) 10 and 70
i) [2030], [80,90]
j) [40,6], [70,90]
"""
E = [[10, 20, 30], [40, 50, 60], [70, 80, 90]]

xlist_E = [
    (E[1].__setitem__(2, 6), E.copy())[1],                                      
    E[:2],                                                                      
    [row[1:] for row in E[1:]],                                                 
    [E[i][i] for i in range(3)],                                                 
    [E[i][2-i] for i in range(3)],
    [row[1] for row in E],                                                       
    [E[1][0], E[1][2]],                                                         
    [E[0][0], E[2][0]],                                                         
    [E[0][1:], E[2][1:]],                                                       
    [[E[1][0], E[1][2]], [E[2][0], E[2][2]]]                                    
]

for i, x in enumerate(xlist_E):
    print(f"{i+1}. {x}")

print("=================================================================================")
########################################################################################

"""
Matrix F (4x5)
1) Element 12
2) Columns [9,3,2]..
3) Elements 9 and 0
4) Sub-matrices
5) Elements [11,4,5]..
6) Add row 0s
7) [11,0,4,6,5] (approx)
8) Reversefirst row
9) Rows 2 and 3
0) Multiple sub 1-slices
"""
F = [[11, 0, 4, 6, 5], [1, 9, 3, 2, 1], [7, 0, 4, 9, 8], [3, 7, 12, 15, 0]]

xlist_F = [
    F[3][2],                                                                     
    [[F[1][1], F[1][2], F[1][3]], [F[2][1], F[2][2], F[2][3]]],                  
    [F[1][1], F[2][1]],                                                           
    [F[i][:3] for i in [1, 2, 3]],                                               
    [[F[0][0], F[0][2], F[0][4]], [F[3][0], F[3][2], F[3][4]]],                  
    (F.append([0, 0, 0, 0, 0]), F.copy())[1],                                     
    F[0],                                                                        
    F[0][::-1],                                                                   
    F[1:3],                                                                       
    [F[0][2:4], F[1][2:4], F[2][2:4], F[3][2:4]]                                 
]

for i, x in enumerate(xlist_F):
    print(f"{i+1}. {x}")

print("=================================================================================")
########################################################################################