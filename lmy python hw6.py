#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May  8 22:37:13 2023

@author: laura
"""
# !pip install matplotlib
# ! pip install seaborn
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import os


# **Question 1: With the x and y values below, create a plot using only Matplotlib.
# You should plot y1 as a scatter plot and y2 as a line, using different colors
# and a legend.  You can name the data simply "y1" and "y2".  Make sure the
# axis tick labels are legible.  Add a title that reads "HW6 Q1".**



x = pd.date_range(start='1990/1/1', end='1991/12/1', freq='MS')
y1 = np.random.normal(10, 2, len(x))
y2 = [np.sin(v)+10 for v in range(len(x))]


os.getcwd()
os.chdir('/Users/laura/Documents/GitHub/HW6')


fig, ax = plt.subplots()
ax.scatter(x, y1, label = 'y1')
ax.plot(x, y2, label = 'y2', color = 'orange')
ax.set_title('HW6 Q1')
ax.legend()
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
fig.savefig(os.getcwd() + '/q1_plot.png')
plt.show()
# plt.close()


# **# Question 2: Using only Matplotlib, reproduce the figure in this repo named
# question_2_figure.png.**


fig.savefig(os.getcwd() + '/question_2_figure.png')
plt.close()

# cite: https://www.geeksforgeeks.org/matplotlib-axes-axes-set_title-in-python/

# **Question 3: Load the mpg.csv file that is in this repo, and create a
# plot that tests the following hypothesis: a car with an engine that has
# a higher displacement (i.e. is bigger) will get worse gas mileage than
# one that has a smaller displacement.  Test the same hypothesis for mpg
# against horsepower and weight.**


mpg = pd.read_csv('mpg.csv')

mpg.head()

fig, ax = plt.subplots()
ax.scatter(mpg['displacement'], mpg['mpg'])
ax.set_title('HW6 Q3a (mpg vs displacement)')
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.set_xlabel('Displacement')
ax.set_ylabel('Miles per Gallon')
plt.show()
fig.savefig(os.getcwd() + '/q3a_plot.png')
plt.close()


fig, ax = plt.subplots()
ax.scatter(mpg['horsepower'], mpg['mpg'])
ax.set_title('HW6 Q3b (mpg vs horsepower)')
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.set_xlabel('Horsepower')
ax.set_ylabel('Miles per Gallon')
plt.show()
fig.savefig(os.getcwd() + '/q3b_plot.png')
plt.close()


fig, ax = plt.subplots()
ax.scatter(mpg['weight'], mpg['mpg'])
ax.set_title('HW6 Q3c (mpg vs weight)')
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.set_xlabel('Weight')
ax.set_ylabel('Miles per Gallon')
plt.show()
fig.savefig(os.getcwd() + '/q3c_plot.png')
plt.close()

# cite: https://www.geeksforgeeks.org/matplotlib-axes-axes-set_xlabel-in-python/

# **Question 4: Continuing with the data from question 3, create a scatter plot 
# with mpg on the y-axis and cylinders on the x-axis.  Explain what is wrong 
# with this plot with a 1-2 line comment.  Now create a box plot using Seaborn
# that uses cylinders as the groupings on the x-axis, and mpg as the values
# up the y-axis.**
# 


fig, ax = plt.subplots()
ax.scatter(mpg['cylinders'], mpg['mpg'])
ax.set_title('HW6 Q4a scatter plot(mpg vs cylinders)')
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.set_xlabel('Cylinders')
ax.set_ylabel('Miles per Gallon')
plt.show()
fig.savefig(os.getcwd() + '/q4a_plot.png')
plt.close()
# The column cylinders stores discrete integers instead of continuous values, and scatter plots are 
# often used to measure continuous data. There are also many overlaps which can be hard to distinguish.
# It's also hard to characterize each number of cylinders seperately as it provides little information
# only by looking at the scatter plot. 



fig, ax = plt.subplots()
ax = sns.boxplot(x = 'cylinders', y = 'mpg', data = mpg)
ax.set_title('HW6 Q4b box plot(mpg vs cylinders)')
ax.set_xlabel('Cylinders')
ax.set_ylabel('Miles per Gallon')
plt.show()
fig.savefig(os.getcwd() + '/q4b_plot.png')
plt.close()


# **Question 5: Continuing with the data from question 3, create a two-by-two 
# grid of subplots, where each one has mpg on the y-axis and one of 
# displacement, horsepower, weight, and acceleration on the x-axis.  To clean 
# up this plot:**
# - Remove the y-axis tick labels (the values) on the right two subplots - 
# the scale of the ticks will already be aligned because the mpg values 
# are the same in all axis.  
# - Add a title to the figure (not the subplots) that reads "Changes in MPG"
# - Add a y-label to the figure (not the subplots) that says "mpg"
# - Add an x-label to each subplot for the x values
# 
# **Finally, use the savefig method to save this figure to your repo.  If any
# labels or values overlap other chart elements, go back and adjust spacing.**



fig, ax = plt.subplots(2, 2, figsize = (10, 10))
(ax1, ax2), (ax3, ax4) = ax
fig.suptitle('Changes in MPG')

ax1.scatter(mpg['displacement'], mpg['mpg'], s = 10)
ax1.set_xlabel('Displacement')
ax1.set_ylabel('MPG')


ax2.scatter(mpg['horsepower'], mpg['mpg'], s = 10)
ax2.set_yticks([])
ax2.set_xlabel('Horsepower')
ax2.set_ylabel('MPG')


ax3.scatter(mpg['weight'], mpg['mpg'], s = 10)
ax3.set_xlabel('Weight')
ax3.set_ylabel('MPG')


ax4 = sns.boxplot(x = 'cylinders', y = 'mpg', data = mpg)
ax4.set_yticks([])
ax4.set_xlabel('Cylinders')
ax4.set_ylabel('MPG')



plt.subplots_adjust(hspace=0.5, wspace=0.3)
plt.show()
fig.savefig(os.getcwd() + '/q5_plot.png')
plt.close()

# cite: https://www.geeksforgeeks.org/how-to-create-different-subplot-sizes-in-matplotlib/
# cite: https://www.geeksforgeeks.org/matplotlib-axes-axes-set_yticks-in-python/

# **Question 6: Are cars from the USA, Japan, or Europe the least fuel
# efficient, on average?  Answer this with a plot and a one-line comment.**
# 



by_country = mpg.groupby('origin')['mpg'].mean()
by_country = pd.DataFrame(by_country).reset_index()

fig, ax = plt.subplots()
ax.bar(by_country['origin'], by_country['mpg'], width = 0.5)
ax.set_title('HW6 Q6 Average MPG by Region')
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.set_xlabel('Cylinders')
ax.set_ylabel('Miles per Gallon')
ax.text(0.3, -0.2, 'Note: On average, cars from Japan have highest MPG while cars from USA have the least.',
        transform=ax.transAxes, ha='center')
for i, v in enumerate(by_country['mpg']):
    ax.text(i - 0.12, v + 0.2, str(round(v, 2)), fontsize=10) # source: add value to each bar

plt.show()
fig.savefig(os.getcwd() + '/q6_plot.png')
plt.close()

# On average, cars from Japan have highest MPG while cars from USA have the least.

# cite: https://stackoverflow.com/questions/30228069/how-to-display-the-value-on-horizontal-bars


# **Question 7: Using Seaborn, create a scatter plot of mpg versus displacement,
# while showing dots as different colors depending on the country of origin.
# Explain in a one-line comment what this plot says about the results of 
# question 6.**


fig, ax = plt.subplots()
sns.set()
ax = sns.scatterplot(x = 'displacement', y = 'mpg', hue = 'origin', data = mpg)
ax.set_title('HW6 Q7 scatter plot(mpg vs displacement by origin)')
ax.set_xlabel('Displacement')
ax.set_ylabel('Miles per Gallon')
plt.show()
fig.savefig(os.getcwd() + '/q7_plot.png')
plt.close()







