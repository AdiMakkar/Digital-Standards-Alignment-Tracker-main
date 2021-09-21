#AutomationDebug.py
#Example of Year 2019: Subsets 2, 3, 4
#Applied to csv files with dtypes as objects and 
#further used by converting the required to floats and performing operations

import pandas as pd

my_df = pd.read_csv("Main_9.12.03.b_subset_4.csv", encoding = "latin-1")

my_df['POSITIVE'] = pd.to_numeric(my_df['POSITIVE'] , errors = 'coerce')
my_df['NEGATIVE'] = pd.to_numeric(my_df['NEGATIVE'] , errors = 'coerce')

my_df = my_df.loc[my_df['QUESTION'] == 'Q44']
my_df = my_df.loc[my_df['SURVEYR'] == 2019]
my_df = my_df.iloc[0:,[20, 22]]

print (my_df)

count = my_df['POSITIVE'].count()
print ('Count: ' + str(count))
count = count.astype('float')

my_df.sum()["POSITIVE"]
my_df.sum()["NEGATIVE"]

average_mpln = my_df.sum()["POSITIVE"] / count
average_mnlp = my_df.sum()["NEGATIVE"] / count

print ('Average for POSITIVE: ' + str(average_mpln))
print ('Average for NEGATIVE: ' + str(average_mnlp))
