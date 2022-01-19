class Solution:
    def canPartition(self, nums: List[int]) -> bool:
      
        # We need to make sure that the total sum is divisigble by two and that whatever subset we form, we can equal to half of total sum
        max_num = sum(nums)
        length = len(nums)
        
        if max_num % 2 != 0:
            return False
        target = max_num // 2
        
        # Approach 1: Calculate all subset sums possible and put it in a set so that the number of operations are limited to O(n*m) where m is the total sum.
        dp = {0}

        for num in nums:
            temp_set = set()
            for subsum in dp:
                # This if statement dramatically reduces runtime.
                if subsum+num == target or num == target:
                    return True
                
                temp_set.add(subsum+num)
                temp_set.add(subsum)
            dp = temp_set
        return True if target in dp else False
      
        # Approach 2: Keep a 2d array to keep track of what subsets sums are possible after adding each element. O(n*(m/2)) 
#         dp = [[True]+([False]*target) for i in range(length)]
        
#         for i in range(length):
#             for j in range(1, target+1):
#                 if dp[i-1][j]: dp[i][j] = True
#                 elif nums[i] <= j and dp[i-1][j-nums[i]]: dp[i][j] = True
        
#         return dp[length-1][target]
