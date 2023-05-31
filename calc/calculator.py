import math


# add
def add(a,b):
	return int(a+b)

# subtract
def subtract(a,b):
	return int(a-b)

# multiply
def multiply(a,b):
	return int(a*b)

# divide
def divide(a,b):
	return int(a/b)

# square
def square(a):
	return int(a*a)

# square root
def square_root(a):
	return int(a**0.5)	

# cube
def cube(a):
	return int(a*a*a)

# cube root
def cube_root(a):
	return int(a**(1.0/3.0))

# power
def power(a,b):
	return int(a**b)

# mod
def mod(a,b):
	return int(a%b)

# absolute
def absolute(a):
	return int(abs(a))

# floor
def floor(a):
	return int(a//1)

# ceiling
def ceiling(a):
	return int(a//1+1)

# truncate
def truncate(a):
	return int(a//1)

# round
def round(a):
	return int(a//1+1)

# exponent	
def exponent(a):
	return int(math.exp(a))

# log
def log(a):
	return int(math.log(a))

# sine
def sine(a):
	return int(math.sin(a))

# cosine
def cosine(a):
	return int(math.cos(a))

# tangent
def tangent(a):
	return int(math.tan(a))

# inverse sine
def inverse_sine(a):
	return int(math.asin(a))

# inverse cosine
def inverse_cosine(a):
	return int(math.acos(a))


# greeting
def greetings(msg):
	return msg

