# sets
"""
{1, 2, 3, 4, 5, 6}
"""

test_set = {1, 2, 3, 4, 5, 6}
another_test_set = set('aaaaaabbbbbbccccccc')
empty_set = set()

# print (test_set)
# print(another_test_set)
# print(empty_set)

sports = {'football', 'soccer', 'basketball', 'rugby', 'baseball'}

# print('football' in sports)
# print('lacrosse' in sports)

set1 = {0,1,2,3}
set2 = {1,2,3,4,5,6,7,8}

union = set.union(set1, set2)
# print(union)

intersection = set1.intersection(set2)
# print(intersection)

difference = set1.difference(set2)
# print(difference)

isSubset = set1 <= set2
# print(isSubset)

isSuperset = set2 >= set1
# print(isSuperset)

# print(set1 - set2)
# print(set1 | set2)
# print(set1 & set2)
# print(set1 ^ set2)

a = {x for x in 'abracadabra' if x not in 'abc'}
print(a)