import argparse
import csv
import matplotlib.pyplot as plt
import os.path as op
import plotly.express as px
import numpy as np
import pandas as pd

def convert_type(element):
	if element == "": 
		return None
	try:
		return int(element)
	except ValueError:
		try:
			return float(element)
		except ValueError:
			return element

def parse_file(filename, delimiter):
    assert(op.isfile(filename)), "The File Doesn't Exist"
    with open(filename,'r') as fhandle:
        my_csvreader = csv.reader(fhandle,delimiter=delimiter)
        outer_list_csv = []
        for row in my_csvreader:
            row_list_csv=[]
            for element in row:
                new_element_csv = convert_type(element)
                if new_element_csv is not None:
                    row_list_csv.append(new_element_csv)
            if len(row_list_csv) > 0:
                outer_list_csv += [row_list_csv]
    return outer_list_csv

def line_to_dict(lines, header=False):
    if header:
        column_titles = lines[0]
        lines = lines[1:]
    else:
        column_titles = []
        for idx in list(range(1, len(lines[0])+1)):
            column_titles += ["Column"+str(idx)]
    
    data_dict = {}
    for idx, column in enumerate(column_titles):
        data_dict[column] = []
        for row in lines:
            data_dict[column] += [row[idx]]
    return data_dict

def plot_data(dd,degree):
    for column1 in dd.keys():
        for column2 in dd.keys():
            plt.scatter(dd[column1], dd[column2])
            plt.xlabel(column1)
            plt.ylabel(column2)
            plt.title("{0} x {1}".format(column1, column2))
            x = dd[column1]
            y = dd[column2]
            coefs = np.polyfit(x, y, degree)
            f = np.poly1d(coefs)
            xs = np.linspace (min(x),max(x),100)
            plt.plot(xs,f(xs))
            plt.legend(["Regression Degree: "+str(degree)],loc="lower left")
            plt.show()
            

def plot_pairs(dd):
    df = pd.DataFrame.from_dict(dd)
    fig = px.scatter_matrix(df)
    fig.update_layout(
        title = "Diabetes Dataset",
        width = 1500,
        height = 1500)
    fig.show()

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("filename",type=str,help='Please input file name')
    parser.add_argument("delimiter", type=str,help='Please indicate the delimiter in your file')
    parser.add_argument('-H', '--header', action="store_true", help="determines if a header is present")
    args = parser.parse_args()
    
             
    data = parse_file(args.filename, args.delimiter)
    data_dict = line_to_dict(data, header=args.header)
    plot = plot_data(data_dict,1)
    plot = plot_data(data_dict,2)
    plot = plot_data(data_dict,3)
    plot = plot_data(data_dict,4)
    pairs = plot_pairs(data_dict)
    	
if __name__ == "__main__":
    main()






