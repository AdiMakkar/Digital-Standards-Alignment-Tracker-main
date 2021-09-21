#Automation
#Specifically used for small subsets with int64 as their astype

import pandas as pd

my_df = pd.read_csv("subset-1-sous-ensemble-1.csv", encoding = "latin-1")
my_df = my_df.loc[my_df['QUESTION'] == 'Q01']
my_df = my_df.loc[my_df['SURVEYR'] == 2020]
my_df = my_df.iloc[0:,[20, 22]]

print (my_df)

count = my_df['MOST_POSITIVE_OR_LEAST_NEGATIVE'].count()
print ('Count: ' + str(count))

my_df = my_df.astype({"MOST_POSITIVE_OR_LEAST_NEGATIVE": "int64", "MOST_NEGATIVE_OR_LEAST_POSITIVE": "int64"}, copy = False)

my_df.sum()["MOST_POSITIVE_OR_LEAST_NEGATIVE"]
my_df.sum()["MOST_NEGATIVE_OR_LEAST_POSITIVE"]

average_mpln = my_df.sum()["MOST_POSITIVE_OR_LEAST_NEGATIVE"] / count
average_mnlp = my_df.sum()["MOST_NEGATIVE_OR_LEAST_POSITIVE"] / count

print ('Average for MOST_POSITIVE_OR_LEAST_NEGATIVE: ' + str(average_mpln))
print ('Average for MOST_NEGATIVE_OR_LEAST_POSITIVE: ' + str(average_mnlp))
