class Solution:
    def findNumberOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        
        # If there is only one element it is the longest subsequence with count of 1.
        if n == 1:
            return 1
        
        # Use dynamic programming to build upon the max length possible from beginning to the current element (indexed by 0) including the element itself.
        # Same thing for ways to reach that element that results in the max length possible.
        dp, count = [1]*n, [0]*n
        
        # Base case: The count of the first element is always going to be 1 and the total max is always going to start as 1.
        count[0], total_max = 1, 1
        
        # O(n^2) operations to compare each element to the previous ones.
        for i in range(1, n):
            max_length = 1
            
            for j in range(i):
                if nums[j] < nums[i]:
                    temp_length = dp[j] + 1
                    
                    # If the max length is newly discovered, as in this the largest max length we've seen set the max_length and count for it using the previous element.
                    # else if the max length is same, add the count for that previous element as well.
                    if max_length < temp_length:
                        count[i] = count[j]
                        max_length = temp_length
                    elif max_length == temp_length:
                        count[i] += count[j]
            
            # This is for if there is no element smaller than the current element, set the count to 1.
            if count[i] == 0:
                count[i] = 1
            
            dp[i] = max_length
            total_max = max(total_max, max_length)
           
        # Return the sum of the counts where the max length for each element equals the overall (total) max.
        return sum(c for l, c in zip(dp, count) if l == total_max)
