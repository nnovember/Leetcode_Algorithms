class Solution():
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """

        s_list = []
        max_length = 0

        for sub_s in s:
            if sub_s in s_list:
                print(s_list)
                print(s_list.index(sub_s)) # index of sub_s
                s_list = s_list[s_list.index(sub_s) + 1:]
            s_list.append(sub_s)
            max_length = max(max_length, len(s_list))

        return max_length

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