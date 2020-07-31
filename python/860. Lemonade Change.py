class Solution(object):
    def lemonadeChange(self, bills):
        """
        :type bills: List[int]
        :rtype: bool
        """

        money_5=0
        money_10=0
        money_20=0
        for i in range(len(bills)):
            if bills[i]==5:
                money_5+=1
            elif bills[i]==10:
                money_10+=1
                money_5-=1
            elif bills[i]==20:
                if money_10!=0:
                    money_20+=1
                    money_10-=1
                    money_5-=1
                else:
                    money_20+=1
                    money_5-=3
            if money_5 < 0:
                return False
        return True

if __name__ == '__main__':
    a=Solution()
    print(a.lemonadeChange(
[5,5,5,5,20,20,5,5,5,5]))


