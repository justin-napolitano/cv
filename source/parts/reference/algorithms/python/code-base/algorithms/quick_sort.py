class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        self.quickSort(nums, 0, len(nums)-1)
        
    def partition(self, nums: List[int], low: int, high: int) -> int:
        pivot = nums[high]
        i = low - 1
        

        for j in range(low,high):
            if nums[j] < pivot:
                i = i+1 
                nums[i],nums[j] = nums[j],nums[i]

        nums[i+1],nums[high] = nums[high],nums[i+1] 
        return ( i+1 ) 

    def quickSort(self, nums: List[int], low: int, high: int):
        if low < high: 
            pi = self.partition(nums,low,high)

            self.quickSort(nums, low, pi-1)
            self.quickSort(nums, pi+1, high)

def main():
    nums = [-3, 4, 9, 20, 1, -30, 100]
    Solution.sortColors(nums)

        
        