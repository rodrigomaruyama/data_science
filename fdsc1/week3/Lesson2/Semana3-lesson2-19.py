import pandas as pd

s1 = pd.Series([1, 2, 3, 4], index=['a', 'b', 'c', 'd'])
s2 = pd.Series([10, 20, 30, 40], index=['c', 'd', 'e', 'f'])

# Try to write code that will add the 2 previous series together,
# but treating missing values from either series as 0. The result
# when printed out should be similar to the following line:
# print pd.Series([1, 2, 13, 24, 30, 40], index=['a', 'b', 'c', 'd', 'e', 'f'])

# minha versao. :( Enorme!!!
new_index = []
new_values = []
for i in s1.index:
    if not i in new_index:
        new_index.append(i)
for j in s2.index:
    if not j in new_index:
        new_index.append(j)

for i in new_index:
    if i in s1.index and i in s2.index:
        new_values.append(s1.loc[i]+s2.loc[i])
    elif i in s1.index and not i in s2.index:
        new_values.append(s1.loc[i])
    elif not i in s1.index and i in s2.index:
        new_values.append(s2.loc[i])

new_series = pd.Series(new_values, index = new_index)

print new_series

# versao da professora
print s1.add(s2, fill_value=0)
