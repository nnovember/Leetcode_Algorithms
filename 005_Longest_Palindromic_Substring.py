# Best : Manacher's algorithm, O(n)
# Palindrome(좌우 대칭, 뒤집어도 똑같은 것)

class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """

        if not s: return s

        for l in range(len(s),0,-1):
            for i in range(len(s) - l + 1):
                j = i + l
                if s[i:j] == s[i:j][::-1]:
                    return s[i:j]
                else:
                    continue

    def longestPalindrome2(self, s):
        """
        :type s: str
        :rtype: str
        """
        m = ''  # Memory to remember a palindrome
        for i in range(len(s)):  # i = start, O = n
            for j in range(len(s), i, -1):  # j = end, O = n^2
                if len(m) >= j - i:  # To reduce time
                    break
                elif s[i:j] == s[i:j][::-1]:
                    m = s[i:j]
                    break
        return m

    def longestPalindrome3(self, s):
        """
        :type s: str
        :rtype: str
        """

        if not s:
            return ''
        l = len(s)

        max_p = ''
        i = 0
        while i < l:
            print("{} == {}".format(s[i - 2], s[i]))
            if i > 1 and s[i - 2] == s[i]:
                k = 1
                while i - 2 - k >= 0 and i + k < l and s[i - 2 - k] == s[i + k]:
                    k += 1

                if 2 * k + 2 > len(max_p):
                    max_p = s[i - 2 - k + 1:i + k]

            print("{} == {}".format(s[i - 1], s[i]))
            if i > 0 and s[i - 1] == s[i]:
                k = 1
                while i - 1 - k >= 0 and i + k < l and s[i - 1 - k] == s[i + k]:
                    k += 1

                if 2 * k + 1 > len(max_p):
                    max_p = s[i - 1 - k + 1:i + k]

            i += 1

        if not max_p:
            return s[0]
        return max_p

    def longestPalindrome4(self, s):
        if len(s) <= 1:
            return s
        i,l=0,0 # 시작 index, 길이
        for j in range(len(s)): # j로 s를 순회하면서
            # print("{} == {}".format(s[j-l: j+1], s[j-l: j+1][::-1]))
            # print("{} == {}".format(s[j-l-1: j+1],s[j-l-1: j+1][::-1]))
            if s[j-l: j+1] == s[j-l: j+1][::-1]:
                i, l = j-l, l+1
                # print(s[i: i+l])
            elif j-l > 0 and s[j-l-1: j+1] == s[j-l-1: j+1][::-1]:
                i, l = j-l-1, l+2
                # print(s[i: i+l])
        return s[i: i+l] # 가장 긴 substring의 시작index는 i, 그 길이는 l



    # Manacher algorithm
    # http://en.wikipedia.org/wiki/Longest_palindromic_substring

    def longestPalindrome5(self, s):
        # Transform S into T.
        # For example, S = "abba", T = "^#a#b#b#a#$".
        # ^ and $ signs are sentinels appended to each end to avoid bounds checking
        T = '#'.join('^{}$'.format(s))
        n = len(T)
        P = [0] * n
        C = R = 0
        for i in range(1, n - 1):
            P[i] = (R > i) and min(R - i, P[2 * C - i])  # equals to i' = C - (i-C)
            # Attempt to expand palindrome centered at i
            while T[i + 1 + P[i]] == T[i - 1 - P[i]]:
                P[i] += 1

            # If palindrome centered at i expand past R,
            # adjust center based on expanded palindrome.
            if i + P[i] > R:
                C, R = i, i + P[i]

        # Find the maximum element in P.
        maxLen, centerIndex = max((n, i) for i, n in enumerate(P))
        return s[(centerIndex - maxLen) // 2: (centerIndex + maxLen) // 2]

def main():

    my_solution = Solution()

    s1 = "babad" # bab or aba
    s2 = "cbbd"  # bb
    s3 = "ahtrexyzzyxgeruioh"
    s4 = "ujtofmboiyyrjzbonysurqfxylvhuzzrzqwcjxibhawifptuammlxstcjmcmfvjuphyyfflkcbwimmpehqrqcdqxglqciduhhuhbjnwaaywofljhwzuqsnhyhahtkilwggineoosnqhdluahhkkbcwbupjcuvzlbzocgmkkyhhglqsvrxsgcglfisbzbawitbjwycareuhyxnbvounqdqdaixgqtljpxpyrccagrkdxsdtvgdjlifknczaacdwxropuxelvmcffiollbuekcfkxzdzuobkrgjedueyospuiuwyppgiwhemyhdjhadcabhgtkotqyneioqzbxviebbvqavtvwgyyrjhnlceyedhfechrbhugotqxkndwxukwtnfiqmstaadlsebfopixrkbvetaoycicsdndmztyqnaehnozchrakt"

    # answer1 = my_solution.longestPalindrome4(s1)
    # answer2 = my_solution.longestPalindrome4(s2)
    # answer3 = my_solution.longestPalindrome4(s3)
    answer4 = my_solution.longestPalindrome5(s4)

    # print(answer1)
    # print(answer2)
    # print(answer3)
    print(answer4)

    return

if __name__ == "__main__":
    main()