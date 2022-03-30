class Solution:
    def validPath(self,n, edges, start, end):
        adjacency_list = {} 

        for a, b in edges:
            if not a in adjacency_list:
                adjacency_list[a] = [] 
            if not b in adjacency_list:
                adjacency_list[b] = [] 
            adjacency_list[a].append(b)
            adjacency_list[b].append(a)

        print(adjacency_list)
        # stack = [start] 
        # seen = set() 

        # while(len(stack) > 0):
        #     # Get the Current Node 
        #     node = stack.pop()

        #     # Check iof we have reached the target node 
        #     if node == end:
        #         return True 
            
        #     # Check if we have already visited this node 
        #     if node in seen: 
        #         continue  
        #     seen.add(node)

        #     # Add all our neighbors to our Stack 
        #     for neighbour in adjacency_list[node]:
        #         stack.append(neighbour) 

        # return False 

one = Solution()
# print(one.validPath(3,[[0,1],[1,2],[2,0]],2,0))
print(one.validPath(3,[[1,2],[2,5],[3,4],[4,5],[5,6],[7,6]],2,0))