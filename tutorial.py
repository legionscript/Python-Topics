"""
Dictionary Example:

{
	'a': 'abc',
	'b': 'def',
	'c': 'ghi'
}
"""

employee = {
	'name': 'Bob',
	'title': 'Software Developer',
	1: 22
}


employee['email'] = 'test@test.com'
employee.update({'name': 'Bobby', 'title': 'Software Engineer', 'phone': '111-1111'})

phone = employee.pop('phone')
# print(phone)
# print(employee)

# for key in employee.values():
# 	print(key)

employee_tuple_list = [('name', 'Bob'), ('title', 'Software Engineer')]
employee = dict(employee_tuple_list)
# print(employee)

# dictinary comprehensions
"""
{
	0: 0,
	1: 1,
	2: 4,
	3: 9,
	4: 16,
}
"""
squares = {x : x * x for x in range(500)}
# print(squares)

dictionary0 = {'a': 0, 'b': 1}
dictionary1 = {'c': 2, 'd': 3}

dictionary0.update(dictionary1)

print(dictionary0)