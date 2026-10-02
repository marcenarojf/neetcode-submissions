class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        duplicate = False
        temp_dict = {}
        for num in nums:
            if num in temp_dict:
                temp_dict[num] = True
                duplicate = True
                return duplicate
            else:
                temp_dict[num] = False
        return duplicate