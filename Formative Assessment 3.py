#!/usr/bin/env python
# coding: utf-8

# In[46]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('fifa_data.csv')


#  ### Which Country Has the Most Number of Players?

# In[47]:


A = df['Nationality'].value_counts()
A1 = A.idxmax()
print(f"The country with the most number of players: {A1}")


# ### Plot a Bar Chart of 5 Top Countries with the Most Number of Players

# In[48]:


B = A.head(5)
sns.barplot(x=B.index, y=B.values, palette= ('#084594', '#2171b5', '#4292c6', '#6baed6', '#9ecae1'))
plt.title('Top 5 Countries with the Most Number of Players')
plt.xlabel('Country')
plt.ylabel('Players')
plt.show()


# ### Which Player Has the Highest Salary?

# In[49]:


C = df.loc[df['Wage'].idxmax()]
C1 = C['Name']
print(f'The player with the highest salary: {C1}')


# ### Plot a Histogram to Get the Salary Range of the Players

# In[50]:


sns.histplot(df['Wage'].str.replace('€', '').str.replace('K', '000').astype(int), kde=True)
plt.title('Player Salary')
plt.xlabel('Wage(Euros)')
plt.ylabel('Number of Players')
plt.show()


# In[ ]:





# ### Who Is the Tallest Player in FIFA?

# In[51]:


def D(height):
    try:
        feet, inches = height.split("'")
        feet = int(feet)
        inches = int(inches)
        return float(f"{feet}.{inches}")
    except:
        return None

df['D1'] = df['Height'].apply(D)

df = df[df['D1'].notna()]

D2 = df.loc[df['D1'].idxmax()]
D3 = D2['Name']
print(f'The tallest player in FIFA: {D3}')

D4 = D2['D1']
print(f'Height of the tallest player: {D4} feet')



# ### Which Club Has the Most Number of Players?

# In[52]:


E = df['Club'].value_counts()
E1 = E.idxmax()
print(f'The club with the most number of players: {E1}')


# ### Which Foot Is Most Preferred by the Players?

# In[53]:


F = df['Preferred Foot'].value_counts()

sns.barplot(x=F.index, y=F.values, palette='cool')
plt.title('Players Preferred Foot')
plt.xlabel('Preferred Foot')
plt.ylabel('Number of Players')
plt.show()


# ### INSIGHTS GATHERED

# In[54]:


#Insight 1: 
# We identified the country with the most number of players, also shows talents in different nationalities.

#Insight 2: 
#shows that certain countries are good at producing FIFA players, also can see regional strengths in football talent.

#Insight 3: 
#Identify the player with the highest salary shows the market value of top players in FIFA.

#Insight 4: 
#The histogram of player wages shows the distribution of salaries, indicating the seeyable differences among players.

#Insight 5: 
#with the knoweldge of tallest player we can see the physical differnces within FIFA players.

#Insight 6: 
#knowing club with most no of players we can see the most sort out club for the players and also can know the team composition.

#Insight 7: 
#this visualization shows the distribution of left footed and right footed players, and we can decide how to influence gameplay and strategize for the game.


# In[ ]:




