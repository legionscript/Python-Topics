# Decorators

# def outer_function():
# 	def inner_function():
# 		print('from the inner function')
# 	inner_function()

# print(outer_function())

# This won't work
# inner_function()

# def logging_decorator(func):
# 	def inner_function(*args, **kwargs):
# 		print('logging before the function is called')
# 		returned_value = func(*args, **kwargs)
# 		print('logging after the function is called')
# 		return returned_value
# 	return inner_function

# @logging_decorator
# def add(a, b):
# 	print(a + b)

# add(2, 2)

def triple(func):
	def inner_function(*args, **kwargs):
		returned_value = func(*args, **kwargs)

		return returned_value * 3

	return inner_function

@triple
def add(a, b):
	return a + b

print(add(2, 8))