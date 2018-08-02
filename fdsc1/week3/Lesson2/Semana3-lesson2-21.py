import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# The following code reads all the Gapminder data into Pandas DataFrames. You'll
# learn about DataFrames next lesson.

path = '/home/maru/Documents/Udacity/Udacity-DataScienceI/Semana3/'
employment = pd.read_csv(path + 'employment-above-15.csv', index_col='Country')
female_completion = pd.read_csv(path + 'female-completion-rate.csv', index_col='Country')
male_completion = pd.read_csv(path + 'male-completion-rate.csv', index_col='Country')
life_expectancy = pd.read_csv(path + 'life-expectancy.csv', index_col='Country')
gdp = pd.read_csv(path + 'gdp-per-capita.csv', index_col='Country')

# The following code creates a Pandas Series for each variable for the United States.
# You can change the string 'United States' to a country of your choice.

employment_us = employment.loc['United States']
female_completion_us = female_completion.loc['United States']
male_completion_us = male_completion.loc['United States']
life_expectancy_us = life_expectancy.loc['United States']
gdp_us = gdp.loc['United States']
gdp_br = gdp.loc['Brazil']
gdp_ge = gdp.loc['Germany']
# gdp_ca = gdp.loc['Canada']

# Uncomment the following line of code to see the available country names
print employment.index.values

# Use the Series defined above to create a plot of each variable over time for
# the country of your choice. You will only be able to display one plot at a time
# with each "Test Run".

# employment_us.plot()
# female_completion_us.plot()
# male_completion_us.plot()
# life_expectancy_us.plot()
# gdp_us.plot()
plt.plot(gdp_us, 'bo')
plt.plot(gdp_br, 'g^')
plt.plot(gdp_ge, 'bs')
plt.show()
