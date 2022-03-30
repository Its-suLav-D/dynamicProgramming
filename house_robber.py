class Solution:
    # Look up Solution  
    def rob(self,nums):
        # Base Case 

        if len(nums) == 1:
            return nums[0] 
        dp = [0] * len(nums) 
        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1]) 

        for i in range(2, len(nums)):
            dp[i] = max(dp[i-1], dp[i-2]+ nums[i]) 
        # Inductive Case  

        return dp[-1] 


one = Solution() 
one.rob([2,7,9,3,1]) # Return 12 

class Sol:
    def rob(self, nums) -> int:
        def dp(i):
            # Base cases
            if i == 0: 
                return nums[0]            
            if i == 1: 
                return max(nums[0], nums[1])            
            if i not in memo:
                memo[i] = max(dp(i - 1), dp(i - 2) + nums[i]) # Recurrence relation
            return memo[i]
        
        memo = {}
        return dp(len(nums) - 1)



