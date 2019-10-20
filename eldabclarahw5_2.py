import os

file_list = ["breast-cancer-wisconsin.data", "diabetes.data", "wdbc.data", "wine.data", "housing.data", "wpbc.data"]

for file_name in file_list:
    os.system("python3 eldabclaraweek5.py "+file_name)
