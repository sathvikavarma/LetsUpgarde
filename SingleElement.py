###
Given an integer array nums where every element appears three times except for one, which appears exactly once. Find the single element and return it.

Example 1:

Input: nums = [2,2,3,2]
Output: 3
Example 2:

Input: nums = [0,1,0,1,0,1,99]
Output: 99

Soln1:Linear time complexity O(n)
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        return (3*sum(set(nums))  - sum(nums))//2
  
  
 Soln2: Space complexity O(1):
 class Solution:
    def singleNumber(self, nums):
        hashmap={}
        for v in nums:
            if v in hashmap:
                hashmap[v]+=1
            else:
                hashmap[v]=1
        for k in hashmap.keys():
            if hashmap[k]==1:
                return k
  
