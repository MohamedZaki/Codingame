import numpy as np

#reading grid data
grid=[]
for i in range(9):
    grid.append(input().split())   
grid = np.array(grid).reshape((9,9)).astype(int)

#Validating the grid
valid = True
#Checking rows/columns
for i in range(9):
    # all elements are unique:
    if len(grid[i]) != len (set(grid[i])):
        valid= False
        break
    if len(grid[:,i]) != len (set(grid[:,i])):
        valid= False
        break
#checking subgrids
for i in range(0,9,3):
    for j in range(0,9,3):
        subgrid = grid[i:i+3,j:j+3]
        if len(subgrid.flatten()) != len(set(subgrid.flatten())):
            valid = False
            break

print("true" if valid else "false")
