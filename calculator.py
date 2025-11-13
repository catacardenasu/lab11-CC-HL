#https://github.com/catacardenasu/lab11-CC-HL
#Partner 1: Catalina Cardenas
#Partner 2: Hanyu Luo
"""
calculator.py
- Defines functions used to create a simple calculator

One function per operation, in order.
"""

# First example
import math
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def mul(a, b):
    return a * b

def div(a, b):
    return b / a # raise ZeroDivisionError if a == 0

def logarithm(a, b):
    if a <= 0 or a == 1 or b <= 0:
        raise ValueError("Input must be a positive number.")
    return math.log(b,a)
def exp(a, b):
    return a**b

def square_root(a):
    return math.sqrt(a)# raise ValueError if a < 0
def hypotenuse(a, b):
    return math.hypot(a, b) # can have negative nums





