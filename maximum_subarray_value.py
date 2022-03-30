# Hacker Rank 

# The value of 0 indexed 
# Square of sum of even idexed elements - sum of odd-indexed elements 

# [2,-1,4,5]
import sys 

def max_sub_array(arr):
    if len(arr) == 2:
        return (arr[0]-arr[1])**2 

    ans = 0 

    for i in range(2,len(arr)):
        temp = 0 
        while temp<i:
            even = 0 
            odd =0 
            for j in range(temp, i+1):
                if j % 2 ==0:
                    even+= arr[j] 
                else:
                    odd+= arr[j] 
            temp+=1 
            total = (even-odd)**2
            
            ans = max(ans,total)
       
    return ans 


# print(max_sub_array([3,-1,-1,-1,5,1]))
print(max_sub_array([-6,10,-1,2,10,-1]))