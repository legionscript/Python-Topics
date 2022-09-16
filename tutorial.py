# small anonymous function (function without a name)

# var_name = lambda var : expression

subtract_5 = lambda x : x - 5

multi_vars = lambda x, y, z : (x*2, y*2, z*2)

# def multi_vars(x,y,z):
# 	return (x*2, y*2, z*2)

def add_number(num):
	return lambda x : x + num

add_five = add_number(5)

add_three = add_number(3)

# print(add_five(15))
# print(add_three(20))

def multiply(num):
	return lambda number : number * num

double = multiply(2)
triple = multiply(3)

print(double(10))