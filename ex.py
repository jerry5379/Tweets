class Solution:
    def solve(self, nums):
        print(len(nums))
        arr = [0]*(len(nums)+1)
        # print(arr)
        for i in nums:
            arr[i] += 1
            print(arr)
            missing = []
        for i in range(len(arr)):
            if arr[i] == 0 and i != 0:
                missing.append(i)
        return missing
ob = Solution()
print(ob.solve([4, 4, 2, 2]))