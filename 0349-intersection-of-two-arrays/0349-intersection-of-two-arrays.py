class Solution(object):
    def intersection(self, nums1, nums2):
        seen = set()
        ls = []
        for i in range(len(nums1)):
            if nums1[i] not in seen:
                seen.add(nums1[i])

        for i in range(len(nums2)):
            if nums2[i] in seen and nums2[i] not in ls:
                ls.append(nums2[i])
            
        return ls
                
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        