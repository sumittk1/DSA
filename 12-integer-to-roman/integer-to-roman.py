class Solution(object):

    def intToRoman(self, num):
        a = [1000,900,500,400,100,90,50,40,10,9,5,4,1]
        b = ['M','CM','D','CD','C','XC','L','XL','X','IX','V','IV','I']
        c=[]
        for a,i in zip(a,b):
            while num>=a:
                num-=a
                c.append(i)
        d="".join(c)
        return d