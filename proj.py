import pandas as pd

list1 = ['Terfs', 'Swerfs', 'Trump Supporters']
s1 = pd.Series(list1)
print(s1)

list2 = ['one', 'two', 'tree']

series1 = pd.Series(list1, index=list2)
print(series1)
print('                    ')

d1 = {'Z': 'Zynga', 'U': 'Uber', 'G': 'Google'}
ds1 = pd.Series(d1)
print(ds1)

d2 = {'Amazon': 852, 'Nvidia': None, 'Alphabet': 856, 'Toyota': '112', \
    'GE': 29, 'Ford': 12, 'Marriot': None, 'Amazon': 1000}

companies = pd.Series(d2, name='Price')
print(companies)
print(companies[['Amazon', 'GE']])

print(f"is Amazon in the list of companies - - - {'Amazon' in companies}")
print(f"should say 'False' unless your mom is in the company - - - {'Your mom' in companies}")

print(companies.isnull())
