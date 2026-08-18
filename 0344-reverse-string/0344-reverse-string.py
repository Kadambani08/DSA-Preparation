class Solution(object):
    def reverseString(self, s):
        i = 0
        right = len(s)-1
        while(i<right):
                temp = s[i]
                s[i] = s[right]
                s[right] = temp
                i+=1
                right-=1
        """
        :type s: List[str]
        :rtype: None Do not return anything, modify s in-place instead.
        """
        