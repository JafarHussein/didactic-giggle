# Given an array nums of size n, return the majority element.

# The majority element is the element that appears more than ⌊n / 2⌋ times in the array. You may assume that the majority element always exists in the array.

# Example 1:

# Input: nums = [5,5,1,1,1,5,5]

# Output: 5
# Example 2:

# Input: nums = [2,2,2]

# Output: 2
# Constraints:

# 1 <= nums.length <= 50,000
# -1,000,000,000 <= nums[i] <= 1,000,000,000
# Follow-up: Could you solve the problem in linear time and in O(1) space?


class Solution:
    def majorityElements(self, nums):
        all_nums_counter={}
        
        for num in nums:
            if num in all_nums_counter:
                all_nums_counter[num]+=1
            else:
                all_nums_counter[num]=1
                
        for key, value in all_nums_counter.items():
            
            if value > len(nums)/2:
                return key
            
nums = [2,2,2]
sol_instance=Solution()
print(sol_instance.majorityElements(nums))

