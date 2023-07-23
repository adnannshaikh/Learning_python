# for i in [1,2,3,4,5,]:
# 	for j in ['a','b','c']:
# 		print(i,j)


# iterable-list tuple dictonary set string
# iterated - one by one check each item in the collection

# 

# for _ in range(3):
# 	print(list(range(10)))


for i,char in enumerate(list(range(100))):
	if char == 88:
		print(f"index of 88 is: {i}")
