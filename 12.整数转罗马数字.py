class Solution(object):

    def intToRoman(self,num):
        """
        :type num: int
        :rtype: str
        """
        c={0:("","I","II","III","IV","V","VI","VII","VIII","IX"),
           1:("","X","XX","XXX","XL","L","LX","LXX","LXXX","XC"),
           2:("","C","CC","CCC","CD","D","DC","DCC","DCCC","CM"),
           3:("","M","MM","MMM")}
        roman=[]
        roman.append(c[3][num//1000])
        roman.append(c[2][num//100%10])
        roman.append(c[1][num//10%10])
        roman.append(c[0][num%10])
        return "".join(roman)
