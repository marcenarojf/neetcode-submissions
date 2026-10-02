class Solution:
    # in nums = [], nums[i] + nums[j] == target
    # Need to return i and j
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dict_num_idx = {}
        nth_element = len(nums)-1
        # fills dict with num and idx, from first to nth element
        for idx,num in enumerate(nums):
            dict_num_idx[num] = idx

        for i in range(nth_element,0,-1): # for loop to check from nth to 1st element 
            num_j = target - nums[i]         
            if num_j in dict_num_idx:
                j = nums.index(num_j)
                if i != j:
                    return [j,i]
        return []        