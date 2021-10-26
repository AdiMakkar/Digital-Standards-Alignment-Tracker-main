#Service_Inventory code to automate the process of counting the value to be found 

import pandas as pd

#CSV file name (csv file should be saved on the desktop and the name can be changed)
my_df = pd.read_csv("test.csv", encoding = "latin-1")

#The columns and rows looking to consider in my_df. 
my_df = my_df.loc[my_df['ï»¿ year'] == 2019] #ï»¿ year represents the first column and the data can be read for years 2016 - 2019 (with only 2017 onwards considered)
my_df = my_df.loc[my_df['client_feedback_onl'] == 'onl'] #client_feedback_onl represents the 'onl' column and we have tel, eml, person, and post with the naming convention being client_feedback_'name of the desired column'
my_df = my_df.iloc[0:,[36]] #makes sure the specified column prints, 36 - onl, 37 - tel, 38 - eml, 39 - phone, 40 - post

#prints the rows and columns preferred
print (my_df)

#count
count = my_df['client_feedback_onl'].count()
print ('Count: ' + str(count))

#The following comments were used to veryify the issues which may or may not occur when dealing with csv files
#Due to enormous amount of changes and preferable dtypes, accessing csv files can be a hassle and can be fixed by accessing and massaging the dtypes of columns. 

#my_df.astype('object').dtypes
#print(my_df.dtypes)
