class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if numRows is 1:
            return s

        main_i, main_j = divmod(len(s), numRows + numRows - 2)
        tail_i, tail_j = divmod(main_j, numRows)

        list_return = [[0 for col in range((1 + numRows - 2) * main_i + (1 * tail_i) + tail_j)] for row in range(numRows)]

        i, row, col = 0, 0, 0
        direction = True
        for i in range(len(s)):
            if direction:
                if row < numRows - 1:
                    list_return[row][col] = s[i]
                    row += 1
                else:
                    list_return[row][col] = s[i]
                    row -= 1
                    col += 1
                    direction = False
            else:
                if row > 0:
                    list_return[row][col] = s[i]
                    row -= 1
                    col += 1
                else:
                    list_return[row][col] = s[i]
                    row += 1
                    direction = True
            i += 1

        string_return = ""
        for row in range(len(list_return)):
            for col in range(len(list_return[0])):
                if list_return[row][col]:
                    string_return = string_return + str(list_return[row][col])
        return string_return

    def convert2(self, s, numRows):
        """
                :type s: str
                :type numRows: int
                :rtype: str
                """
        lin = 0
        pl = 1
        outp = [""] * numRows
        for i in range(len(s)):
            outp[lin] += s[i]
            if numRows > 1:
                lin += pl
                if lin == 0 or lin == numRows - 1:
                    pl *= -1
        outputStr = ""
        for j in range(numRows):
            outputStr += outp[j]
        return outputStr

    def convert3(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if numRows == 1 or numRows >= len(s):
            return s

        L = [''] * numRows
        index, step = 0, 1

        for x in s:
            L[index] += x
            if index == 0:
                step = 1
            elif index == numRows -1:
                step = -1
            index += step

        return ''.join(L)

def main():

    my_solution = Solution()

    s1 = "PAYPALISHIRING" # len(s1) = 14
    answer1 = my_solution.convert3(s1, 4)

    print(answer1)

    return

if __name__ == "__main__":
    main()