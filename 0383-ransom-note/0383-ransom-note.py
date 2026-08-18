class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        count = {}

        for char in magazine:
            if char not in count:
                count[char] = 1
            else:
                count[char] += 1

        for char in ransomNote:
            if char not in count:
                return False

            if count[char] == 0:
                return False

            count[char] -= 1

        return True