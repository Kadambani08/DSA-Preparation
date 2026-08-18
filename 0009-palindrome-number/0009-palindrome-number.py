class Solution(object):
    def isPalindrome(self, x):
        text = str(x)
        return text == text[::-1]

        """
        :type x: int
        :rtype: bool
        """
        