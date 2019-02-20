# -*- coding: utf-8 -*-
# -*- coding: utf-8 -*-
#!usr/bin/env python 3

# Script for ME 599 lab 5
# Jonathan Bonebrake

class Complex():    
    def __init__(self,re = 0, im = 0):   
        # default values for real ad imaginary parts are zero
        self.re = re
        self.im = im

    def __repr__(self):
        # Note that only the representation of the complex number is truncated
        # to 6 decimals. Precision is maintained in the instance itself
        re = ()
        im = ()
        #first check to see if re, im are integers, and format accordingly
        if self.re % 1 == 0:
            re = "%0.f" % (self.re)
        else:
            re = "%0.6f" % (self.re)
            
        if self.im % 1 == 0:
            im = "%0.f" % abs((self.im))        
        else:
            im = "%0.6f" % abs((self.im))     
            
        # stick everything together, with appropriate sign for im
        if self.im < 0:       
            return str('('+re + '-' + im+'i'+')')
        if self.im >= 0:
            return str('('+re + '+' + im+'i'+')')

    def __str__(self):
        return self.__repr__()
#    def __repr__(self):
#        # Note that only the representation of the complex number is truncated
#        # to 2 decimals. Precision is maintained in the instance itself
#        return "Complex(%1.2f + %1.2fi)" % (self.re, self.im)
#        
#    def __str__(self):
#        # Note that only the string for the complex number is truncated
#        # to 2 decimals. Precision is maintained in the instance itself        
#        if self.im < 0:
#            return "(%1.2f - %1.2fi)" % (self.re, abs(self.im))
#        else:
#            return "(%1.2f + %1.2fi)" % (self.re, self.im)
    
    def __add__(self,other):
        # addition operator for Complex class
        d = Complex()
        try: 
            d.re = self.re + other.re
            d.im = self.im + other.im
        except:
            return self + Complex(other)
        return d
    
    def __radd__(self,other):
        # right addition operator for Complex class
        return self + other

    def __sub__(self,other):
        # subtraction operator for Complex class
        d = Complex()
        try: 
            d.re = self.re + (-1)*other.re
            d.im = self.im + (-1)*other.im
        except:
            return self - Complex(other)            
        return d
    
    def __rsub__(self,other):
        # right subtraction operator for Complex class 
        return Complex(other)-self
    
    def __mul__(self,other):
        # multiplication operator for Complex class
        # math from: http://www.mesacc.edu/~scotz47781/mat120/notes/complex/multiplying/multiplying_complex.html
        d = Complex()
        try:
            d.re = self.re*other.re - self.im*other.im
            d.im = self.re*other.im + self.im*other.re

        except:
            return self*Complex(other)
        return d
    
    def __rmul__(self,other):
        # right multiply operator for Complex class
        return self*other
    
    def __truediv__(self,other):
        # division operator for Complex class
        # math from: http://www.mesacc.edu/~scotz47781/mat120/notes/complex/dividing/dividing_complex.html
        d = Complex()
        try:
            num = self*(~other)
            den = other.re*other.re + other.im*other.im
            d.re = num.re*den**(-1)
            d.im = num.im*den**(-1)
                                
        except:
            return self/Complex(other)
        
        return d
            
    def __invert__(self):
        # inversion (complex conjugate) operator for Complex class
        return Complex(self.re,(-1)*self.im)
    
    def __neg__(self):
        # negation operator from Complex class
        return Complex(0-self.re,0-self.im)
    
if __name__ == '__main__':
      
    a = Complex(2,1)
    b = Complex(-2,1)

    ap = complex(2,1)
    bp = complex(-2,1)
    
    print('tests for class Complex')
    print('syntax: my class printed first, then the built-in class')
    
    print('\n--test addition--')
    print('a+b:')
    print(a+b)
    print(ap+bp)
    print('a+4:')
    print(a+4)
    print(ap+4)
    print('4+a:')
    print(4+a)
    print(4+ap)
    
    print('\n--test subtraction--')
    print('a-b:')
    print(a-b)
    print(ap-bp)
    print('a-4:')
    print(a-4)
    print(ap-4)
    print('4-a:')
    print(4-a)
    print(4-ap)

    print('\n--test multiplication--')
    print('a*b:')
    print(a*b)
    print(ap*bp)
    print('b*a:')
    print(b*a)
    print(bp*ap)
    
    print('\n--test division--')
    print('a/b:')
    print(a/b)
    print(ap/bp)
    print('b/a:')
    print(b/a)
    print(bp/ap)
    
    print('\n--test negation--')
    print('b:')
    print(b)
    print('-b:')
    print(-b)
    print(-bp)
    
    print('\n--test complex conjugate--')
    print('b:')
    print(b)
    print('~b:')
    print(~b)
    
