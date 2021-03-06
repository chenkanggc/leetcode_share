#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/9/17 09:01
# @Author  : ck
"""
题目:<在排序数组中查找元素的第一个和最后一个位置>
给定一个按照升序排列的整数数组 nums，和一个目标值 target。找出给定目标值在数组中的开始位置和结束位置。

你的算法时间复杂度必须是 O(log n) 级别。

如果数组中不存在目标值，返回 [-1, -1]。

示例 1:

输入: nums = [5,7,7,8,8,10], target = 8
输出: [3,4]
示例 2:

输入: nums = [5,7,7,8,8,10], target = 6
输出: [-1,-1]
"""
from typing import List


class Solution:
    def extreme_insertion_index(self, nums: List[int], target: int, left: bool) -> int:
        lo = 0
        hi = len(nums)

        while lo < hi:
            mid = (lo + hi) // 2
            if nums[mid] > target or (left and target == nums[mid]):
                hi = mid
            else:
                lo = mid + 1
        return lo

    def searchRange(self, nums: List[int], target: int) -> List[int]:
        left_idx = self.extreme_insertion_index(nums, target, True)

        if left_idx == len(nums) or nums[left_idx] != target:
            return [-1, -1]

        return [left_idx, self.extreme_insertion_index(nums, target, False) - 1]


if __name__ == "__main__":
    s = Solution()
    nums = [5, 7, 7, 8, 8, 10]
    target = 8
    results = s.searchRange(nums, target)
    print(results)
