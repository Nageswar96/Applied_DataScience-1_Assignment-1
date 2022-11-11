#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as nmp # linear algebra
import pandas as pnds # data processing, CSV file I/O (e.g. pd.read_csv)
import matplotlib.pyplot as mtplt
import warnings

warnings.filterwarnings("ignore")


# In[99]:


#reading the dataset with the pandas 
dataOfVictims = pnds.read_csv("https://www.ethnicity-facts-figures.service.gov.uk/crime-justice-and-the-law/crime-and-reoffending/victims-of-crime/latest/downloads/victims-of-crime-data.csv", encoding= 'unicode_escape')


# In[100]:


dataOfVictims.tail(10)


# In[101]:


#checking for the null values 
dataOfVictims.isnull().sum()


# In[102]:


dataOfVictims['Time'].unique()


# In[103]:


dataOfVictims.info()


# In[104]:


#converting the data types in string
dataOfVictims = dataOfVictims.convert_dtypes()
dataOfVictims.info()


# In[129]:


#replacing the commas with the blank value
dataOfVictims = dataOfVictims.replace(',','', regex=True)
#replacing the "Male " which have a extra space with the "male"
dataOfVictims = dataOfVictims.replace('Male ','Male', regex=True)
#replacing the ? with the value 0 because all are the numerical values
dataOfVictims = dataOfVictims.replace(['?'], '0')
dataOfVictims.head(30)


# In[107]:


#converting  the value, sample size, lower CI and Upper CI values in the float because all are the numerical values
dataOfVictims['Value'] = dataOfVictims['Value'].astype('float')
dataOfVictims['Sample size'] = dataOfVictims['Sample size'].astype('float')
dataOfVictims['Upper CI'] = dataOfVictims['Upper CI'].astype('float')
dataOfVictims['Lower CI'] = dataOfVictims['Lower CI'].astype('float')

dataOfVictims.dtypes


# In[108]:


pnds.to_numeric(dataOfVictims['Value'])


# In[109]:


dataOfVictims = dataOfVictims.astype({"Value" : float})


# In[113]:


dataOfVictims['Geography'].unique()


# In[151]:


'''the function is used for plotting the line plot for the given dataset in which it specifies the figure size that is x axis has 20 and y has 10,
then use group by on the attribute on the Geography attribute with the mean of CI values on the data. Then in the function defined a title to the plot
 and give the label on the x axis and y axis and in the end give the legend by the use of library'''
def GeographyVsCIValues():
    mtplt.figure(figsize=(20,10))
    dataOfVictims.groupby(['Geography'])['Upper CI'].mean().plot( marker = 'o')
    dataOfVictims.groupby(['Geography'])['Lower CI'].mean().plot( marker = 'o')
    mtplt.xticks(rotation=90)
    mtplt.ylabel("CI Values")
    mtplt.xlabel("Geography Location")
    mtplt.title("Geography location having their Minumum and Maximum CI values")
    mtplt.legend(["Upper CI", "Lower CI"], title="CI values")
GeographyVsCIValues()


# In[60]:


dataOfVictims['Ethnicity_type'].unique()


# In[147]:


'''The function EthinicityCount is defined to draw a histogram for the attribute Ethnicity which  count the number of observations of Ethnicity.
In the same function, defnied the figure size and title to the figure, label for x axis and y axis and in the end defined the legend for the graph '''
def EthinicityCount():
    mtplt.figure(figsize=(20,10))
    dataOfVictims['Ethnicity_type'].hist()
    mtplt.ylabel("Count")
    mtplt.xlabel("Ethnicity Type")
    mtplt.title("Number of records in each  ethnicity type")
    mtplt.legend(["Ethnicity"], title="Type of ethnicity")
EthinicityCount()


# In[77]:


dataOfVictims['Geography code'].unique()


# In[153]:


'''The function Scatterr is used to draw a scatter plot with the help of matplotlib library. In the plot the scattering on the basis of the gender,
if the gender is all then it will scatter in orange color if gender is male then blue  and if gender is female then color is Red.
In the function there is size, title lable on x and y axis is given and in the last defined the legend for the graph according to the Gender values'''
def Scatterr():
    mtplt.figure(figsize=(20,10))
    mtplt.scatter('Upper CI', 'Lower CI', data=dataOfVictims[dataOfVictims.Gender=="All"], c = 'orange')
    mtplt.scatter('Upper CI', 'Lower CI', data=dataOfVictims[dataOfVictims.Gender=="Male"], c = 'blue')
    mtplt.scatter('Upper CI', 'Lower CI', data=dataOfVictims[dataOfVictims.Gender=="Female"], c = 'Red')
    mtplt.legend(('All', 'Male','Female'), title='Gender')
    mtplt.ylabel("Upper CI")
    mtplt.xlabel("Lower CI")
    mtplt.title("Lower and Upper CI values scatter with Gender details")
    mtplt.legend(['All','Male','Female'], title="Gender")
Scatterr()


# In[ ]:




