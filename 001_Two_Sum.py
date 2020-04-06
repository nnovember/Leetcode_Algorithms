class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        h = {}
        for i, num in enumerate(nums):
            n = target - num
            if n not in h:
                h[num] = i
            else:
                return [h[n], i]

def main():

    my_solution = Solution()

    nums = [2, 7, 11, 15]
    target = 9

    answer = my_solution.twoSum(nums, target)

    print(answer)

    return

if __name__ == "__main__":
    main()