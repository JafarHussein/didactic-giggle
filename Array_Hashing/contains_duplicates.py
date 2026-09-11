# Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.

 

# Example 1:

# Input: nums = [1,2,3,1]

# Output: true

# Explanation:

# The element 1 occurs at the indices 0 and 3.

# Example 2:

# Input: nums = [1,2,3,4]

# Output: false

# Explanation:

# All elements are distinct.

# Example 3:

# Input: nums = [1,1,1,3,3,4,3,2,4,2]

# Output: true

class Solution(object):
    def containsDuplicate(self, nums):
        empty_set=set()

        for i in range(0, len(nums)):
            if nums[i] not in empty_set:
                empty_set.add(nums[i])
                continue
            else:
                return True
        return False

nums = [1,1,1,3,3,4,3,2,4,2]
sol_instance=Solution()
print(sol_instance.containsDuplicate(nums))
        

 