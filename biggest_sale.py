#!/usr/bin/env python
# coding: utf-8

# In[1]:


import plotly.express as px
import pandas as pd

#reading .csv using panda
real_estate = pd.read_csv("real-estate-sales_main.csv")

#grouping by using groupby() function of panda
Highest_sale = real_estate.groupby(['SaleDate']).agg({'SalePrice':'count'})

# writing to .csv file using to_csv() functions of panda
Highest_sale.to_csv('highest_sale_per_month.csv')

#reading a .csv file  using panda's read_csv () and storing comma-separated values in a variable
data = pd.read_csv('highest_sale_per_month.csv')

# constructing  dataframe out of csv data 
df = pd.DataFrame(data)

new_df = df.rename(columns={'SalePrice': 'BiggestSaleOfTheMonth'})

# Creating lists out of dataframe column for the bar plot 

Months = list(df.iloc[:, 0])
Sales = list(df.iloc[:, 1])

#pltting bar plot using plotly
fig = px.bar(new_df,x = Months, y = Sales, color='BiggestSaleOfTheMonth' )

#showing the plot
fig.show()

    


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




