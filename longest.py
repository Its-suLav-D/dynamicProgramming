def renameFile(newName, oldName):
    # Write your code here
    n = len(newName)
    m = len(oldName)
    
    lookup = [[0]* (n+1) for i in range(m+1)]
    
    for i in range(m+1):
        lookup[i][0] =1
        
    for row in range (1,m+1):
        for col in range(1,n+1):
            nextIndex = lookup[row-1][col]
            prevIndex = lookup[row-1][col-1]
            if oldName[row-1] == newName[col-1]:
                lookup[row][col] = prevIndex + nextIndex
            else:
                lookup[row][col] = nextIndex 
                
    return lookup[m][n]

print(renameFile('ab','aba'))