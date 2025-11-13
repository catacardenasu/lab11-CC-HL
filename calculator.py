"""
calculator.py
- Defines functions used to create a simple calculator

One function per operation, in order.
"""

# First example
import math
def add(a, b):
    return a + b

def sub(a, b):
    return a - b

def mul(a, b):
    return a * b

def div(a, b):
    return b / a # raise ZeroDivisionError if a == 0

def log(a, b):
    return math.log(b,a)# use math library + raise ValueError
    if a <= 0 or a == 1 or b <= 0:
        raise ValueError("Input must be a positive number.")


def exp(a, b):
    return math.power(a, b)
import math
def add(a, b): 
    return a + b
def sub(a, b):
    return a - b
def mul(a, b):
    return a * b

def log(a, b):
    if a <= 0 or a == 1 or b <= 0:
        raise ValueError("value error")
    return math.log(b, a)
def exp(a, b):
    return a**b




