# Given an integer array nums and an integer k, return the k most frequent elements within the array.

# The test cases are generated such that the answer is always unique.

# You may return the output in any order.

# Example 1:

# Input: nums = [1,2,2,3,3,3], k = 2

# Output: [2,3]
# Example 2:

# Input: nums = [7,7], k = 1

# Output: [7]
# Constraints:

# 1 <= nums.length <= 10^4.
# -1000 <= nums[i] <= 1000
# 1 <= k <= number of distinct elements in nums.

class Solution:
    def topKFrequent(self, nums,k):
        number_count={}
        output_list=[]
        for num in nums:
            if num in number_count:
                number_count[num]+=1
            else:
                number_count[num]=1

        for i in range(k):
            greatest_count=0
            largest_number=None

            for number, count in number_count.items():
                if count > greatest_count:
                    greatest_count=count
                    largest_number=number

            output_list.append(largest_number)
            number_count.pop(largest_number)

        return output_list
        

nums = [1,2,2,3,3,3]
k = 2
sol_instance=Solution()
print(sol_instance.topKFrequent(nums,k))