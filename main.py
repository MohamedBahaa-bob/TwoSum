# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import copy


class Solution:
    def twoSum(self, nums, target):
        copied = copy.deepcopy(nums)
        nums.sort()
        i = 0
        j = len(nums) - 1
        found = False
        while i != j:
            res = nums[i] + nums[j]
            if res < target:
                i += 1
            else:
                if res > target:
                    j -= 1
                else:
                    found = True
                    break
        if found:
            num1 = nums[i]
            num2 = nums[j]
            found1 = False
            found2 = False
            for i in range(0, len(copied)):
                if num1 == copied[i] and not found1:
                    m = i
                    found1 = True
                else:
                    if num2 == copied[i] and not found2:
                        n = i
                        found2 = True
                if found1 and found2:
                    break
            return [m, n]


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    obj = Solution()
    print(obj.twoSum([3, 3], 6))

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
