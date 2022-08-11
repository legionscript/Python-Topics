def my_func(*args, **kwargs):
    pass

"""
    *args -> positional argument collector,
        collects all positional arguments after the already defined positional arguments
        
        example: def test_func(var1, var2, var3):


    **kwargs -> keyword argument collector,
        collects all keyword arguments after the already defined positional arguments
        
        example def test_func(var1='hello', var2='world)
"""

def my_function(var1, var2, *args):
    print(args[0], args[1])
    print(var1, var2)

# my_function('abc', 'def', 'hello', 'world')

def my_function2(var1, text='test',*args, **kwargs):
    print(kwargs)

# my_function2('abc', hello='world')

def add_numbers(*args):
    total = 0

    for number in args:
        total += number

    return total

print(add_numbers(1))

