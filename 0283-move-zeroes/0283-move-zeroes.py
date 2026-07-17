class Solution(object):
    def moveZeroes(self, nums):
        slow = 0
        i =0
        for i in range(len(nums)):
            if nums[i]!=0:
                nums[slow]= nums[i]
                slow+=1
            else:
                i+=1

        while slow< len(nums):
            nums[slow] = 0
            slow+=1


                 
                


        

       