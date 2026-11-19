class Solution:
    def isPalindrome(self, s: str) -> bool:
        sChars = []
        for char in s:
            if char.isalnum():
                sChars.append(char)
        reverseChars = sChars.copy()
        reverseChars.reverse()
        sString = ''.join(sChars)
        reverseString = ''.join(reverseChars)
        print(sString)
        print(reverseString)
        return sString.lower() == reverseString.lower()

