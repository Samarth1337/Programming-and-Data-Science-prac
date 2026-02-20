# Implement Quicksort

class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        def partition(low: int, high:int):
            pivot = nums[high]
            i = low
            for j in range(low, high):
                if nums[i] < pivot:
                    nums[i], nums[j] = nums[j], nums[i]
                    i += 1
            nums[i], nums[high] = nums[high], nums[i]
            return i
        def quickSort( low:int, high: int):
            if low < high:
                p = partition(low, high)
                quickSort(low, p-1)
                quickSort(p+1, high)
        quickSort(0, len(nums)-1)
        return nums
