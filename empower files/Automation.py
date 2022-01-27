#Automation
#Specifically used for small subsets with int64 as their astype

import pandas as pd

my_df = pd.read_csv("subset-1-sous-ensemble-1.csv", encoding = "latin-1") #CSV file name (csv file should be saved on the desktop and the name can be changed).
my_df = my_df.loc[my_df['QUESTION'] == 'Q01'] #loc: QUESTION represents column name for which Q01 is the column value the user is concerned with. The code runs it for Q01, Q04, Q08, Q11, Q13, Q14, Q15, Q44.
my_df = my_df.loc[my_df['SURVEYR'] == 2020] #loc: SURVEYR represents column name for which 2020 is the column value the user is concerned with. The code runs for all the years datasets are provided for.
my_df = my_df.iloc[0:,[20, 22]] #iloc: [index:,[column1, column2]] where columns 20 and 22 represent POSITIVE and NEGATIVE respectively.

print (my_df) #Used to print the POSITIVE and NEGATIVE columns (columns 20 and 22).

count = my_df['MOST_POSITIVE_OR_LEAST_NEGATIVE'].count()
print ('Count: ' + str(count)) #Prints the count of values in the column after the application of loc and iloc.

my_df = my_df.astype({"MOST_POSITIVE_OR_LEAST_NEGATIVE": "int64", "MOST_NEGATIVE_OR_LEAST_POSITIVE": "int64"}, copy = False) #Problems arise due dtype issues. This is used for small csv files that have clean datasets with no strings and NaN values.

my_df.sum()["MOST_POSITIVE_OR_LEAST_NEGATIVE"]
my_df.sum()["MOST_NEGATIVE_OR_LEAST_POSITIVE"] #Sums calculated.

average_mpln = my_df.sum()["MOST_POSITIVE_OR_LEAST_NEGATIVE"] / count
average_mnlp = my_df.sum()["MOST_NEGATIVE_OR_LEAST_POSITIVE"] / count #Averages calculated.

print ('Average for MOST_POSITIVE_OR_LEAST_NEGATIVE: ' + str(average_mpln))
print ('Average for MOST_NEGATIVE_OR_LEAST_POSITIVE: ' + str(average_mnlp)) #Print averages.
