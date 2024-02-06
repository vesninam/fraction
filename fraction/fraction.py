class Fraction:
   def __init__(self, numerator, denominator):
       self.numerator = numerator
       self.denominator = denominator
       if self.denominator < 0:
               self.denominator = \
                   abs(self.denominator)
               self.numerator = -1*self.numerator
       elif self.denominator == 0:
           raise ZeroDivisionError



