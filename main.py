class Solution:
    def romanToInt(self, s: str) -> int:
        summary = 0
        roman = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
        }
        for index in range(len(s)-1):
            if roman[s[index]] < roman[s[index+1]]:
                summary -= roman[s[index]]
            else:
                summary += roman[s[index]]
        return summary+roman[s[-1]]


x = Solution()
print(x.romanToInt("LVIII"))
