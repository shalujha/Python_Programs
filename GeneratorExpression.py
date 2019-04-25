#lets find the sum of first 10 natural numbers without using functions:
gen=(x**2 for x in range(1,8))
print(next(gen))
print(next(gen))
print(next(gen))
print(type(gen))
# no need to call generator expression
