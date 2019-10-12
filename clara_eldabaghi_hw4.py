def convert_type(element):
	# Case 2: is an emptry str, should be ignored
	if element == "": # len(element) == 0
		return None
	# Case 4: is a # with no ., should be int
	try:
		return int(element)
	except ValueError:
		# Case 3: has a . but is a #, should be float
		try:
			return float(element)
		except ValueError:
			# Case 1: is a string, should remain a string
			return element

def split_custom(row):
	split_row = row.split(',')
	#if you split the row successfully (i.e it generated more than 1 element), then return the split row
	if len(split_row)>1:
		return split_row
	else:
		#if the split didn't occur at the comma, then split at blank space
		return row.split()
	
def header_fn(list_of_lists):
	need_header = True
	for row in list_of_lists[1:]:
		if type(list_of_lists[0][0])==type(row[0]):
			continue
		else:
			need_header = False
			break
	header=[]		
	if need_header == True:
		for counter,value in enumerate(row):
			header += ["Column " + str(counter+1)]
		return header
	else:
		return outer_list[0]
	

filename = '/Users/c_eldab/Desktop/python/diabetes.data'

data = open(filename, 'r')

my_read_data = data.read()
#print(my_read_data)

my_read_data1 = my_read_data.split('\n')

outer_list = []
for row in my_read_data1:
	row_list = []
	for element in split_custom(row):
		if element is not None:
			new_element = convert_type(element)
		else:
			continue
		if new_element is not None:
			row_list.append(new_element)
			# row_list += [new_element]   # equiv. to the above
		print(element, end="\t")
		print(new_element, type(new_element))
	print(row_list)

	if len(row_list) > 0:
		outer_list += [row_list]
		# outer_list.append(row_list)  # equiv. to the above


header = header_fn(outer_list)
outer_list.insert(0,header)

# Dictionary of lists-time:
our_dictionary = {}
# We know: our first row (i.e. outer_list[0]) contains
# our column headings. We want these headings to be our
# dictionary keys.

for location, column_headings in enumerate(outer_list[0]):
	#print(column_headings)
	our_dictionary[column_headings] = list()  # equiv. to []
	for row in outer_list[1:]:
		our_dictionary[column_headings] += [row[location]]
	# Add data values to the corresponding columns

#print(our_dictionary)

print(header)

