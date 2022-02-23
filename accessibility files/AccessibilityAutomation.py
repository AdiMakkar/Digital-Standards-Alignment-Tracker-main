#AccessibilityAutomation

import pandas as pd

my_df = pd.read_csv("accessibility_2021.csv", encoding = "latin-1") #CSV file name (csv file should be saved on the desktop and the name can be changed).

count = my_df['Mobile_Accessibility'].count()
print ('Count: ' + str(count)) #Prints the count of values in the column after the application of loc and iloc.

my_df = my_df.astype({"Mobile_Accessibility": "int64", "Desktop_Accessibility": "int64"}, copy = False) #Problems arise due dtype issues. This is used for small csv files that have clean datasets with no strings and NaN values.

my_df.sum()["Mobile_Accessibility"]
my_df.sum()["Desktop_Accessibility"] #Sums calculated.

average_mpln = my_df.sum()["Mobile_Accessibility"] / count
average_mnlp = my_df.sum()["Desktop_Accessibility"] / count #Averages calculated.

print ('Average for Mobile_Accessibility: ' + str(average_mpln))
print ('Average for Desktop_Accessibility: ' + str(average_mnlp)) #Print averages.