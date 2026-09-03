class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        c,m=0,0
        for i in nums:
            if i==1:
                c+=1
                print(i,c)
            else:
                m=max(c,m)
                print(m)
                c=0
        return max(c,m)