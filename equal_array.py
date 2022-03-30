import sys 
from collections import defaultdict 

# [64,30,25,33]

def min_Operations(arr, threshold, d):
    dp = defaultdict(lambda:[0,0])
    ans = sys.maxsize

    for x in arr:
        steps = 0 
        while True:
            dp[x][0] += 1 
            dp[x][1] += steps 

            if dp[x][0] >= threshold:
                ans = min(ans,dp[x][1])
            if x == 0:
                break 
            x // d  
            steps+=1 
    return ans 


min_Operations([64,30,25,33],2,2)