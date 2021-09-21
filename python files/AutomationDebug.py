#AutomationDebug.py
#Specifically used for large subsets
#Used when dtypes differ and can be analyzed by converting the required
#into floats from objects and the operations being performed

import pandas as pd

#CSV file name (csv file should be saved on the desktop and the name can be changed).
my_df = pd.read_csv("Main_9.12.03.b_subset_4.csv", encoding = "latin-1") 

#Used to get rid of NaN values in the documents that usually arise in large csv files and change them to float64.
my_df['POSITIVE'] = pd.to_numeric(my_df['POSITIVE'] , errors = 'coerce')
my_df['NEGATIVE'] = pd.to_numeric(my_df['NEGATIVE'] , errors = 'coerce') 

#loc: QUESTION represents column name for which Q01 is the column value the user is concerned with. The code runs it for Q01, Q04, Q08, Q11, Q13, Q14, Q15, Q44. 
#QUESTION string value could be different and could display empty datasets 
my_df = my_df.loc[my_df['QUESTION'] == 'Q44'] 

#loc: SURVEYR represents column name for which 2020 is the column value the user is concerned with. The code runs for all the years datasets are provided for.
my_df = my_df.loc[my_df['SURVEYR'] == 2019] 

#iloc: [index:,[column1, column2]] where columns 20 and 22 represent POSITIVE and NEGATIVE respectively.
my_df = my_df.iloc[0:,[20, 22]] 

#Used to print the POSITIVE and NEGATIVE columns (columns 20 and 22).
print (my_df) 

#count
count = my_df['POSITIVE'].count()

#Prints the count of values in the column after the application of loc and iloc.
print ('Count: ' + str(count)) 

#Changes the dtype of the count from object to float64.
count = count.astype('float') 

#Calculated Sums.
my_df.sum()["POSITIVE"]
my_df.sum()["NEGATIVE"] 

#Calciulated Averages.
average_mpln = my_df.sum()["POSITIVE"] / count
average_mnlp = my_df.sum()["NEGATIVE"] / count 

#Prints the averages.
print ('Average for POSITIVE: ' + str(average_mpln))
print ('Average for NEGATIVE: ' + str(average_mnlp)) 
