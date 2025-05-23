'''
script: Class Fraction
action: a) uses the fractions module to manipulate and print fractions
        b) uses built-in type complex to manipulate and print complex numbers
author: Branden Duval
date:   03/11/2025
'''

# importing the necessary modules
from fractions import Fraction as fns

#Part 1: FRACTIONS
fractionA = fns(2, 4) # storing the first fraction
fractionB = fns(6, 7) # storing the second fraction

# Part 1A: Adding two fractions
print(fractionA, '+', fractionB, '=', fractionA + fractionB)

# Part 1B: Subtracting two fractions
print(fractionA, '-', fractionB, '=', fractionA - fractionB)

# Part 1C: Multiplying two fractions
print(fractionA, '*', fractionB, '=', fractionA * fractionB)

# Part 1D: Dividing two fractions
print(fractionA, '/', fractionB, '=', fractionA / fractionB)

# Part 1E: Printing fractions in the form a/b, where a is the numerator and b is the denominator
print('Fraction A:', fractionA)
print('Fraction B:', fractionB)

# Part 1F: Converting fractions to floating-point numbers with built-in function float
print('Fraction A converted to a decimal:', float(fractionA))
print('Fraction B converted to a decimal:', float(fractionB))

# Part 2: BUILT-IN TYPE COMPLEX
cplx1 = complex(5, 8) # creates and stores the first complex number as cplx1
cplx2 = complex(7, 2) # creates and stores the second complex number as cplx2

# Part 2A: Adding two complex numbers
print(cplx1, '+', cplx2, '=', cplx1 + cplx2)

# Part 2B: Subtracting two complex numbers
print(cplx1, '-', cplx2, '=', cplx1 - cplx2)

# Part 2C: Printing complex numbers
print('Complex number 1:', cplx1)
print('Complex number 2:', cplx2)

# Part 2D: Getting the real and imaginary parts of the complex numbers
print('The real number in', cplx1, 'is', cplx1.real)
print('The imaginary number in', cplx1, 'is', cplx1.imag)
print('The real number in', cplx2, 'is', cplx2.real)
print('The imaginary number in', cplx2, 'is', cplx2.imag)