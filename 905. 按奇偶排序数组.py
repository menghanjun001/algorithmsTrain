class Solution:
    def sortArrayByParity(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        ou=[]
        ji=[]
        for i in A:
            if i&1==0:
                ou.append(i)
            else:
                ji.append(i)
        return ou+ji