#This section defines the functions to be used:

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
    if need_header == True:
        header=[]
        row=list_of_lists[0]
        for counter,value in enumerate(row):
            header += ["Column " + str(counter+1)]
        return header
    else:
        return None
	
#This section imports the libraries

import argparse
import csv
import matplotlib.pyplot as plt

#This section allows us to input the file name as an argument and exits with an error message if the file does not exist

parser = argparse.ArgumentParser()
parser.add_argument("filename",type=str,help='Please input file name and location')
arguments = parser.parse_args()
filename = arguments.filename

try:
    data_csv = open(filename, 'r')
except:
    print("File doesn't exist. Please type valid file name")
    exit()

#Here we parse with the cvs library

my_csvreader = csv.reader(data_csv,delimiter=',')
    #if len(first_line_csv)==1:
#   my_csvreader = csv.reader(data_csv,delimiter=' ')
outer_list_csv = []
for row in my_csvreader:
    row_list_csv=[]
    for element in row:
        new_element_csv = convert_type(element)
        if new_element_csv is not None:
            row_list_csv.append(new_element_csv)
    if len(row_list_csv) > 1:
        outer_list_csv += [row_list_csv]

if len(outer_list_csv)==0:
    data_csv_1 = open(filename, 'r')
    my_csvreader = csv.reader(data_csv_1,delimiter=' ')
    for row in my_csvreader:
        row_list_csv=[]
        for element in row:
            new_element_csv = convert_type(element)
            if new_element_csv is not None:
                row_list_csv.append(new_element_csv)
        if len(row_list_csv) > 0:
            outer_list_csv += [row_list_csv]

header_csv = header_fn(outer_list_csv)
if header_csv is not None:
    outer_list_csv.insert(0,header_csv)

our_dictionary_csv = {}

for location, column_headings in enumerate(outer_list_csv[0]):
    our_dictionary_csv[column_headings] = list()
    for row in outer_list_csv[1:]:
        our_dictionary_csv[column_headings] += [row[location]]

#Here we parse as we did in prior homework

data = open(filename, 'r')
my_read_data = data.read()
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
	if len(row_list) > 0:
		outer_list += [row_list]

header = header_fn(outer_list)
if header is not None:
    outer_list.insert(0,header)

our_dictionary = {}

for location, column_headings in enumerate(outer_list[0]):
	our_dictionary[column_headings] = list()
	for row in outer_list[1:]:
		our_dictionary[column_headings] += [row[location]]

#Here, we test to see if the two parsing methods have the same results:

print(len(outer_list))
print(len(outer_list_csv))
print(outer_list[0])
print(outer_list_csv[0])
print(outer_list[1])
print(outer_list_csv[1])
print(outer_list[len(outer_list)-1])
print(outer_list_csv[len(outer_list_csv)-1])
assert (len(outer_list_csv) == len(outer_list)), "The lists of lists don't have the same length"
for counter_1,row_csv in enumerate(outer_list_csv):
    assert (len(outer_list[counter_1]) == len(outer_list_csv[counter_1])), "The rows in the lists of lists don't have the same lengths"
    assert (outer_list[counter_1][0] == outer_list_csv[counter_1][0]), "The first element in outer_list_csv is not equal to the corresponding element in outer_list"

#Here, we plot each column of dataset

for key,attribute in our_dictionary_csv.items():
    if type(our_dictionary_csv[key][0]) is float or type(our_dictionary_csv[key][0]) is int:
        plt.plot(attribute)
        plt.ylabel(key)
        plt.show()
    else:
        x=[]
        for c,i in enumerate(attribute):
            x.append(c)
        plt.scatter(x,attribute)
        plt.ylabel(key)
        plt.show()


