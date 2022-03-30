# O(wh) time | O(wh) space 

'''
	[
		[1,0,0,1,0], 
		[1,0,1,0,0],
		[0,0,1,0,1],
		[1,0,1,0,1],
		[1,0,1,1,0]
	]
'''
def riverSizes(matrix):
    sizes =[] 
    visited =[[False for _ in row] for row in matrix] 

    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if visited[i][j]:
                continue  
            traverseNode(i,j,matrix,visited,sizes)
    return sizes 

def traverseNode(i,j,matrix,visited,sizes):
    currentRiverSize = 0 
    # Depth First Search  
    # Stack 
    nodeToExplore = [[i,j]]

    while len(nodeToExplore): 
        currentNode = nodeToExplore.pop()
        # row 
        i = currentNode[0] 
        # column 
        j = currentNode[1]

        if visited[i][j]:
            continue  
        visited[i][j] = True 

        if matrix[i][j] == 0:
            continue  
        
        currentRiverSize +=1 

        unvisitedNeighbors = getUnvisitedNeighbors(i,j,matrix,visited) 

        for neighbor in unvisitedNeighbors:
            nodeToExplore.append(neighbor)
        
    if currentRiverSize >0:
        sizes.append(currentRiverSize)
    

def getUnvisitedNeighbors(i,j,matrix,visited):
    unvisitedNeighbors = [] 
    
    # UP 
    if i > 0 and not visited[i-1][j]:
        unvisitedNeighbors.append([i-1,j])

    # Down  
    if i < len(matrix) -1  and not visited[i+1][j]:
        unvisitedNeighbors.append([i+1,j])

    # Left  
    if j > 0 and not visited[i][j-1]:
        unvisitedNeighbors.append([i,j-1]) 
    
    # Right 
    if j < len(matrix[0]) -1 and not visited[i][j+1]:
        unvisitedNeighbors.append([i,j+1])

    

    return unvisitedNeighbors


print(riverSizes(	[
		[1,0,0,1,0], 
		[1,0,1,0,0],
		[0,0,1,0,1],
		[1,0,1,0,1],
		[1,0,1,1,0]
	]))
