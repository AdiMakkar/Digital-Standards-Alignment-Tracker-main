# Getting Started

1. Ensure you have Python3 downloaded. 
2. Ensure you have Python Pandas Library used for statiscal analysis. 
3. Ensure the csv file being used is saved on your desktop for easier access. 

# Development 

The following is used to import pandas, libraries, and used to identify the csv file, along with segregating the columns and rows the person is interested in. 

```
import pandas as pd

my_df = pd.read_csv("test.csv", encoding = "latin-1")

my_df = my_df.loc[my_df['ï»¿ year'] == 2019] #ï»¿ year represents the first column and the data can be read for years 2016 - 2019 (with only 2017 onwards considered)

my_df = my_df.loc[my_df['client_feedback_onl'] == 'onl'] #client_feedback_onl represents the 'onl' column and we have tel, eml, person, and post with the naming convention being client_feedback_'name of the desired column'

my_df = my_df.iloc[0:,[36]] #makes sure the specified column prints, 36 - onl, 37 - tel, 38 - eml, 39 - phone, 40 - post

```

The following is used to find the count and can be used to check the count of various service in the service_inventory. 

```
count = my_df['client_feedback_onl'].count()
print ('Count: ' + str(count))
```
