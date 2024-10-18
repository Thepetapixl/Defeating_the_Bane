class Solution:
    def countMaxOrSubsets(self, nums: List[int]) -> int:
        self.maxi = 0
        self.count = 0
        self.backtrack(0 , 0, nums)
        return self.count
    
    def backtrack(self, index: int, curr_or: int, nums: List[int]):
        
        if index == len(nums):

            if curr_or > self.maxi:
                self.maxi = curr_or
                self.count = 1
            elif curr_or == self.maxi:
                self.count += 1
            return
        
        self.backtrack(index + 1, curr_or | nums[index], nums)

        self.backtrack(index + 1, curr_or, nums)

