# Getting Started

1. Ensure you have Python3 downloaded. 
2. Ensure you have Python Pandas Library used for statiscal analysis. 
3. Ensure the csv file being used is saved on your desktop for easier access. 

# Development 

The following is used to import pandas and use it to identify the csv file, put in the parameters to look for specific tabs and choose the columns to be averaged in the question, 
```
import pandas as pd

my_df = pd.read_csv("file_name.csv', encoding = "latin-1")

my_df = my_df.loc[my_df['column_name#1'] == 'column_value_to_be_chosen#1'] where column_name#1 and column_value_to_be_chosen#1 mean Column of the parameter and parameter chosen respectively. 

my_df = my_df.loc[my_df['column_name#2'] == 'column_value_to_be_chosen#2'] where column_name#2 and column_value_to_be_chosen#2 mean Column of the parameter and parameter chosen respectively.

my_df = my_df.iloc[0:,[column#1, column#2]] where column#1 and column#2 mean the columns that need to be averaged
```

The following is used to find the count of the number of values being averaged for one specific question of one specific subset of one specific year,

```
count = my_df['column#1 or column#2].count()
print ('Count: ' + str(count))
```

The following is used to changed the type of the result, 

```
my_df = my_df.astype({"column#1": "int64", "column#2": "int64"}, copy = False)
```

The following is used to sum the columns, 

```
my_df.sum()["column#1"]
my_df.sum()["column#2"]
```

The following is used to average the columns on the basis of the count of rows, 

```
average_column#1 = my_df.sum()["column#1"] / count
average_column#2 = my_df.sum()["column#2"] / count
```

The following is used to print the averaged values of a specific question for a specific subset of a specific year, 

```
print ('Average for column#1: ' + str(average_column#1))
print ('Average for column#2: ' + str(average_column#2))
```
