
#complex number class

class Complex:
    """ Complex nos addition multiplication and division """

    def __init__(self, real = None, imag = None):
        self.real = real
        self.imag = imag

    def __str__(self):
        #return str(self.real) + "+" + str(self.imag)+"j"
        return "{0}+({1})i".format(self.real, self.imag)

    #Method overriding
    def __add__(self, other):
        temp = Complex()
        temp.real = self.real+other.real
        temp.imag = self.imag+other.imag
        return temp

    def __mul__(self, other):
        temp = Complex()
        temp.real = (self.real * other.real) - (self.imag * other.imag)
        temp.imag = (self.imag * other.real) + (self.real * other.imag)
        return temp



    def __truediv__(self, other):
        temp = Complex()
        (sr, si, orr, oi) = (self.real, self.imag, other.real, other.imag)
        r = float(orr**2 + oi**2)
        return Complex((sr*orr+si*oi)/r, (si*orr-sr*oi)/r)





    def __del__(self):
        pass


# uses c.__add__(d).__add__(f)
c = Complex(3 , 2)
d = Complex(1, 4)
f = Complex(5.00, 7.0)
e = c+d+f
print(e)

#multiplication
x = c.__mul__(d)
print x

#division
y = c.__truediv__(d)
print y


"""
print Complex.__doc__       #gives docstring
print c.__class__           #gives associated class
print d.__class__

print dir(c)

print c.__dict__

"""
