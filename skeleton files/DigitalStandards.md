# Getting Started

1. Ensure you have Python3 downloaded. 
2. Ensure you have Python Pandas Library used for statiscal analysis. 
3. Ensure the csv file being used is saved on your desktop for easier access. 

# Development 

The following is used to import pandas and use it to identify the directory of the csv file in question, 

```
import pandas as pd 
df = pd.read_csv (r'file path.csv')
print (df)
```

The following is used to find the average in regards to the questions to be dealt with,

```
mean_n = df['ColumnTitleToBeAveraged'].mean() where n is the first column number 
mean_(n+1) = df['ColumnTitleToBeAveraged'].mean() #where (n+1) is the next column number
...
mean_(x-1) = df['ColumnTitleToBeAveraged'].mean() #where (x-1) is the second last column number
mean_x = df['ColumnTitleToBeAveraged'].mean() #where x is the last column number
```

The following is used to print the averages, 

``` 
print ('Average: ' + str(mean_n))
print ('Average: ' + str(mean_(n+1)))
...
print ('Average: ' + str(mean_(x-1)))
print ('Average: ' + str(mean_x))
```
