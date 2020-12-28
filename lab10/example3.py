def recursive_list_(thelist):
	total = 0
	for element in thelist:
		if type(element) == list:
			total = total + recursive_list_(element)
		else:
			total = total + element

	return total
print( recursive_list_([1, 2, [3,4],[5,6]]))