numbers = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]

under10 = []
for number in numbers:
	if number < 10:
		under10.append(number)

print(under10)

under10 = [number for number in numbers if number < 10]

print(under10)

variable_name = [expression for variable in iterable opt_bool_exp]

up_to_fifty = [x for x in range(51)]

print(up_to_fifty)

other_numbers = [x for x in numbers if x > 3 and x < 12]

print(other_numbers)

times_three = [i * 3 for i in range(10)]

print(times_three)
