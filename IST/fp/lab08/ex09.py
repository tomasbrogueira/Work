import unittest

def gcd(a : int, b : int):
    while b != 0:
        a, b = b, a % b
    return a

class Racional:

    def __init__(self,num,den):
        if den == 0:
            raise ValueError
        div = gcd(num,den)
        self.num = num//div
        self.den = den//div
    
    def nume(self):
        return self.num
    
    def deno(self):
        return self.den
    
    def real(self):
        return self.num/self.den
    
    def __add__(self,other):
        return Racional(self.num*other.den + self.den*other.num,self.den*other.den)

    def __mul__(self,other):
        return Racional(self.num*other.num,self.den*other.den)

    def __eq__(self, other) -> bool:
        return self.num == other.num and self.den ==other.den
    
    def __ne__(self, other) -> bool:
        return not self == other

    def __repr__(self):
        return str(self.num)+'/'+str(self.den)

def rac_inverso(b):
    return Racional(b.den,b.num)
   
if __name__ == '__main__':
    unittest.main()
