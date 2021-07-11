class Solution(object):
    def findStartingIndex(self, nums, target):
        index = -1
        left, right = 0, len(nums)-1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                index = mid
                right = mid - 1
            elif nums[mid] > target:
                right = mid - 1
            else:
                left = mid + 1
        return index


    def findEndingIndex(self, nums, target):
        index = -1
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                index = mid
                left = mid + 1
            elif nums[mid] > target:
                right = mid - 1
            else:
                left = mid + 1
        return index

    def searchRange(self, nums, target):
        result = [-1, -1]
        result[0] = self.findStartingIndex(nums, target)
        result[1] = self.findEndingIndex(nums, target)
        return result