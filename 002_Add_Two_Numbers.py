# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        result = ListNode(0)
        result_tail = result
        carry = 0

        while l1 or l2 or carry:
            val1 = (l1.val if l1 else 0)
            val2 = (l2.val if l2 else 0)
            carry, out = divmod(val1 + val2 + carry, 10)
            # divmod is built-in function which returns and the quotient and the remainder

            result_tail.next = ListNode(out)
            result_tail = result_tail.next

            l1 = (l1.next if l1 else None)
            l2 = (l2.next if l2 else None)

        return result.next

def main():
    my_solution = Solution()

    s1 = "abcabcbb"
    s2 = "bbbbbb"
    s3 = "pwwkew"

    answer1 = my_solution.lengthOfLongestSubstring(s1)
    answer2 = my_solution.lengthOfLongestSubstring(s2)
    answer3 = my_solution.lengthOfLongestSubstring(s3)

    print(answer1)
    print(answer2)
    print(answer3)

    return

if __name__ == "__main__":
    main()