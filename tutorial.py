"""
r - reading only
	
rb - reading only in binary format

r+ - both reading and writing

rb+ - both reading and writing in binary format
	
w - writing only

wb - writing only in binary format

w+ - both writing and reading

wb+ - both writing and reading in binary format

a - appending

ab - appending in binary format

a+ - both appending and reading

ab+ - both appending and reading in binary format
"""
import os
import json

# test_file = open("test_file.txt", "a+")

# test_file.write("test3")

# test_file.close()

# with open("test_file.txt", "a+") as test_file:
# 	test_file.write("\ntest4")

# os.rename("another_test.txt", "test2.txt")

# os.remove("test2.txt")

test_data = {
	"abc": "test data"
}

# print(json.dumps(test_data))

# with open("test_file.json", "w") as f:
	# json.dump(test_data, f)

# with open("test_file.json") as f:
# 	json_data = json.load(f)

# print(json_data)