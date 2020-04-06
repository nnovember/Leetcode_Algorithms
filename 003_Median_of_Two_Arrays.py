# https://www.youtube.com/watch?v=LPFhl65R7ww

class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        A = nums1
        B = nums2
        m, n = len(A), len(B)
        if m > n: # always n > m, binary search for smaller list
            A, B, m, n = B, A, n, m
        if n == 0:
            raise ValueError

        imin, imax, half_len = 0, m, (m + n + 1) // 2 # it works for both odd and even cases
        while imin <= imax:
            i = (imin + imax) // 2 # partition in A
            j = half_len - i       # partition in B
            if i < m and B[j-1] > A[i]:
                # i is too small, must increase it
                imin = i + 1
            elif i > 0 and A[i-1] > B[j]:
                # i is too big, must decrease it
                imax = i - 1
            else:
                # i(partition for division) is perfect

                if i == 0: max_of_left = B[j-1]
                elif j == 0: max_of_left = A[i-1]
                else: max_of_left = max(A[i-1], B[j-1])

                if (m + n) % 2 == 1: # odd
                    return max_of_left

                if i == m: min_of_right = B[j]
                elif j == n: min_of_right = A[i]
                else: min_of_right = min(A[i], B[j])

                return (max_of_left + min_of_right) / 2.0

def main():

    my_solution = Solution()

    num1 = [1, 3, 4, 6, 2]
    num2 = [2]

    num3 = [1, 2]
    num4 = [3, 4]

    num5 = [23, 26, 31, 35]
    num6 = [3, 5, 7, 9, 11, 16]

    answer1 = my_solution.findMedianSortedArrays(num1, num2)
    answer2 = my_solution.findMedianSortedArrays(num3, num4)
    answer3 = my_solution.findMedianSortedArrays(num5, num6)
    print(answer1)
    print(answer2)
    print(answer3)

    return

if __name__ == "__main__":
    main()