class Solution:
    def search(self, nums: list[int], target: int) -> int:
        # Need to split array into 2
        n = len(nums)
        start = 0
        i=0
        num = nums[i]
        while(n>0):
            # identify mid element, if even or odd number of elements
            i = int((start+n)/2)
            # compare to half element
            num = nums[i]
            if target < num:
                n = i
            else:
                if start != i:
                    start = i
                else:
                    if target == num:
                        return i
                    else:
                        return -1
        
        return i if target == num else -1