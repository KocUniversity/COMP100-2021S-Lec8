#################
## EXAMPLE: simple class to represent fractions
## Try adding more built-in operations like multiply, divide
### Try adding a reduce method to reduce the fraction (use gcd)
#################
class Fraction(object):
  """
  A number represented as a fraction
  """
  def __init__(self, num, denom):
    """ num and denom are integers """
    assert type(num) == int and type(denom) == int, "ints not used"
    self.num = num
    self.denom = denom
    self.reduce()
      
  def __str__(self):
    """ Retunrs a string representation of self """
    return str(self.num) + "/" + str(self.denom)

  def __add__(self, other):
    """ Returns a new fraction representing the addition """
    # a/b+c/d
    # (a*d + c*b) / (b*d) 
    top = self.num*other.denom + self.denom*other.num
    bott = self.denom*other.denom
    return Fraction(top, bott)

  def __sub__(self, other):
    """ Returns a new fraction representing the subtraction """
    top = self.num*other.denom - self.denom*other.num
    bott = self.denom*other.denom
    return Fraction(top, bott)

  def __mul__(self, other):
    """ Return a new fraction representing the multiplication """
    top = self.num*other.num
    bott = self.denom*other.denom
    return Fraction(top, bott)

  def __truediv__(self, other):
    top = self.num * other.denom
    bott = self.denom * other.num
    return Fraction(top, bott)

  def __float__(self):
    """ Returns a float value of the fraction """
    return self.num/self.denom

  def reduce(self):
    """ Reduces the fraction using gcd """
    def gcd(a,b):
      if b == 0:
        return a
      else:
        return gcd(b, a%b)
    num_denom_gcd = gcd(self.num, self.denom)
    self.num = self.num // num_denom_gcd
    self.denom = self.denom // num_denom_gcd
    
  def inverse(self):
    """ Returns a new fraction representing 1/self """
    return Fraction(self.denom, self.num)

a = Fraction(1,4)
b = Fraction(3,4)
c = a + b # c is a Fraction object
print(c)
print(float(c))
print(Fraction.__float__(c))
print(Fraction.__sub__(b,a))
c = Fraction(3.14, 2.7) # assertion error
# print(a/b) # error, did not define how to multiply two Fraction objects