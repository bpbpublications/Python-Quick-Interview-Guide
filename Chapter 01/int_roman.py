class Solution:
    def intToRoman(self, num: int) -> str:
        v = [(1000,"M"),(900,"CM"),(500,"D"),(400,"CD"),
             (100,"C"),(90,"XC"),(50,"L"),(40,"XL"),
             (10,"X"),(9,"IX"),(5,"V"),(4,"IV"),(1,"I")]
        roman_str = ''
        i = 0
        while  num > 0:
            m = v[i]
            for k in range(num // v[i][0]):
                roman_str += v[i][1]
                num -= v[i][0]
            i += 1
        return roman_str


print(Solution().intToRoman(1))
print(Solution().intToRoman(2020))
