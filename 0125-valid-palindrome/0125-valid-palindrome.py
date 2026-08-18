class Solution(object):
    def isPalindrome(self, s):
        s = s.lower()
        test = ""

        for char in s:
            if char.isalnum():
                test += char

        return test == test[::-1]