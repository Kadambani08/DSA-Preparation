class Solution(object):
    def maxArea(self, height):
        i = 0
        j = len(height)-1
        maxx= []
        while i<j:
            distance = j-i
            if height[i]<height[j]:
                area = height[i]*distance
                maxx.append(area)
                i+=1
            else:
                area = height[j]*distance
                maxx.append(area)
                j-=1
        
        return max(maxx)

