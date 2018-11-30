#!/bin/python
# http://hr.gs/afcdbc

class Complex(complex):
    def __add__(self, no):
        return Complex(complex.__add__(self, no))

    def __sub__(self, no):
        return Complex(complex.__sub__(self, no))

    def __mul__(self, no):
        return Complex(complex.__mul__(self, no))

    def __div__(self, no):
        return Complex(complex.__div__(self, no))

    def mod(self):
        return Complex(complex.__abs__(self))

    def __str__(self):
        if self.imag == 0:
            result = "%.2f+0.00i" % (self.real)
        elif self.real == 0:
            if self.imag >= 0:
                result = "0.00+%.2fi" % (self.imag)
            else:
                result = "0.00-%.2fi" % (abs(self.imag))
        elif self.imag > 0:
            result = "%.2f+%.2fi" % (self.real, self.imag)
        else:
            result = "%.2f-%.2fi" % (self.real, abs(self.imag))
        return result

if __name__ == '__main__':
    c = map(float, raw_input().split())
    d = map(float, raw_input().split())
    x = Complex(*c)
    y = Complex(*d)
    print '\n'.join(map(str, [x+y, x-y, x*y, x/y, x.mod(), y.mod()]))
