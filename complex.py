

class Complex:
    def __init__(self, real = None, imag = None):
        self.real = real
        self.imag = imag

    def __str__(self):
        #return str(self.real) + "+" + str(self.imag)+"j"
        return "{0}+{1}j".format(self.real, self.imag)

    #Method overriding
    def __add__(self, other):
        temp = Complex()
        temp.real = self.real+other.real
        temp.imag = self.imag+other.imag
        return temp

    def __mul__(self):
        pass

    def __truediv__(self):
        pass
    def __del__(self):
        pass


# uses c+__add__(d)+__add__(f)
c = Complex(4.15, 5.0)
d = Complex(4.15, 6.0)
f = Complex(5.00, 7.0)
e = c+d+f
print(e)
