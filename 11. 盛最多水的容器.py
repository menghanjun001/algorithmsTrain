class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        if len(height)<2:
            return None
        left=0
        right=len(height)-1
        water=min(height[left],height[right])*(right-left)
        while left!=right:
            water=max(water,min(height[left],height[right])*(right-left))
            if height[right]>height[left]:
                left+=1
            else:
                right-=1
        return water





if __name__ == '__main__':
    a=Solution()
    print(a.maxArea([1,8,6,2,5,4,8,3,7]))