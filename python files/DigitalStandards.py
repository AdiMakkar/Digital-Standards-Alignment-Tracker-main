import pandas as pd

df = pd.read_csv (r'Averages of the Questions Related to Digital Standards 2020.csv')
print (df)

#Averages of Questions
mean1 = df['QUESTION#1MPLN'].mean()
mean2 = df['QUESTION#1MNLP'].mean()
mean3 = df['QUESTION#4MPLN'].mean()
mean4 = df['QUESTION#4MNLP'].mean()
mean5 = df['QUESTION#8MPLN'].mean()
mean6 = df['QUESTION#8MNLP'].mean()
mean7 = df['QUESTION#11MPLN'].mean()
mean8 = df['QUESTION#11MNLP'].mean()
mean9 = df['QUESTION#13MPLN'].mean()
mean10 = df['QUESTION#13MNLP'].mean()
mean11 = df['QUESTION#14MPLN'].mean()
mean12 = df['QUESTION#14MNLP'].mean()
mean13 = df['QUESTION#15MPLN'].mean()
mean14 = df['QUESTION#15MNLP'].mean()
mean15 = df['QUESTION#44MPLN'].mean()
mean16 = df['QUESTION#44MNLP'].mean()

#Printing the Averages of Questions
means = [str(mean1) , str(mean2), str(mean3), str(mean4), str(mean5), str(mean6), str(mean7), str(mean8), str(mean9), str(mean10), str(mean11), str(mean12), str(mean13), str(mean14), str(mean15), str(mean16)]
print(means)