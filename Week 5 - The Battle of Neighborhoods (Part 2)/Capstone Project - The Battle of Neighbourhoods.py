#!/usr/bin/env python
# coding: utf-8

# <h1><center><u>Capstone Project - The Battle of Neighbourhoods</u></center></h1>
# <h2><center>London's Crime Rate Analysis and Clustering of the Safest Neighbourhoods of London</center></h2>

# Vincent Stanislaus Pereira<br>
# August 2021

# # <u>Table of Contents</u>:
# * [Introduction](#Intro)
# * [Business Problem](#Problem)
# * [Objective of the Capstone Project](#Objective)
# * [Interested Parties](#Target)
# * [Description of Data](#Data)
# * [Methodology](#Method)
#  * [A) Importing Libraries](#A)
#  * [B) Extracting, Scraping, Exploring, Cleaning and Processing the Datasets](#B)
#    - [1) Dataset 1: Metropolitan Police Service Ward Level Crime Data for London](#Dataset1)
#    - [2) Dataset 2: List of London Boroughs](#Dataset2)
#    - [3) Dataset 3: Merged Dataset of Dataset 1 and Dataset 2](#Dataset3)
#    - [4) Dataset 4: London Postcodes](#Dataset4)
#  * [C) Understanding the Dataset Using Groupby Function and Charts](#C)
#    - [1) Group the Dataframe by "Borough"](#1)
#    - [2) Group the Dataframe by "Ward"](#2)
#    - [3) Group the Dataframe by "Crime Head"](#3)
#    - [4) Group the Dataframe by "Crime Sub-Head"](#4)
#    - [5) Group the Dataframe by "Borough" and "Ward"](#5)
#    - [6) Group the Dataframe by "Borough" and "Crime Head"](#6)
#    - [7) Group the Dataframe by "Borough", "Crime Head" and "Crime Sub-Head"](#7)
#    - [8) Group the Dataframe by "Borough", "Ward", "Crime Head" and "Crime Sub-Head"](#8)
#    - [9) Group the Dataframe by "Ward" and "Crime Sub-Head"](#9)
#    - [10) Top 10 Most Safest and Worst 10 Most Dangerous Boroughs of London](#10)
#    - [11) Month on Month Crime Rate for the 10 Safest & 10 Dangerous Boroughs of London](#11)
#    - [12) Top 5 Crimes in Each of the 5 Most Safest Boroughs of London](#12)
#      - [a) Top 5 Crimes in the No. 1 Safest Borough of London](#a)
#      - [b) Top 5 Crimes in the No. 2 Safest Borough of London](#b)
#      - [c) Top 5 Crimes in the No. 3 Safest Borough of London](#c)
#      - [d) Top 5 Crimes in the No. 4 Safest Borough of London](#d)
#      - [e) Top 5 Crimes in the No. 5 Safest Borough of London](#e)
#    - [13) Top 5 Crimes in the 5 Most Safest Boroughs of London Grouped By "Boroughs"](#13)
#    - [14) Top 10 Crimes in the 5 Most Safest Boroughs of London Grouped By "Crime Head"](#14)
#    - [15) Month on Month Crime Rate for the Top 5 Crimes in the 5 Most Safest Boroughs](#15)
#    - [16) Top 50 Most Safest Wards in the 5 Most Safest Boroughs of London](#16)
#  * [D) Collecting the Coordinates and Plotting them on the Map of London](#D)
#    - [(i) Creating a Crime Dataframe of the Top 5 Boroughs](#Crime_Dataframe)
#    - [(ii) Merging Crime Dataframe of the Top 5 Boroughs with Top 50 Most Safest Wards](#Merging_Dataframes)
#    - [iii) Extracting the Postcodes of the Top 50 Safest Wards of London](#Postcodes)
#    - [(iv) Selecting Locations Nearest to a Station](#Nearest_Station)
#    - [(v) Fetching Coordinates by Using the Arcgis API](#ArcGIS_API)
#    - [(vi) Plotting Stations on the Map of London](#Plot_Stations)
#  * [E) Identifying Venues around the Safe Neighbourhoods of London](#E)
#    - [(i) Defining Foursquare API Credentials](#Credentials)
#    - [(ii) Creating a Function to Get All the Venue Categories in London](#Function)
#    - [(iii) Gathering Information of Venues in the Safe Neighbourhoods of London](#Venue_Information)
#    - [(iv) Analysing the Dataset](#Analyse)
#  * [F) Segmenting Neighbourhoods of London By Common Venue Categories](#F)
#    - [(i) One Hot Encoding](#OHE)
#    - [(ii) Printing Each Neighbourhood Along with the Top 8 Most Common Venues](#Print)
#    - [(iii) Transferring the Venues into a Pandas Dataframe](#Pandas_Dataframe)
#  * [G) Clustering Neighbourhoods By Common Venues (K-Means Clustering)](#G)
#    - [(i) Building a Model to Cluster the Neighbourhoods](#Model)
#    - [(ii) Principal Component Analysis (PCA)](#PCA)
#    - [(iii) Visualising the Resulting Clusters on the Map of London](#Map)
#    - [(iv) Examining the Clusters](#Examine)
# * [Results and Discusion](#Result)
# * [Conclusion](#Conclusion)

# # <u>Introduction</u>:<a name="Intro"></a>

# London is one of the most multicultural cities in the world. It is a melting pot of cultures, where one can taste the best of the world cuisine. It is a major centre for banking and finance, insurance, world trade, media, advertising, tourism, theatre, fashion, arts and more. Fusing gritty, historic pomp with shimmering modernity, world-class culture and fashion-forward shopping, the UK’s capital has it all and there’s something for everyone. The vibrancy of the city extends across all 32 of its boroughs, all of which are home to a plethora of unique neighbourhoods.

# # <u>Business Problem</u>:<a name="Problem"></a>

# The decision to move to a new a city or a new country altogether, is a harrowing one. But after having decided to move to London, the next challenge one faces is to decide where to live in London. If one looks at the map of London, they will find a haphazard cluster of neighbourhoods and villages, each with their own distinct features and identity. Some of London’s best neighbourhoods are usually established on the typical tourist trail, while others are constantly evolving, taking turns to emerge as the new cool hotspot. The following questions then arise in our mind,
# - Which neighbourhood is right for us?
# - Which part of the city has the best parks and playgrounds?
# - Which schools fall in the neighbourhood?
# - What area has the best craft beer scene or all-night eateries?
# - Where can one find the hippest bookstores or outdoor yoga?
# 
# And at the top of all these doubts, the most intriguing questions anyone would face are,
# - What is the crime rate in the area?
# - Is it a secure neighbourhood?
# - Is it safe to venture out in the night?
# 
# All these questions and more plague our mind and then the quest to find the answers begins.

# # <u>Objective of the Capstone Project</u>:<a name="Objective"></a>

# The objective of this assignment is to give an insight into what some of the safest London neighbourhoods can offer its residents and tourists.
# 
# To help uncover the best that London has to offer, this project aims to do the following,
# - Identify the safest boroughs and wards in London based on the latest crime data
# - Find the Latitude & the Longitude coordinates of the preferred neighbourhoods by using their Postcodes
# - Plot the safest neighbourhoods on the Map of London using the geographical coordinates obtained 
# - Locate the most common venues in the vicinity of 500 metres from these neighbourhoods
# - Cluster these neighbourhoods based on the common venues using a Machine Learning algorithm (K-Means Clustering)

# # <u>Interested Parties</u>:<a name="Target"></a>

# The objective of this project is to identify and recommend the best & safest neighbourhoods in London to anyone who wants to visit or relocate to London. The interested parties could be anyone from the below mentioned list,
# - Young couples
# - Families with children
# - Executives
# - Tourists, etc.

# # <u>Description of Data</u>:<a name="Data"></a>

# ## 1) Metropolitan Police Service Ward Level Crime Data for London
# - This dataset has been extracted from the Metropolitan Police Service’s “Recorded Crime: Geographic Breakdown” Data available on the London Datastore: https://data.london.gov.uk/dataset/recorded_crime_summary
# - This data provides the number of crimes recorded per month according to crime type at the geographic level of London’s Wards for the period July 2019 to June 2021

# ## 2) List of London Boroughs
# - This dataset has been extracted from the Wikipedia.org page: https://en.wikipedia.org/wiki/List_of_London_boroughs
# - It has been used to fetch more information on the different Boroughs of London, like the local authority of the borough, the political party controlling the local authority, the Head Quarters of the local authority, the area of the Borough, its population, its coordinates and its designated number on the map of London
# - With this information we can get more insight in to the various Boroughs of London

# ## 3) London Postcodes
# - This dataset has been extracted from Doogal.co.uk: https://www.doogal.co.uk/london_postcodes.php
# - The dataset has a complete list of London postcode districts
# - Even though this dataset already had the Latitude and the Longitude data available, I have used the ArcGIS API to re-fetch the coordinates of the preferred locations 

# ## 4) ArcGIS API Data
# - ArcGIS is an online API that enables us to connect people, locations, and data using interactive maps: https://developers.arcgis.com/python/
# - We use the ArcGIS API to get the geographical coordinates (Latitude and Longitude) of the neighbourhoods of London by providing the Postcodes of the desired locations
# - The following information is obtained for each Postcode,
#  - Latitude: Latitude of the Postcode
#  - Longitude: Longitude of the Postcode

# ## 5) Foursquare API Data
# - Foursquare is a location data provider with information about different venues and events within an area of interest: https://foursquare.com
# - The information obtained from the Foursquare API includes venue names, locations, menus, reviews, photos, etc.
# - The Foursquare location platform is, thus, used by us as a data source since all the required information about the different venues in various neighbourhoods of the desired Borough or Ward can be obtained through their API

# # <u>Methodology</u>:<a name="Method"></a>

# **<u>Note</u>: You may click on any of the links below to directly go to the code for the related topic.**
# 
# <a href="#A"><dd>A) Importing Libraries</dd></a>
# - Libraries used in this Project are,
#  - **Pandas:** For creating and manipulating dataframes
#  - **Numpy:** For scientific computation
#  - **JSON:** To handle JSON files
#  - **Requests:** To handle http requests
#  - **Matplotlib:** It is a data visualisation and graphical plotting library
#  - **Plotly:** It is also a visualisation library for creating interactive and publication-quality charts / graphs
#  - **Folium:** It is used for visualising geospatial data and plotting interactive maps
#  - **Geocoder:** To retrieve Location Data
#  - **Scikit Learn:** To use K-Means Clustering, a Machine Learning Algorithm
# 
# <a href="#B"><dd>B) Extracting, Scraping, Exploring, Cleaning and Processing the Datasets</dd></a>
# - After importing all the required libraries, we will extract the data from different sources and clean it so that it is ready for processing and analysing
# 
# <a href="#C"><dd>C) Understanding the Dataset Using Groupby Function and Charts</dd></a>
# - We will then use the Groupby Function and Charts to understand the data better
#  - During this process, the dataset will be used to find Boroughs that have the highest and the lowest crime rate
#  - After having found the boroughs with the lowest crime rate, the data will be sorted, and the 5 safest Boroughs in London will be identified
#  - Though the 5 Boroughs identified can easily serve our purpose, as these 5 Boroughs are the safest ones as compared to the other Boroughs of London; we will further try to eliminate the areas with crime so as to find the most secure venues for our target audience
#  - If we take all the 92 Wards from the shortlisted 5 safe Boroughs, there may still be a possibility that some of the Venues could fall in the "unsafe" Ward of that particular safe Borough
#  - Therefore, in order to avoid such a scenario and to ensure that the Venues found are from the most secure areas of London, another layer of safety will be added to identify the 10 Most Safest Wards within each of the 5 Most Safest Boroughs
#  - Thus, out of a total of 615 Wards in the whole of London, we will shortlist only the 50 Most Safest Wards
# 
# <a href="#D"><dd>D) Collecting the Coordinates and Plotting them on the Map of London</dd></a>
# - Once we are done with the identifying the safest Boroughs and Wards of London, we will extract the Postcodes of the different neighbourhoods in London
#  - It should be noted that even though the dataset already has the Latitude and the Longitude data available as a part of the originally downloaded dataset, we will still be using the ArcGIS API to re-fetch the coordinates of the preferred locations
#  - The dataset will then be processed to identify the postcodes of the Top 50 safest Wards of London
#  - After cleaning the data, we find that there are still 10,083 records of the Postcodes for the Top 50 safest Wards of London
#  - Now, we could have used these 10,083 Postcodes of the Top 50 Wards of London to find their coordinates, but the process of fetching the coordinates for so many postcodes would have taken a lot of time
#  - Hence, it is necessary to reduce the number of records further
#  - In order to further reduce the number of locations, the neighbourhoods having distance nearest to a station in these safe Wards will be selected
#  - This process will not only reduce the number of locations, but it will also greatly assist the target audience, as finding venues that are nearer to the stations will reduce their travel time and will also be more convenient to them
#  - Since the number of stations that fall in these safe Wards are 81, after processing this requirement, the number of Postcodes reduce to 81 from 10,083
#  - Further, since we have selected only those Venues that are nearest to the Station, we will rename the column "Nearest Station" to "Neighbourhood" as all these neighbourhoods are very close to the respective Stations
#  - This dataset of Postcodes will then be used to fetch the geographical coordinates, i.e., the Latitude and Longitude, of the different neighbourhoods within the Top 50 safest Wards of London
#  - As discussed earlier, we will use the ArcGIS API to collect the Latitude and Longitude coordinates of the neighbourhoods based on their postcodes
#  - These coordinates will then be used to plot these locations on the Map of London
# 
# <a href="#E"><dd>E) Identifying Venues around the Safe Neighbourhoods of London</dd></a>
# - The Latitude and Longitude coordinates will be linked with the Foursquare API to identify the different venues near these neighbourhoods
# - In order to get the required information, we will provide the Foursquare API with the Latitude and Longitude coordinates of the preferred neighbourhood
# - Based on the Latitude and Longitude coordinates, the Foursquare API will acquire information about different venues within each neighbourhood
# - The data retrieved from the Foursquare API contains information of venues, which are within the radius of 500 metres of the latitude and longitude of said postcode
# - The following information is obtained for each venue,
#  - **Neighbourhood:** Name of the Neighbourhood
#  - **Neighbourhood Latitude:** Latitude of the Neighbourhood
#  - **Neighbourhood Longitude:** Longitude of the Neighbourhood
#  - **Venue:** Name of the Venue
#  - **Venue Category:** Category of the Venue
#  - **Venue Latitude:** Latitude of the Venue
#  - **Venue Longitude:** Longitude of the Venue
# - In order to understand this information better, we will analyse the data using Groupby
# 
# <a href="#F"><dd>F) Segmenting Neighbourhoods of London By Common Venue Categories</dd></a>
# - Here, we will use One Hot Encoding on the column Venue Category
# - This will convert all the values in the column Venue Category to those many different columns
# - We will then print each Neighbourhood along with the Top 8 Most Common Venues in that Neighbourhood
# - After this, we will create a dataframe having the columns Neighbourhood and the Top 8 Most Common Venues in those Neighbourhoods
# 
# <a href="#G"><dd>G) Clustering Neighbourhoods By Common Venues (K-Means Clustering)</dd></a>
# - In order to assist our Target Audience to find venues of their choice in the safest neighbourhoods of London, we will be clustering the neighbourhoods using the K-Means Clustering Algorithm
# - The K-Means Clustering Algorithm will cluster neighbourhoods with similar venues into different clusters
# - We will first use the Elbow Method to identify the Optimal Number of Clusters
# - As per this method, the optimal number of clusters is achieved when the change in slope of the line becomes small
# - After we have identified the optimal number of clusters, we will run the Machine Learning Algorithm to get the Cluster Labels
# - Applying Dimensionality Reduction Techniques helps in visualising how the Clusters are related in the original high dimensional space
# - Hence, in order to see how the Clusters are related in the original space, we will use Principal Component Analysis (PCA) to visualise the high dimensional data
# - PCA also helps in finding if the features of the data are linearly related to each other
# - The clustered neighbourhoods will then plotted on the Map of London
# - Based on the information collected, we will present our observations and findings, which will assist us in taking the necessary decisions

# # A) Importing Libraries:<a name="A"></a>

# In[1]:


import pandas as pd
import numpy as np

import json
from pandas.io.json import json_normalize
import requests

get_ipython().run_line_magic('matplotlib', 'inline')
import matplotlib as mpl
import matplotlib.pyplot as plt
import matplotlib.cm as cm
import matplotlib.colors as colors

import plotly.express as px
import plotly.graph_objects as go

import folium

import geocoder
from geopy.geocoders import Nominatim

from sklearn.cluster import KMeans
from sklearn.decomposition import PCA
from sklearnex import patch_sklearn
patch_sklearn()


# # B) Extracting, Scraping, Exploring, Cleaning and Processing the Datasets:<a name="B"></a>

# #### Here, we extract the datasets from different sources. If the source is a downloadable file, we use the Pandas library to extract the data. And if the source is a website, we scrape the data using JSON and Requests library. Sometimes, we may also use Beautiful Soup, another Python Library, to scrape the data from a website.
# 
# #### Next, we clean the data, if required, and then process the same so that the data can be analysed

# ## 1) Dataset 1: Metropolitan Police Service Ward Level Crime Data for London<a name="Dataset1"></a>

# ### Extracting the MPS Ward Level Crime Dataset for the Period July 2019 to June 2021 from the Metropolitan Police Service’s “Recorded Crime: Geographic Breakdown” Data available on the London Datastore

# In[2]:


crime_df = pd.read_csv("MPS Ward Level Crime (most recent 24 months).csv")
crime_df.head()


# In[3]:


crime_df.info()


# ### Renaming the Columns

# In[4]:


columns = ["Crime Head", "Crime Sub-Head", "Ward", "Ward Code", "Borough", 201907, 201908, 201909, 201910, 201911, 201912, 202001, 202002, 202003, 202004, 202005, 202006, 202007, 202008, 202009, 202010, 202011, 202012, 202101, 202102, 202103, 202104, 202105, 202106]


# In[5]:


crime_df.columns = columns


# In[6]:


crime_df.head()


# ### Re-indexing the Columns / Changing the Position of the Columns

# In[7]:


crime_df = crime_df.reindex(["Ward Code", "Ward", "Borough", "Crime Head", "Crime Sub-Head", 201907, 201908, 201909, 201910, 201911, 201912, 202001, 202002, 202003, 202004, 202005, 202006, 202007, 202008, 202009, 202010, 202011, 202012, 202101, 202102, 202103, 202104, 202105, 202106], axis = 1)


# In[8]:


crime_df.head()


# ### Inserting a "Total" Column in the Dataframe 

# In[9]:


crime_df["Total"] = crime_df.sum(numeric_only = True, axis = 1)


# In[10]:


crime_df.head()


# ### During the Exploration, I found that there are 2 Wards by the name of "Belmont" in Harrow and Sutton. We need to Segregate them so that the analysis gives better results.

# In[11]:


crime_df[crime_df["Ward"] == "Belmont"]


# ### Changing Ward to "Belmont Harrow", where the Ward is "Belmont" and Borough is "Harrow"

# In[12]:


crime_df.loc[((crime_df["Ward"] == "Belmont") & (crime_df["Borough"] == "Harrow")), "Ward"] = "Belmont Harrow"
crime_df[crime_df["Ward"] == "Belmont Harrow"]


# ### Changing Ward to "Belmont Sutton", where the Ward is "Belmont" and Borough is "Sutton"

# In[13]:


crime_df.loc[((crime_df["Ward"] == "Belmont") & (crime_df["Borough"] == "Sutton")), "Ward"] = "Belmont Sutton"
crime_df[crime_df["Ward"] == "Belmont Sutton"]


# In[14]:


crime_df.head()


# In[15]:


crime_df.info()


# ### Statistics

# In[16]:


crime_df.nunique()


# In[17]:


mask = (crime_df["Borough"] == "Kingston upon Thames") | (crime_df["Borough"] == "Richmond upon Thames") | (crime_df["Borough"] == "Sutton") | (crime_df["Borough"] == "Merton") | (crime_df["Borough"] == "Harrow")


# In[18]:


crime_df[mask].nunique()


# In[19]:


crime_df.describe()


# ## 2) Dataset 2: List of London Boroughs<a name="Dataset2"></a>

# ### Scraping the Data on List of London Boroughs from the Wikipedia Page

# In[20]:


london_bor_list_url = "https://en.wikipedia.org/wiki/List_of_London_boroughs"
london_bor_list = pd.read_html(london_bor_list_url)


# In[21]:


type(london_bor_list)


# In[22]:


london_bor_df = london_bor_list[0]
london_bor_df


# In[23]:


london_bor_df.columns=["Borough", "Inner", "Status", "Local Authority", "Political Control", "Head Quarters", "Area (sq mi)", "Population (2013 estimate)",
"Co-ordinates", "Borough No. on Map"]
london_bor_df


# In[24]:


london_bor_df = london_bor_df.replace("note 1", "", regex=True) 
london_bor_df = london_bor_df.replace("note 2", "", regex=True) 
london_bor_df = london_bor_df.replace("note 3", "", regex=True) 
london_bor_df = london_bor_df.replace("note 4", "", regex=True) 
london_bor_df = london_bor_df.replace("note 5", "", regex=True)


# In[25]:


london_bor_df


# In[26]:


london_bor_df["Borough"].replace({
                                    "Barking and Dagenham[]" : "Barking and Dagenham",
                                    "Greenwich []" : "Greenwich",
                                    "Hammersmith and Fulham[]" : "Hammersmith and Fulham",
                                }, inplace = True)
london_bor_df["Borough"]


# In[27]:


london_bor_df = london_bor_df.drop(["Inner", "Status"], axis = 1)
london_bor_df


# In[28]:


london_bor_df.info()


# ## 3) Dataset 3: Merged Dataset of Dataset 1 and Dataset 2<a name="Dataset3"></a>

# ### Merging the MPS Ward Level Crime Dataset and List of London Broughs Dataset into a Single Dataset

# In[29]:


london_crime_df = pd.merge(crime_df, london_bor_df , on = 'Borough')
london_crime_df


# ### Re-indexing the Columns / Changing the Position of the Columns

# In[30]:


london_crime_df = london_crime_df.reindex(["Ward Code", "Ward", "Borough", "Local Authority", "Political Control", "Head Quarters", "Area (sq mi)", "Population (2013 estimate)", "Co-ordinates", "Borough No. on Map", "Crime Head", "Crime Sub-Head", 201907, 201908, 201909, 201910, 201911, 201912, 202001, 202002, 202003, 202004, 202005, 202006, 202007, 202008, 202009, 202010, 202011, 202012, 202101, 202102, 202103, 202104, 202105, 202106, "Total"], axis = 1)
london_crime_df


# In[31]:


london_crime_df.info()


# ## 4) Dataset 4: London Postcodes<a name="Dataset4"></a>

# ### Extracting the London Postcodes Dataset from Doogal.co.uk

# In[32]:


london_postcodes_df = pd.read_csv("London Postcodes.csv", low_memory = False)
london_postcodes_df.head()


# In[33]:


london_postcodes_df.info()


# ### Cleaning the Data

# In[34]:


london_postcodes_df = london_postcodes_df.drop(["County", "Country", "County Code", "Introduced", "Terminated", "Parish", "National Park", "Population", "Households", "Built up area", "Built up sub-division", "Rural/urban", "Region", "Altitude", "Local authority", "Parish Code", "Census output area", "Index of Multiple Deprivation", "Quality", "User Type", "Last updated", "Police force", "Water company", "Plus Code", "Average Income", "Sewage Company", "Travel To Work Area"], axis = 1)
london_postcodes_df.head()


# In[35]:


london_postcodes_df.info()


# ### Keeping only those Postcodes that are "In Use"

# In[36]:


london_postcodes_df = london_postcodes_df[london_postcodes_df["In Use?"] == "Yes"]
london_postcodes_df.info()


# In[37]:


london_postcodes_df = london_postcodes_df.drop(["In Use?"], axis = 1)
london_postcodes_df.info()


# ### Renaming the Columns

# In[38]:


postcode_cols = ["Postcode Data", "Latitude Data", "Longitude Data", "Easting", "Northing", "Grid Ref", "Borough", "Ward", "Borough Code", "Ward Code", "Constituency", "Lower Layer Super Output Area", "London Zone", "LSOA Code", "MSOA Code", "Middle Layer Super Output Area", "Constituency Code", "Nearest Station", "Distance To Station", "Postcode Area", "Postcode District"]
london_postcodes_df.columns = postcode_cols
london_postcodes_df.info()


# ### Re-indexing the Columns / Changing the Position of the Columns

# In[39]:


postcode_cols_new = ["Postcode Data", "Latitude Data", "Longitude Data", "Nearest Station", "Distance To Station", "Ward Code", "Ward", "Borough Code", "Borough", "Constituency Code", "Constituency", "LSOA Code", "Lower Layer Super Output Area", "MSOA Code", "Middle Layer Super Output Area", "London Zone", "Postcode Area", "Postcode District", "Easting", "Northing", "Grid Ref"]
london_postcodes_df = london_postcodes_df.reindex(postcode_cols_new, axis = 1)
london_postcodes_df.info()


# ### While the Exploring the "crime_df" Dataset, it was found that there were 2 Wards by the name of "Belmont" in Harrow and Sutton. Hence, in order to Segregate them, their names were changed to "Belmont Harrow" and "Belmont Sutton". To maintain consistency, we will change the names of these 2 Wards in the "london_postcodes_df" Dataset as well.

# In[40]:


london_postcodes_df[london_postcodes_df["Ward"] == "Belmont"]


# #### There are a total of 402 rows with Ward as "Belmont"

# In[41]:


london_postcodes_df[(london_postcodes_df["Ward"] == "Belmont") & (london_postcodes_df["Borough"] == "Harrow")]


# #### Out of the total 402 rows with Ward as "Belmont", 208 rows have Ward as "Belmont" and Borough as "Harrow"

# In[42]:


london_postcodes_df[(london_postcodes_df["Ward"] == "Belmont") & (london_postcodes_df["Borough"] == "Sutton")]


# #### Out of the total 402 rows with Ward as "Belmont", 194 rows have Ward as "Belmont" and Borough as "Sutton"

# ### Changing Ward to "Belmont Harrow", where the Ward is "Belmont" and Borough is "Harrow"

# In[43]:


london_postcodes_df.loc[((london_postcodes_df["Ward"] == "Belmont") & (london_postcodes_df["Borough"] == "Harrow")), "Ward"] = "Belmont Harrow"
london_postcodes_df[london_postcodes_df["Ward"] == "Belmont Harrow"]


# ### Changing Ward to "Belmont Sutton", where the Ward is "Belmont" and Borough is "Sutton"

# In[44]:


london_postcodes_df.loc[((london_postcodes_df["Ward"] == "Belmont") & (london_postcodes_df["Borough"] == "Sutton")), "Ward"] = "Belmont Sutton"
london_postcodes_df[london_postcodes_df["Ward"] == "Belmont Sutton"]


# In[45]:


london_postcodes_df.head()


# In[46]:


london_postcodes_df.info()


# In[47]:


london_postcodes_df.nunique()


# # C) Understanding the Dataset Using Groupby Function and Charts:<a name="C"></a>

# Here, the we explore the dataset by using the Groupby Function. We also visualise the data by plotting Charts. This helps us to understand the data and get a better insight into the dataset.

# ## 1) Group the Dataframe by "Borough"<a name="1"></a>

# In[48]:


bor_crime_df = crime_df.groupby("Borough").sum()
bor_crime_df.sort_values(by = ["Total", "Borough"], inplace = True)
bor_crime_df


# ### a) Plotting the Bar Chart of the Total Crimes Recorded During the Period July 2019 to June 2021

# In[49]:


bar_chart = px.bar(
                        bor_crime_df,
                        title = "Total Crimes Recorded in London Boroughs During the Period July 2019 to June 2021",
                        color = "Total",
                        color_continuous_scale=[(0, "cyan"), (0.25, "yellow"), (0.5, "red"), (0.75, "red"), (1, "maroon")],
                        width = 1000,
                        height = 700
                  )

bar_chart.show()


# ### b) Plotting the Horizontal Bar Chart of the Total Crimes Recorded During the Period July 2019 to June 2021

# In[50]:


h_bar_chart = px.bar(
                        bor_crime_df,
                        title = "Total Crimes Recorded in London Boroughs During the Period July 2019 to June 2021",
                        color = "Total",
                        orientation = "h",
                        color_continuous_scale=[(0, "cyan"), (0.25, "yellow"), (0.5, "red"), (0.75, "red"), (1, "maroon")],
                        width = 1000,
                        height = 750
                    )

h_bar_chart.show()


# ## 2) Group the Dataframe by "Ward"<a name="2"></a>

# In[51]:


crime_df.groupby("Ward").sum()


# ### a) Total Crimes Recorded in the Top 20 Most Safest London Wards During the Period July 2019 to June 2021

# In[52]:


top_ward_crime_df = crime_df.groupby("Ward").sum()
top_ward_crime_df.sort_values(by = ["Total", "Ward"], ascending = True, inplace = True)
top_ward_crime_df = top_ward_crime_df.head(20)
top_ward_crime_df


# #### Plotting the Horizontal Bar Chart for the Total Crimes Recorded in the Top 20 Most Safest London Wards During the Period July 2019 to June 2021

# In[53]:


h_bar_chart = px.bar(
                        top_ward_crime_df,
                        title = "Total Crimes Recorded in the Top 20 Most Safest London Wards During the Period July 2019 to June 2021",
                        color = "Total",
                        orientation = "h",
                        color_continuous_scale=[(0, "cyan"), (0.25, "lightgreen"), (0.5, "yellow"), (0.75, "orange"), (1, "red")]
                    )

h_bar_chart.show()


# ### b) Total Crimes Recorded in Worst 20 Most Dangerous London Wards During the Period July 2019 to June 2021

# In[54]:


worst_ward_crime_df = crime_df.groupby("Ward").sum()
worst_ward_crime_df.sort_values(by = ["Total", "Ward"], ascending = True, inplace = True)
worst_ward_crime_df = worst_ward_crime_df.tail(20)
worst_ward_crime_df


# #### Plotting the Horizontal Bar Chart for the Total Crimes Recorded in Worst 20 Most Dangerous London Wards During the Period July 2019 to June 2021

# In[55]:


h_bar_chart = px.bar(
                        worst_ward_crime_df,
                        title = "Total Crimes Recorded in Worst 20 Most Dangerous London Wards During the Period July 2019 to June 2021",
                        color = "Total",
                        orientation = "h",
                        color_continuous_scale=[(0, "red"), (0.25, "darkred"), (0.5, "maroon"), (0.75, "maroon"), (1, "indigo")]
                    )

h_bar_chart.show()


# ## 3) Group the Dataframe by "Crime Head"<a name="3"></a>

# ### Types of Crimes Recorded in London During the Period July 2019 to June 2021

# In[56]:


type_crimes_crime_df = crime_df.groupby(["Crime Head"]).sum()
type_crimes_crime_df.sort_values(by = ["Total", "Crime Head"], ascending = True, inplace = True)
type_crimes_crime_df


# #### Plotting the Horizontal Bar Chart for the Types of Crimes Recorded in London During the Period July 2019 to June 2021

# In[57]:


type_crimes_crime_bar = px.bar(
                        type_crimes_crime_df,
                        title = "Types of Crimes Recorded in London During the Period July 2019 to June 2021",
                        color = "Total",
                        orientation = "h",
                        color_continuous_scale=[(0, "cyan"), (0.25, "yellow"), (0.5, "orange"), (0.75, "red"), (1, "maroon")]
                    )

type_crimes_crime_bar.show()


# ## 4) Group the Dataframe by "Crime Sub-Head"<a name="4"></a>

# ### Top 20 Crimes Recorded in London During the Period July 2019 to June 2021

# In[58]:


type_sub_crimes_crime_df = crime_df.groupby(["Crime Sub-Head"]).sum()
type_sub_crimes_crime_df.sort_values(by = ["Total", "Crime Sub-Head"], ascending = False, inplace = True)
type_sub_crimes_crime_df = type_sub_crimes_crime_df.head(20)
type_sub_crimes_crime_df.sort_values(by = ["Total", "Crime Sub-Head"], ascending = True, inplace = True)
type_sub_crimes_crime_df


# #### Plotting the Horizontal Bar Chart for the Top 20 Crimes Recorded in London During the Period July 2019 to June 2021

# In[59]:


type_sub_crimes_crime_bar = px.bar(
                        type_sub_crimes_crime_df,
                        title = "Top 20 Crimes Recorded in London During the Period July 2019 to June 2021",
                        color = "Total",
                        orientation = "h",
                        color_continuous_scale=[(0, "cyan"), (0.25, "orange"), (0.5, "red"), (0.75, "maroon"), (1, "purple")]
                    )

type_sub_crimes_crime_bar.show()


# ## 5) Group the Dataframe by "Borough" and "Ward"<a name="5"></a>

# In[60]:


crime_df.groupby(["Borough", "Ward"]).sum()


# ## 6) Group the Dataframe by "Borough" and "Crime Head"<a name="6"></a>

# In[61]:


crime_df.groupby(["Borough", "Crime Head"]).sum()


# ## 7) Group the Dataframe by "Borough", "Crime Head" and "Crime Sub-Head"<a name="7"></a>

# In[62]:


crime_df.groupby(["Borough", "Crime Head", "Crime Sub-Head"]).sum()


# ## 8) Group the Dataframe by "Borough", "Ward", "Crime Head" and "Crime Sub-Head"<a name="8"></a>

# In[63]:


crime_df.groupby(["Borough", "Ward", "Crime Head", "Crime Sub-Head"]).sum()


# ## 9) Group the Dataframe by "Ward" and "Crime Sub-Head"<a name="9"></a>

# In[64]:


crime_df.groupby(["Ward", "Crime Sub-Head"]).sum()


# ## 10) Top 10 Most Safest and Worst 10 Most Dangerous Boroughs of London<a name="10"></a>

# ### a) Plotting the Bar Chart for the Top 10 Most Safest Boroughs of London

# In[65]:


T10S_bor_crime_df = bor_crime_df.head(10)
T10S_bor_crime_df


# In[66]:


T10S_bor_bar = px.bar(
                        T10S_bor_crime_df,
                        title = "Top 10 Most Safest Boroughs of London",
                        color = "Total",
                        color_continuous_scale=[(0, "cyan"), (0.25, "lightgreen"), (0.5, "yellow"), (0.75, "orange"), (1, "red")]
                     )
T10S_bor_bar.show()


# ### b) Plotting the Bar Chart for the Worst 10 Most Dangerous Boroughs of London

# In[67]:


W10D_bor_crime_df = bor_crime_df.sort_values(by = "Total", ascending = False).head(10)
W10D_bor_crime_df


# In[68]:


W10D_bor_bar = px.bar(
                        W10D_bor_crime_df,
                        title = "Worst 10 Most Dangerous Boroughs of London",
                        color = "Total",
                        color_continuous_scale=[(0, "yellow"), (0.25, "red"), (0.5, "red"), (0.75, "maroon"), (1, "maroon")]
                        #color_continuous_scale=[(0, "orange"), (0.5, "magenta"), (1, "red")]
                     )
W10D_bor_bar.show()


# ## 11) Month on Month Crime Rate for the 10 Safest & 10 Dangerous Boroughs of London<a name="11"></a>

# ### a) Plotting the Line Chart for the Month on Month Crime Rate for the Top 10 Most Safest Boroughs of London

# In[69]:


T10S_mom_bor_crime_df = bor_crime_df.drop(["Total"], axis = 1).head(10)
T10S_mom_bor_crime_df


# In[70]:


T10S_bor_line = T10S_mom_bor_crime_df.transpose()
T10S_bor_line


# #### X-Axis for the Line Chart

# In[71]:


T10S_years = [str(year) for year in list(T10S_bor_line.index.values)]
T10S_years


# #### Y-Axis for the Line Chart

# In[72]:


T10S_boroughs = [str(year) for year in list(T10S_bor_line.columns.values)]
T10S_boroughs


# In[73]:


T10S_bor_line[T10S_boroughs[0]]


# #### "name" Parameter for the Line Chart

# In[74]:


T10S_boroughs[0]


# #### Line Chart for the Month on Month Crime Rate for the Top 10 Most Safest Boroughs of London

# In[75]:


line = go.Figure()

line.add_trace(go.Scatter(x = T10S_years, y = T10S_bor_line[T10S_boroughs[0]], name = T10S_boroughs[0], mode = "lines + markers", line=dict(color='black', width=2)))
line.add_trace(go.Scatter(x = T10S_years, y = T10S_bor_line[T10S_boroughs[1]], name = T10S_boroughs[1], mode = "lines + markers", line=dict(color='royalblue', width=2)))
line.add_trace(go.Scatter(x = T10S_years, y = T10S_bor_line[T10S_boroughs[2]], name = T10S_boroughs[2], mode = "lines + markers", line=dict(color='yellow', width=2)))
line.add_trace(go.Scatter(x = T10S_years, y = T10S_bor_line[T10S_boroughs[3]], name = T10S_boroughs[3], mode = "lines + markers", line=dict(color='green', width=2)))
line.add_trace(go.Scatter(x = T10S_years, y = T10S_bor_line[T10S_boroughs[4]], name = T10S_boroughs[4], mode = "lines + markers", line=dict(color='magenta', width=2)))
line.add_trace(go.Scatter(x = T10S_years, y = T10S_bor_line[T10S_boroughs[5]], name = T10S_boroughs[5], mode = "lines + markers", line=dict(color='cyan', width=2)))
line.add_trace(go.Scatter(x = T10S_years, y = T10S_bor_line[T10S_boroughs[6]], name = T10S_boroughs[6], mode = "lines + markers", line=dict(color='firebrick', width=2)))
line.add_trace(go.Scatter(x = T10S_years, y = T10S_bor_line[T10S_boroughs[7]], name = T10S_boroughs[7], mode = "lines + markers", line=dict(color='orange', width=2)))
line.add_trace(go.Scatter(x = T10S_years, y = T10S_bor_line[T10S_boroughs[8]], name = T10S_boroughs[8], mode = "lines + markers", line=dict(color='red', width=2)))
line.add_trace(go.Scatter(x = T10S_years, y = T10S_bor_line[T10S_boroughs[9]], name = T10S_boroughs[9], mode = "lines + markers", line=dict(color='skyblue', width=2)))

line.update_layout(title = "Month on Month Crime Rate for the Top 10 Most Safest Boroughs of London", xaxis_title = "Month & Year", yaxis_title = "Total No. of Crimes")

line.show()


# ### b) Plotting the Line Chart for the Month on Month Crime Rate for the Worst 10 Most Dangerous Boroughs of London

# In[76]:


W10D_mom_bor_crime_df = bor_crime_df.sort_values(by = "Total", ascending = False).drop(["Total"], axis = 1).head(10)
W10D_mom_bor_crime_df


# In[77]:


W10D_bor_line = W10D_mom_bor_crime_df.transpose()
W10D_bor_line


# #### X-Axis for the Line Chart

# In[78]:


W10D_years = [str(year) for year in list(W10D_bor_line.index.values)]
W10D_years


# #### Y-Axis for the Line Chart

# In[79]:


W10D_boroughs = [str(year) for year in list(W10D_bor_line.columns.values)]
W10D_boroughs


# In[80]:


W10D_bor_line[W10D_boroughs[0]].head()


# #### "name" Parameter for the Line Chart

# In[81]:


W10D_boroughs[0]


# #### Line Chart for the Month on Month Crime Rate for the Worst 10 Most Dangerous Boroughs of London

# In[82]:


line = go.Figure()

line.add_trace(go.Scatter(x = W10D_years, y = W10D_bor_line[W10D_boroughs[0]], name = W10D_boroughs[0], mode = "lines + markers", line=dict(color='black', width=2)))
line.add_trace(go.Scatter(x = W10D_years, y = W10D_bor_line[W10D_boroughs[1]], name = W10D_boroughs[1], mode = "lines + markers", line=dict(color='royalblue', width=2)))
line.add_trace(go.Scatter(x = W10D_years, y = W10D_bor_line[W10D_boroughs[2]], name = W10D_boroughs[2], mode = "lines + markers", line=dict(color='yellow', width=2)))
line.add_trace(go.Scatter(x = W10D_years, y = W10D_bor_line[W10D_boroughs[3]], name = W10D_boroughs[3], mode = "lines + markers", line=dict(color='green', width=2)))
line.add_trace(go.Scatter(x = W10D_years, y = W10D_bor_line[W10D_boroughs[4]], name = W10D_boroughs[4], mode = "lines + markers", line=dict(color='magenta', width=2)))
line.add_trace(go.Scatter(x = W10D_years, y = W10D_bor_line[W10D_boroughs[5]], name = W10D_boroughs[5], mode = "lines + markers", line=dict(color='cyan', width=2)))
line.add_trace(go.Scatter(x = W10D_years, y = W10D_bor_line[W10D_boroughs[6]], name = W10D_boroughs[6], mode = "lines + markers", line=dict(color='firebrick', width=2)))
line.add_trace(go.Scatter(x = W10D_years, y = W10D_bor_line[W10D_boroughs[7]], name = W10D_boroughs[7], mode = "lines + markers", line=dict(color='orange', width=2)))
line.add_trace(go.Scatter(x = W10D_years, y = W10D_bor_line[W10D_boroughs[8]], name = W10D_boroughs[8], mode = "lines + markers", line=dict(color='red', width=2)))
line.add_trace(go.Scatter(x = W10D_years, y = W10D_bor_line[W10D_boroughs[9]], name = W10D_boroughs[9], mode = "lines + markers", line=dict(color='skyblue', width=2)))

line.update_layout(title = "Month on Month Crime Rate for the Worst 10 Most Dangerous Boroughs of London", xaxis_title = "Month & Year", yaxis_title = "Total No. of Crimes")

line.show()


# ## 12) Top 5 Crimes in Each of the 5 Most Safest Boroughs of London<a name="12"></a>

# ### Group the Dataframe by "Borough" and "Crime Head" and then Sort the Values on "Borough", "Total" and "Crime Head" Columns

# In[83]:


bor_ch_crime_df = crime_df.groupby(["Borough", "Crime Head"]).sum()
bor_ch_crime_df.sort_values(by = ["Borough", "Total", "Crime Head"], inplace = True)
bor_ch_crime_df


# In[84]:


bor_ch_crime_df.reset_index(inplace = True)
bor_ch_crime_df


# ### a) Top 5 Crimes in the No. 1 Safest Borough of London<a name="a"></a>

# In[85]:


print('The No. 1 Safest Borough of London is "' + T10S_boroughs[0] + '"')


# In[86]:


N01SB_T05C_df = bor_ch_crime_df[bor_ch_crime_df["Borough"] == T10S_boroughs[0]].sort_values(by = "Total", ascending = False).head()
N01SB_T05C_df


# In[87]:


N01SB_T05C_df_new = N01SB_T05C_df[["Borough", "Crime Head", "Total"]]
N01SB_T05C_df_new.set_index("Borough", inplace = True)
N01SB_T05C_df_new


# #### Bar Chart for the Top 5 Crimes in the No. 1 Safest Borough of London

# In[88]:


N01SB_T05C_bar = px.bar(
                            N01SB_T05C_df_new,
                            title = "Top 5 Crimes in the No. 1 Safest Borough of London",
                            color = "Crime Head",
                            barmode = "group",
                            width = 900,
                            height = 600
                       )

N01SB_T05C_bar.show()


# ### b) Top 5 Crimes in the No. 2 Safest Borough of London<a name="b"></a>

# In[89]:


print('The No. 2 Safest Borough of London is "' + T10S_boroughs[1] + '"')


# In[90]:


N02SB_T05C_df = bor_ch_crime_df[bor_ch_crime_df["Borough"] == T10S_boroughs[1]].sort_values(by = "Total", ascending = False).head()
N02SB_T05C_df


# In[91]:


N02SB_T05C_df_new = N02SB_T05C_df[["Borough", "Crime Head", "Total"]]
N02SB_T05C_df_new.set_index("Borough", inplace = True)
N02SB_T05C_df_new


# #### Bar Chart for the Top 5 Crimes in the No. 2 Safest Borough of London

# In[92]:


N02SB_T05C_bar = px.bar(
                            N02SB_T05C_df_new,
                            title = "Top 5 Crimes in the No. 2 Safest Borough of London",
                            color = "Crime Head",
                            barmode = "group",
                            width = 900,
                            height = 600
                       )

N02SB_T05C_bar.show()


# ### c) Top 5 Crimes in the No. 3 Safest Borough of London<a name="c"></a>

# In[93]:


print('The No. 3 Safest Borough of London is "' + T10S_boroughs[2] + '"')


# In[94]:


N03SB_T05C_df = bor_ch_crime_df[bor_ch_crime_df["Borough"] == T10S_boroughs[2]].sort_values(by = "Total", ascending = False).head()
N03SB_T05C_df


# In[95]:


N03SB_T05C_df_new = N03SB_T05C_df[["Borough", "Crime Head", "Total"]]
N03SB_T05C_df_new.set_index("Borough", inplace = True)
N03SB_T05C_df_new


# #### Bar Chart for the Top 5 Crimes in the No. 3 Safest Borough of London

# In[96]:


N03SB_T05C_bar = px.bar(
                            N03SB_T05C_df_new,
                            title = "Top 5 Crimes in the No. 3 Safest Borough of London",
                            color = "Crime Head",
                            barmode = "group",
                            width = 900,
                            height = 600
                       )

N03SB_T05C_bar.show()


# ### d) Top 5 Crimes in the No. 4 Safest Borough of London<a name="d"></a>

# In[97]:


print('The No. 4 Safest Borough of London is "' + T10S_boroughs[3] + '"')


# In[98]:


N04SB_T05C_df = bor_ch_crime_df[bor_ch_crime_df["Borough"] == T10S_boroughs[3]].sort_values(by = "Total", ascending = False).head()
N04SB_T05C_df


# In[99]:


N04SB_T05C_df_new = N04SB_T05C_df[["Borough", "Crime Head", "Total"]]
N04SB_T05C_df_new.set_index("Borough", inplace = True)
N04SB_T05C_df_new


# #### Bar Chart for the Top 5 Crimes in the No. 4 Safest Borough of London

# In[100]:


N04SB_T05C_bar = px.bar(
                            N04SB_T05C_df_new,
                            title = "Top 5 Crimes in the No. 4 Safest Borough of London",
                            color = "Crime Head",
                            barmode = "group",
                            width = 900,
                            height = 600
                       )

N04SB_T05C_bar.show()


# ### e) Top 5 Crimes for the No. 5 Safest Borough of London<a name="e"></a>

# In[101]:


print('The No. 5 Safest Borough of London is "' + T10S_boroughs[4] + '"')


# In[102]:


N05SB_T05C_df = bor_ch_crime_df[bor_ch_crime_df["Borough"] == T10S_boroughs[4]].sort_values(by = "Total", ascending = False).head()
N05SB_T05C_df


# In[103]:


N05SB_T05C_df_new = N05SB_T05C_df[["Borough", "Crime Head", "Total"]]
N05SB_T05C_df_new.set_index("Borough", inplace = True)
N05SB_T05C_df_new


# #### Bar Chart for the Top 5 Crimes in the No. 5 Safest Borough of London

# In[104]:


N05SB_T05C_bar = px.bar(
                            N05SB_T05C_df_new,
                            title = "Top 5 Crimes in the No. 5 Safest Borough of London",
                            color = "Crime Head",
                            barmode = "group",
                            width = 900,
                            height = 600
                       )

N05SB_T05C_bar.show()


# ## 13) Top 5 Crimes in the 5 Most Safest Boroughs of London Grouped By "Boroughs"<a name="13"></a>

# ### Merging the Dataframes of the Top 5 Crimes of the 5 Most Safest Boroughs of London into a Single Dataframe

# In[105]:


df = [N01SB_T05C_df, N02SB_T05C_df, N03SB_T05C_df, N04SB_T05C_df, N05SB_T05C_df]


# In[106]:


Top05SB_df = pd.DataFrame()
Top05SB_df = Top05SB_df.append(df, ignore_index = True)


# In[107]:


Top05SB_df.set_index("Borough", inplace = True)
Top05SB_df


# In[108]:


Top05SB_df.info()


# ### Plotting the Grouped Bar Chart for the Top 5 Crimes of the 5 Most Safest Boroughs of London

# In[109]:


Top05SB_df_new = Top05SB_df[["Crime Head", "Total"]]
Top05SB_df_new


# In[110]:


Top05SB_bar = px.bar(
                        Top05SB_df_new,
                        title = "Top 5 Crimes of the 5 Most Safest Boroughs of London",
                        color = "Crime Head",
                        barmode = "group",
                        width = 900,
                        height = 600
                     )
Top05SB_bar.show()


# ## 14) Top 10 Crimes in the 5 Most Safest Boroughs of London Grouped By "Crime Head"<a name="14"></a>

# ### Merging the Dataframes of the Top 10 Crimes of the 5 Most Safest Boroughs of London into a Single Dataframe

# In[111]:


T10C_df = pd.DataFrame()

for i in range(5):
    data_df = pd.DataFrame()
    data_df = bor_ch_crime_df[bor_ch_crime_df["Borough"] == T10S_boroughs[i]].sort_values(by = "Total", ascending = False).head(10)
    T10C_df = T10C_df.append(data_df, ignore_index = True)


# In[112]:


T10C_df


# In[113]:


T10C_Top05SB_df = T10C_df[["Borough", "Crime Head", "Total"]]
T10C_Top05SB_df = T10C_Top05SB_df.reindex(["Crime Head", "Borough", "Total"], axis = 1)
T10C_Top05SB_df.sort_values(["Total"], ascending = False, inplace = True)
T10C_Top05SB_df.sort_values(["Crime Head", "Total", "Borough"], ascending = False, inplace = True)
T10C_Top05SB_df


# #### Top 10 Crimes in Descending Order

# In[114]:


T10C_bct_df = T10C_df[["Borough", "Crime Head", "Total"]]
T10C_bct_df = T10C_bct_df.groupby("Crime Head").sum()
T10C_bct_df.sort_values(["Total"], ascending = False, inplace = True)
T10C_bct_df


# #### List of Top 10 Crimes in Descending Order

# In[115]:


T10C_bct_df.index


# In[116]:


T10C_bct_list = [str(i) for i in list(T10C_bct_df.index)]
T10C_bct_list


# In[117]:


T10C_bct_list[0]


# #### Creating a Dataframe of Top 10 Crimes in the Descending Order of the Total Crimes recorded in the 5 Most Safest Boroughs of London

# In[118]:


T10C_df_new = pd.DataFrame()

for i in range(10):
    data_df_new = pd.DataFrame()
    data_df_new = T10C_Top05SB_df[T10C_Top05SB_df["Crime Head"] == T10C_bct_list[i]].sort_values(by = "Total", ascending = False)
    T10C_df_new = T10C_df_new.append(data_df_new, ignore_index = True)

T10C_df_new.set_index("Crime Head", inplace = True)
T10C_df_new


# In[119]:


T10C_Top05SB_bar = px.bar(
                                T10C_df_new,
                                title = "Top 10 Crimes of the 5 Most Safest Boroughs of London",
                                color = "Borough",
                                barmode = "group",
                                width = 1000,
                                height = 700
                         )
T10C_Top05SB_bar.show()


# ## 15) Month on Month Crime Rate for the Top 5 Crimes in the 5 Most Safest Boroughs<a name="15"></a>

# In[120]:


T05C_mom_Top05SB_df = Top05SB_df.copy(deep = True)
T05C_mom_Top05SB_df.drop(["Crime Head", "Total"], axis = 1, inplace = True)
T05C_mom_Top05SB_df


# In[121]:


T05C_bor_line = T05C_mom_Top05SB_df.groupby("Borough").sum().transpose()
T05C_bor_line


# #### Note: Above we find that when we Transpose the Dataframe, the positions of the columns change. Now, the sequence of the columns is very important for us as we use the same to display the Rankings of the Safest Boroughs, i.e., the First Column is the No. 1 Most Safest Borough, the Second Column is the No. 2 Most Safest Borough, and so on. In order to change the position of the columns, we do the following,

# In[122]:


columns = [T10S_boroughs[0], T10S_boroughs[1], T10S_boroughs[2], T10S_boroughs[3], T10S_boroughs[4]]
columns


# In[123]:


T05C_bor_line = T05C_bor_line.reindex(columns, axis = 1)
T05C_bor_line


# #### X-Axis for the Line Chart

# In[124]:


T05C_years = [str(year) for year in list(T05C_bor_line.index.values)]
T05C_years


# #### Y-Axis for the Line Chart

# In[125]:


T05C_boroughs = [str(year) for year in list(T05C_bor_line.columns.values)]
T05C_boroughs


# In[126]:


T05C_bor_line[T05C_boroughs[0]]


# #### "name" Parameter for the Line Chart

# In[127]:


T05C_boroughs[0]


# In[128]:


line = go.Figure()

line.add_trace(go.Scatter(x = T05C_years, y = T05C_bor_line[T05C_boroughs[0]], name = T05C_boroughs[0], mode = "lines + markers", line=dict(color='black', width=2)))
line.add_trace(go.Scatter(x = T05C_years, y = T05C_bor_line[T05C_boroughs[1]], name = T05C_boroughs[1], mode = "lines + markers", line=dict(color='royalblue', width=2)))
line.add_trace(go.Scatter(x = T05C_years, y = T05C_bor_line[T05C_boroughs[2]], name = T05C_boroughs[2], mode = "lines + markers", line=dict(color='yellow', width=2)))
line.add_trace(go.Scatter(x = T05C_years, y = T05C_bor_line[T05C_boroughs[3]], name = T05C_boroughs[3], mode = "lines + markers", line=dict(color='green', width=2)))
line.add_trace(go.Scatter(x = T05C_years, y = T05C_bor_line[T05C_boroughs[4]], name = T05C_boroughs[4], mode = "lines + markers", line=dict(color='magenta', width=2)))

line.update_layout(title = "Month on Month Crime Rate for the Top 5 Crimes of the 5 Most Safest Boroughs of London", xaxis_title = "Month & Year", yaxis_title = "Total No. of Crimes")

line.show()


# ## 16) Top 50 Most Safest Wards in the 5 Most Safest Boroughs of London<a name="16"></a>

# In[129]:


bor_ward_crime_df = crime_df.copy(deep = True)
bor_ward_crime_df = bor_ward_crime_df[["Borough", "Ward", "Total"]]
bor_ward_crime_df = bor_ward_crime_df.groupby(["Borough", "Ward"]).sum()
bor_ward_crime_df.reset_index(inplace = True)
bor_ward_crime_df


# In[130]:


for i in range(5):
    print(T10S_boroughs[i])


# In[131]:


T10W_df = pd.DataFrame()

for i in range(5):
    data_df_updated = pd.DataFrame()
    data_df_updated = bor_ward_crime_df[bor_ward_crime_df["Borough"] == T10S_boroughs[i]].sort_values(by = "Total", ascending = True).head(10)
    T10W_df = T10W_df.append(data_df_updated, ignore_index = True)


# ### Top 50 Most Safest Wards in London Grouped by "Borough" and Sorted by "Total"

# In[132]:


T10W_df.to_csv("Top 50 Most Safest Wards in London.csv")


# In[133]:


T10W_df


# In[134]:


T10W_df_bar = px.pie(
                        T10W_df,
                        title = "Top 50 Most Safest Wards in the 5 Most Safest Boroughs of London",
                        values = "Total",
                        names = "Ward",
                        color = "Borough",
                        width = 900,
                        height = 700
                     )
T10W_df_bar.show()


# ### Top 10 Most Safest Wards in London, Sorted on "Total"

# In[135]:


T10W_df_new = T10W_df.copy(deep = True)
T10W_df_new.reset_index(inplace = True)
T10W_df_new = T10W_df_new.reindex(["Ward", "Borough", "Total"], axis = 1)
T10W_df_new.sort_values(by = ["Total", "Ward", "Borough"], inplace = True)
T10W_df_new.reset_index(inplace = True)
T10W_df_new.drop(["index"], axis = 1, inplace = True)
T10W_df_new


# In[136]:


T10W_df_new_bar = px.pie(
                        T10W_df_new,
                        title = "Top 50 Most Safest Wards in the 5 Most Safest Boroughs of London",
                        values = "Total",
                        names = "Ward",
                        color = "Borough",
                        width = 900,
                        height = 700
                     )
T10W_df_new_bar.show()


# # D) Collecting the Coordinates and Plotting them on the Map of London:<a name="D"></a>

# ## (i) Creating a Crime Dataframe of the Top 5 Boroughs<a name="Crime_Dataframe"></a>

# In[137]:


all_crime_df = crime_df[["Ward Code", "Ward", "Borough", "Crime Head", "Crime Sub-Head", "Total"]]

Top5_bor_crime_df = pd.DataFrame()

for i in range(5):
    data_df_updated = pd.DataFrame()
    data_df_updated = all_crime_df[all_crime_df["Borough"] == T10S_boroughs[i]]
    Top5_bor_crime_df = Top5_bor_crime_df.append(data_df_updated, ignore_index = True)

Top5_bor_crime_df.to_csv("Crime in Top 5 Safest Boroughs of London.csv")
Top5_bor_crime_df


# ## (ii) Merging Crime Dataframe of the Top 5 Boroughs with Top 50 Most Safest Wards<a name="Merging_Dataframes"></a>

# ### Dropping the "Total" Column from the Top 50 Most Safest Wards in London Dataframe

# In[138]:


T10W_df_updated = T10W_df_new.copy(deep = True)
T10W_df_updated.drop(["Total"], axis = 1, inplace = True)
T10W_df_updated


# In[139]:


T10W_crime_df = pd.merge(T10W_df_updated, Top5_bor_crime_df, on = 'Ward')
T10W_crime_df.drop(["Borough_y"], axis = 1, inplace = True)
T10W_crime_df = T10W_crime_df.reindex(["Ward Code", "Ward", "Borough_x", "Crime Head", "Crime Sub-Head", "Total"], axis = 1)
T10W_crime_df.columns = ["Ward Code", "Ward", "Borough", "Crime Head", "Crime Sub-Head", "Total"]
T10W_crime_df.to_csv("Crime in Top 50 Safest Wards of London.csv")
T10W_crime_df


# ## (iii) Extracting the Postcodes of the Top 50 Safest Wards of London<a name="Postcodes"></a>

# ### Since we will be working only on the Top 5 Most Safest Boroughs of London, we can drop the data for the rest of the Boroughs from the "london_postcodes_df" Dataset

# In[140]:


top5_bor_postcode_df = london_postcodes_df.copy(deep = True)


# In[141]:


postcode_top5_bor_df = pd.DataFrame()

for i in range(5):
    dataset_new = pd.DataFrame()
    dataset_new = top5_bor_postcode_df[top5_bor_postcode_df["Borough"] == T10S_boroughs[i]]
    postcode_top5_bor_df = postcode_top5_bor_df.append(dataset_new, ignore_index = True)


# In[142]:


postcode_top5_bor_df.to_csv("Postcodes of Top 5 Safest Boroughs of London.csv")
postcode_top5_bor_df


# ### We will now filter the Top 50 Most Safest Wards of London from the above Dataset of Top 5 Most Safest Boroughs

# In[143]:


postcode_top50_ward_df = pd.DataFrame()

for i in range(len(T10W_df_updated)):
    dataset_updated = pd.DataFrame()
    dataset_updated = postcode_top5_bor_df[postcode_top5_bor_df["Ward"] == T10W_df_updated["Ward"][i]]
    postcode_top50_ward_df = postcode_top50_ward_df.append(dataset_updated, ignore_index = True)


# In[144]:


postcode_top50_ward_df.to_csv("Postcodes of Top 50 Safest Wards of London.csv")
postcode_top50_ward_df


# ### So far, we have tried to find Areas that were the Safest in London, first by finding the 5 Most Safest Boroughs and then by finding the 50 Most Safest Wards within the 5 Safest Boroughs. But we still have 10,000 plus Locations in the Dataset. In order to reduce the Dataset further, we will select only those Locations that are Nearest to the Station.

# ## (iv) Selecting Locations Nearest to a Station<a name="Nearest_Station"></a>

# In[145]:


min_dist_station_df = postcode_top50_ward_df.groupby(["Nearest Station", "Distance To Station"]).min()
min_dist_station_df.reset_index(inplace = True)
min_dist_station_df.to_csv("Minimum Distance to Stations in Top 50 Safe Wards of London.csv")
min_dist_station_df


# ### Identifying the Stations in the Dataset

# In[146]:


min_dist_station_df["Nearest Station"].unique()


# In[147]:


min_dist_station_df.nunique()


# ### Keeping only those Locations that are the Closest to the Stations and Dropping the rest of the Locations

# In[148]:


nearest_to_station_df = min_dist_station_df.drop_duplicates(subset = ["Nearest Station"], keep = "first")
nearest_to_station_df.reset_index(inplace = True)
nearest_to_station_df.drop(["index"], axis = 1, inplace = True)
nearest_to_station_df.to_csv("Nearest Station to Top 50 Safest Wards of London.csv")
nearest_to_station_df


# In[149]:


nearest_to_station_df.nunique()


# ### Now, the Postcodes Dataframe has only 81 records

# ### Note: Even though the "nearest_to_station_df" Dataframe already has the Latitude and the Longitude Data available as a part of the Dataframe, we will still try to fetch the Coordinates of the Postcodes by Identifying the Geolocations Using the Arcgis API

# ## (v) Fetching Coordinates by Using the Arcgis API<a name="ArcGIS_API"></a>

# ### Identifying the Geolocations Using Arcgis API

# In[150]:


from arcgis.geocoding import geocode
from arcgis.gis import GIS
gis = GIS()


# ### Defining the London Arcgis Geocode Function to get the Latitude and Longitude Using the Postcode

# In[151]:


def get_coordinates_uk(address):
   latitude_coordinates = 0
   longitude_coordinates = 0
   g = geocode(address = "{}, London, England, GBR".format(address))[0]
   longitude_coordinates = g["location"]["x"]
   latitude_coordinates = g["location"]["y"]
   return str(latitude_coordinates) + "," + str(longitude_coordinates)


# ### Testing if the Function performs well

# In[152]:


cor = get_coordinates_uk("KT1 3RN")
cor


# In[153]:


cor = get_coordinates_uk("KT6 5RY")
cor


# In[154]:


cor = get_coordinates_uk("KT6 5PT")
cor


# In[155]:


cor = get_coordinates_uk("TW7")
cor


# ### Segregating the Unique Postcodes from the Dataframe

# In[156]:


london_postcodes = nearest_to_station_df.loc[ : , "Postcode Data"]
london_postcodes


# In[157]:


london_postcodes_dfnew = pd.DataFrame(london_postcodes)
post_cols = ["Postcodes"]
london_postcodes_dfnew.columns = post_cols
london_postcodes_dfnew


# ### Using the "get_coordinates_uk" Function to retrieve the Latitudes and Longitudes for the Top 50 Safest Wards of London 

# In[158]:


london_coordinates = []

for i in range(len(london_postcodes)):
    london_coordinates.append(get_coordinates_uk(london_postcodes[i]))

london_coordinates


# ### Extracting the Latitude from the "london_coordinates"

# In[159]:


london_latitude = []

for i in range(len(london_coordinates)):
    lat = london_coordinates[i].split(",")[0]
    lat = round(float(lat), 5)
    london_latitude.append(lat)


# In[160]:


london_latitude_df = pd.DataFrame(london_latitude)
lat_cols = ["Latitude"]
london_latitude_df.columns = lat_cols
london_latitude_df


# ### Extracting the Longitude from the "london_coordinates"

# In[161]:


london_longitude = []

for i in range(len(london_coordinates)):
    long = london_coordinates[i].split(",")[1]
    long = round(float(long), 5)
    london_longitude.append(long)


# In[162]:


london_longitude_df = pd.DataFrame(london_longitude)
long_cols = ["Longitude"]
london_longitude_df.columns = long_cols
london_longitude_df


# In[163]:


print("No. of Rows in each Dataframe: Postcodes = " + str(len(london_postcodes_dfnew)) + "; Latitude = " + str(len(london_latitude_df)) + "; Latitude = " + str(len(london_longitude_df)))


# ### Merging the Data on Postcodes, Latitude & Longitude into one Dataframe

# In[164]:


london_pc_df = pd.concat([london_postcodes_dfnew, london_latitude_df, london_longitude_df], axis=1)
london_pc_df


# ### Merging the "london_pc_df" Dataframe with the "nearest_to_station_df"

# In[165]:


nearest_to_station_coordinates_df = pd.concat([nearest_to_station_df, london_pc_df], join = "outer", axis=1)
postcode_cols_new = ["Nearest Station", "Distance To Station", "Postcodes", "Latitude", "Longitude", "Ward Code", "Ward", "Borough Code", "Borough", "Constituency Code", "Constituency", "LSOA Code", "Lower Layer Super Output Area", "MSOA Code", "Middle Layer Super Output Area", "London Zone", "Postcode Area", "Postcode District", "Easting", "Northing", "Grid Ref", "Postcode Data", "Latitude Data", "Longitude Data"]
nearest_to_station_coordinates_df = nearest_to_station_coordinates_df.reindex(postcode_cols_new, axis = 1)
nearest_to_station_coordinates_df


# ### As discussed above, in order to reduce the number of locations, we have selected only those locations that are Nearest to the Station. Accordingly, we fetched the coordinates of only those locations that were very close to the respective Stations. Now, apart from safe Neighbourhoods, our Target Audience is also looking at Venues that are close to the Station so that it is convenient for them to travel. Since we will be identifying Venues that are close to the Station, we will rename the column "Nearest Station" to "Neighbourhood"

# In[166]:


postcode_cols_updated = ["Neighbourhood", "Distance To Station", "Postcodes", "Latitude", "Longitude", "Ward Code", "Ward", "Borough Code", "Borough", "Constituency Code", "Constituency", "LSOA Code", "Lower Layer Super Output Area", "MSOA Code", "Middle Layer Super Output Area", "London Zone", "Postcode Area", "Postcode District", "Easting", "Northing", "Grid Ref", "Postcode Data", "Latitude Data", "Longitude Data"]
nearest_to_station_coordinates_df.columns = postcode_cols_updated
neighbourhood_df = nearest_to_station_coordinates_df.reindex(postcode_cols_updated, axis = 1)
neighbourhood_df.to_csv("Neighbourhoods of Top 50 Safest Wards of London with Coordinates.csv")
neighbourhood_df


# In[167]:


neighbourhood_df.info()


# ## (vi) Plotting Stations on the Map of London<a name="Plot_Stations"></a>

# In[168]:


address = "London, England"

geolocator = Nominatim(user_agent = "london_explorer")
location = geolocator.geocode(address)
latitude = location.latitude
longitude = location.longitude
print("The coordinates of London are {}, {}.".format(latitude, longitude))


# ### Plotting All Stations of London on the Map of London

# In[169]:


london_postcodes_df.info()


# In[170]:


london_postcodes_df.nunique()


# In[171]:


min_dist_all_station_df = london_postcodes_df.groupby(["Nearest Station", "Distance To Station"]).min()
min_dist_all_station_df.reset_index(inplace = True)
min_dist_all_station_df.to_csv("Minimum Distance to All Stations.csv")
min_dist_all_station_df


# In[172]:


station_df = min_dist_all_station_df.drop_duplicates(subset = ["Nearest Station"], keep = "first")
station_df.reset_index(inplace = True)
station_df.drop(["index"], axis = 1, inplace = True)
station_df.to_csv("Nearest Station to the Respective Wards of London.csv")
station_df


# In[173]:


station_df.nunique()


# In[174]:


# Creating the map of London
map_London_all_stations = folium.Map(location = [latitude, longitude], zoom_start = 10)

# Adding markers to map
for latitude, longitude, borough, ward, neighbourhood in zip(station_df["Latitude Data"], station_df["Longitude Data"], station_df["Borough"], station_df["Ward"], station_df["Nearest Station"]):
    label = "{}, {}, {}".format(neighbourhood, ward, borough)
    label = folium.Popup(label, parse_html = True)
    folium.CircleMarker(
                            [latitude, longitude],
                            radius = 5,
                            popup = label,
                            color = "red",
                            fill = True
                        ).add_to(map_London_all_stations)  
    
map_London_all_stations


# ### Plotting Stations in the Safest Wards of London on the Map of London

# In[175]:


# Creating the map of London
map_London_safe_neigh = folium.Map(location = [latitude, longitude], zoom_start = 10)

# Adding markers to map
for latitude, longitude, borough, ward, neighbourhood in zip(neighbourhood_df["Latitude"], neighbourhood_df["Longitude"], neighbourhood_df["Borough"], neighbourhood_df["Ward"], neighbourhood_df["Neighbourhood"]):
    label = "{}, {}, {}".format(neighbourhood, ward, borough)
    label = folium.Popup(label, parse_html = True)
    folium.CircleMarker(
                            [latitude, longitude],
                            radius = 5,
                            popup = label,
                            color = "blue",
                            fill = True
                        ).add_to(map_London_safe_neigh)  
    
map_London_safe_neigh


# # E) Identifying Venues around the Safe Neighbourhoods of London:<a name="E"></a>

# ## (i) Defining Foursquare API Credentials<a name="Credentials"></a>

# In[176]:


CLIENT_ID = "DVS0H5U52KP03MEJUX0WCA0SZ1SQB2ASHNNRRB4SIT2GWJ3U" # your Foursquare ID
CLIENT_SECRET = "SCZJLODKBUVU2BSHU3MAEKUXR0BRDIDCQILD3QQW1X4PUW2Y" # your Foursquare Secret
VERSION = "20180605" # Foursquare API version
LIMIT = 100 # A default Foursquare API limit value

print("Your credentails:")
print("CLIENT_ID: " + CLIENT_ID)
print("CLIENT_SECRET: " + CLIENT_SECRET)


# ## (ii) Creating a Function to Get All the Venue Categories in London<a name="Function"></a>

# In[177]:


def getNearbyVenues(names, wards, boroughs, latitudes, longitudes, radius = 500):
    
    venues_list = []
    for name, ward, borough, lat, lng in zip(names, wards, boroughs, latitudes, longitudes):
        print(name)
            
        # create the API request URL
        url = "https://api.foursquare.com/v2/venues/explore?&client_id={}&client_secret={}&v={}&ll={},{}&radius={}".format(
                    CLIENT_ID, 
                    CLIENT_SECRET, 
                    VERSION, 
                    lat, 
                    lng, 
                    radius
                    )
            
        # make the GET request
        results = requests.get(url).json()["response"]["groups"][0]["items"]
        
        # return only relevant information for each nearby venue
        venues_list.append([(
                                name,
                                ward,
                                borough,
                                lat, 
                                lng, 
                                v["venue"]["name"],
                                v["venue"]["categories"][0]["name"],
                                v["venue"]["location"]["lat"],
                                v["venue"]["location"]["lng"]
                            ) for v in results])

    nearby_venues = pd.DataFrame([item for venue_list in venues_list for item in venue_list])
    nearby_venues.columns = ["Neighbourhood", "Ward", "Borough", "Neighbourhood Latitude", "Neighbourhood Longitude", "Venue", "Venue Category", "Venue Latitude", "Venue Longitude"]
    
    return (nearby_venues)


# ## (iii) Gathering Information of Venues in the Safe Neighbourhoods of London<a name="Venue_Information"></a>

# In[178]:


venues_london = getNearbyVenues(neighbourhood_df["Neighbourhood"], neighbourhood_df["Ward"], neighbourhood_df["Borough"], neighbourhood_df["Latitude"], neighbourhood_df["Longitude"])


# In[179]:


venues_london.shape


# In[180]:


venues_london.to_csv("Venues in Safe Neighbourhoods of London.csv")
venues_london.head()


# In[181]:


venues_london.info()


# ## (iv) Analysing the Dataset<a name="Analyse"></a>

# ### Grouped by Neighbourhood

# In[182]:


neighbourhood_group = venues_london.groupby("Neighbourhood").count()
neighbourhood_group.to_csv("Grouped By Neighbourhood - Venues in Safe Neighbourhoods of London.csv")
neighbourhood_group


# ### Grouped by Venue Category

# In[183]:


venuecat_group = venues_london.groupby("Venue Category").count()
venuecat_group.to_csv("Grouped By Venue Category - Venues in Safe Neighbourhoods of London.csv")
venuecat_group


# ### Grouped by Venue Category & Venue

# In[184]:


venuecat_venue_group = venues_london.groupby(["Venue Category", "Venue"]).count()
venuecat_venue_group.to_csv("Grouped By Venue Category & Venue - Venues in Safe Neighbourhoods of London.csv")
venuecat_venue_group


# ### Grouped by Wards of London

# In[185]:


ward_group = venues_london.groupby("Ward").count()
ward_group.to_csv("Grouped By Ward - Venues in Safe Neighbourhoods of London.csv")
ward_group


# ### Grouped by Boroughs of London

# In[186]:


borough_group = venues_london.groupby("Borough").count()
borough_group.to_csv("Grouped By Borough - Venues in Safe Neighbourhoods of London.csv")
borough_group


# ### Grouped by Venue Category & Neighbourhood

# In[187]:


venuecat_neigh_group = venues_london.groupby(["Venue Category", "Neighbourhood"]).count()
venuecat_neigh_group.to_csv("Grouped By Venue Category & Neighbourhood - Venues in Safe Neighbourhoods of London.csv")
venuecat_neigh_group


# ### Grouped by Venue Category & Wards of London

# In[188]:


venuecat_ward_group = venues_london.groupby(["Venue Category", "Ward"]).count()
venuecat_ward_group.to_csv("Grouped By Venue Category & Ward - Venues in Safe Neighbourhoods of London.csv")
venuecat_ward_group


# ### Grouped by Venue Category & Boroughs of London

# In[189]:


venuecat_borough_group = venues_london.groupby(["Venue Category", "Borough"]).count()
venuecat_borough_group.to_csv("Grouped By Venue Category & Borough - Venues in Safe Neighbourhoods of London.csv")
venuecat_borough_group


# # F) Segmenting Neighbourhoods of London By Common Venue Categories:<a name="F"></a>

# In[190]:


venues_london.nunique()


# ## (i) One Hot Encoding<a name="OHE"></a>

# In[191]:


venues_london_ohe = pd.get_dummies(venues_london[["Venue Category"]], prefix = "", prefix_sep = "")
venues_london_ohe.head()


# ### Now we add the "Neighbourhood" Column from the Main Dataframe to the Encoded Dataframe

# In[192]:


venues_london_ohe["Neighbourhood"] = venues_london["Neighbourhood"] # This adds the "Neighbourhood" column in the end

# Moving the Neighbourhood Column to the First Column
columns = [venues_london_ohe.columns[-1]] + list(venues_london_ohe.columns[ : -1])
venues_london_ohe = venues_london_ohe[columns]

venues_london_ohe.head()


# In[193]:


neighbourhood_group_ohe = venues_london_ohe.groupby("Neighbourhood").sum()
neighbourhood_group_ohe.reset_index(inplace = True)
neighbourhood_group_ohe


# In[194]:


neighbourhood_group_ohe.shape


# ## (ii) Printing Each Neighbourhood Along with the Top 8 Most Common Venues<a name="Print"></a>

# In[195]:


num_top_venues = 8

for neigh in neighbourhood_group_ohe["Neighbourhood"]:
    print("---------"+neigh+"---------")
    temp = neighbourhood_group_ohe[neighbourhood_group_ohe["Neighbourhood"] == neigh].T.reset_index()
    temp.columns = ["Venue", "Frequency"]
    temp = temp.iloc[ 1 : ]
    temp["Frequency"] = temp["Frequency"].astype(float)
    temp = temp.round({"Frequency" : 2})
    print(temp.sort_values("Frequency", ascending = False).reset_index(drop = True).head(num_top_venues))
    print("\n")


# ## (iii) Transferring the Venues into a Pandas Dataframe<a name="Pandas_Dataframe"></a>

# #### Writing a Function to Sort the Venues in Descending Order

# In[196]:


def return_most_common_venues(row, num_top_venues):
    row_categories = row.iloc[1 : ]
    row_categories_sorted = row_categories.sort_values(ascending = False)
    
    return row_categories_sorted.index.values[0 : num_top_venues]


# #### Creating a New Dataframe and Displaying the Top 5 Venues for Each Neighbourhood

# In[197]:


indicators = ["st", "nd", "rd"]

# Create columns according to number of top Venues
columns = ["Neighbourhood"]
for ind in np.arange(num_top_venues):
    try:
        columns.append('{}{} Most Common Venue'.format(ind+1, indicators[ind]))
    except:
        columns.append('{}th Most Common Venue'.format(ind+1))

# Create a new Dataframe
neighbourhoods_venues_sorted = pd.DataFrame(columns = columns)
neighbourhoods_venues_sorted["Neighbourhood"] = neighbourhood_group_ohe["Neighbourhood"]

for ind in np.arange(neighbourhood_group_ohe.shape[0]):
    neighbourhoods_venues_sorted.iloc[ind, 1 : ] = return_most_common_venues(neighbourhood_group_ohe.iloc[ind, : ], num_top_venues)

neighbourhoods_venues_sorted.head()


# In[198]:


neighbourhoods_venues_sorted.info()


# # G) Clustering Neighbourhoods By Common Venues (K-Means Clustering):<a name="G"></a>

# ## (i) Building a Model to Cluster the Neighbourhoods<a name="Model"></a>

# #### In order to assist our Target Audience to find venues of their choice in the safest neighbourhoods of London, we will be clustering the neighbourhoods using the K-Means Clustering Algorithm. K-Means Clustering Algorithm will cluster neighbourhoods with similar venues together. This will help my Target Audience (Tourists and Migrants) to shortlist areas of their interest based on the venues around each neighbourhood.

# In[199]:


neighbourhood_group_cluster = neighbourhood_group_ohe.drop(labels = "Neighbourhood", axis = 1)


# #### We will use the Elbow Method to identify the Optimal Number of Clusters. As per this method, the optimal number of clusters is achieved when the change in slope of the line becomes small.

# In[200]:


distortions = []

K = range(1,20)
for k in K:
    kmean = KMeans(init = "k-means++", n_clusters = k, random_state = 0, n_init = 50, max_iter = 500)
    kmean.fit(neighbourhood_group_cluster)
    distortions.append(kmean.inertia_)


# In[201]:


plt.figure(figsize = (10, 5))
plt.plot(K, distortions, "bx-")
plt.xlabel("k")
plt.ylabel("Distortion")
plt.title("The Elbow Method")
plt.show()


# #### As per the Chart above, the optimal number of clusters seems to have been achieved at k = 3, as after the third cluster, the change in slope of the line is very small. In view of the same, we will run the K-Means Clustering Algorithm to Cluster the Neighbourhood Venues into 3 Clusters.

# In[202]:


# set number of clusters
k_num_clusters = 3


# #### Running k-means Clustering

# In[203]:


kmeans = KMeans(init = "k-means++", n_clusters = k_num_clusters, random_state = 0)
kmeans.fit(neighbourhood_group_cluster)


# In[204]:


# check cluster labels generated for each row in the dataframe
labels = kmeans.labels_[0 : 80]
labels


# #### Creating a new Dataframe that includes the Cluster as well as the 5 Most Common Venues in each Neighbourhood

# In[205]:


neighbourhoods_venues_sorted.insert(1, "Cluster Labels", kmeans.labels_)


# In[206]:


neighbourhoods_venues_sorted.head()


# In[207]:


neighbourhoods_venues_sorted.info()


# #### Extracting the Columns, "Neighbourhood", "Distance To Station", "Ward", "Borough", "Postcodes", "Latitude" and "Longitude", from the "neighbourhood_df" Dataframe

# In[208]:


neighbour_df = neighbourhood_df[["Neighbourhood", "Distance To Station", "Ward", "Borough", "Postcodes", "Latitude", "Longitude"]].copy(deep = True)
neighbour_df


# #### Merging "neighbourhoods_venues_sorted" with "neighbour_df" on the "Neighbourhood" Column for Plotting the Clusters on the Map of London

# In[209]:


london_merged = neighbour_df
london_merged = london_merged.join(neighbourhoods_venues_sorted.set_index("Neighbourhood"), on = "Neighbourhood")
london_merged.to_csv("Neighbourhoods of London with Cluster Labels.csv")
london_merged.head()


# In[210]:


london_merged.info()


# #### We find that there are 81 Rows in the "neighbour_df" Dataframe while the "neighbourhoods_venues_sorted" Dataframe, there are only 80 Rows

# #### Hence, in order to avoid skewing of data, we will Drop all the NaN values 

# In[211]:


london_merged = london_merged.dropna(subset = ["Cluster Labels"])


# In[212]:


london_merged.info()


# #### Now the number of Rows are equal. We can, therefore, proceed.

# ## (ii) Principal Component Analysis (PCA)<a name="PCA"></a>

# ### Using PCA to visualise high dimensional data, in order to see how the Clusters are related in the original space

# #### Applying Dimensionality Reduction Techniques helps in visualising how the Clusters are related in the original high dimensional space. It also helps in finding if the features of the data are linearly related to each other.

# In[213]:


pca = PCA().fit(neighbourhood_group_cluster)
pca_neigh = pca.transform(neighbourhood_group_cluster)
print("Variance Explained by Each Component (%): ")
for i in range(len(pca.explained_variance_ratio_)):
      print("\n", i+1, "º: " + str(round(pca.explained_variance_ratio_[i] * 100, 2)) + "%")
print("\nTotal Sum: " + str(round(sum(pca.explained_variance_ratio_) * 100, 2)) + "%")
print("\nExplained Variance of the First Eight Components, i.e. 10% of the Total Components: " + str(round(sum(pca.explained_variance_ratio_[0 : 8]) * 100, 2)) + "%")


# #### It can be seen that 10% of the Total Components, i.e., the first eight components, are able to preserve about 74% of the original information, thus, reducing the dimensionality of our data

# In[214]:


c1 = []
c2 = []
c3 = []


for i in range(len(pca_neigh)):
    if kmeans.labels_[i] == 0:
        c1.append(pca_neigh[i])
    if kmeans.labels_[i] == 1:
        c2.append(pca_neigh[i])
    if kmeans.labels_[i] == 2:
        c3.append(pca_neigh[i])
        
        
c1 = np.array(c1)
c2 = np.array(c2)
c3 = np.array(c3)


plt.figure(figsize = (10, 8))
plt.scatter(c1[ : , 0], c1[ : , 1], c = "red", label = "Cluster 1")
plt.scatter(c2[ : , 0], c2[ : , 1], c = "blue", label = "Cluster 2")
plt.scatter(c3[ : , 0], c3[ : , 1], c = "green", label = "Cluster 3")


plt.legend()
plt.xlabel("PC1")
plt.ylabel("PC2")
plt.title("Low Dimensional Visualisation (PCA) - Neighbourhoods")


# ## (iii) Visualising the Resulting Clusters on the Map of London<a name="Map"></a>

# In[215]:


london_merged


# In[216]:


# Create Map of London
map_clusters = folium.Map(location = [latitude, longitude], zoom_start = 10)

# Set color scheme for the clusters
x = np.arange(k_num_clusters)
ys = [i + x + (i * x) ** 2 for i in range(k_num_clusters)]
colors_array = cm.rainbow(np.linspace(0, 1, len(ys)))
rainbow = [colors.rgb2hex(i) for i in colors_array]

for lat, lon, mcv, poi, ward, bor, cluster in zip(london_merged["Latitude"], london_merged["Longitude"], london_merged["1st Most Common Venue"], london_merged["Neighbourhood"], london_merged["Ward"], london_merged["Borough"], london_merged["Cluster Labels"]):
    label = folium.Popup("Cluster " + str(int(cluster) + 1) + ":\n" + str(mcv) + ",\n" + str(poi) + ",\n" + str(ward) + ",\n" + str(bor), parse_html = True)
    folium.CircleMarker(
                            [lat, lon],
                            radius = 5,
                            popup = label,
                            color = rainbow[int(cluster - 1)],
                            fill = True,
                            fill_color = rainbow[int(cluster - 1)],
                            fill_opacity = 0.5
                        ).add_to(map_clusters)
        
map_clusters


# ## (iv) Examining the Clusters<a name="Examine"></a>

# #### Cluster 1:

# In[217]:


cluster_1 = london_merged.loc[london_merged["Cluster Labels"] == 0, london_merged.columns[[0] + [2] + [3] + list(range(7, london_merged.shape[1]))]]
cluster_1.to_csv("Venues in the Neighbourhood of London - Cluster 1.csv")
cluster_1


# In[218]:


cluster_1.info()


# #### Cluster 2:

# In[219]:


cluster_2 = london_merged.loc[london_merged["Cluster Labels"] == 1, london_merged.columns[[0] + [2] + [3] + list(range(7, london_merged.shape[1]))]]
cluster_2.to_csv("Venues in the Neighbourhood of London - Cluster 2.csv")
cluster_2


# In[220]:


cluster_2.info()


# #### Cluster 3:

# In[221]:


cluster_3 = london_merged.loc[london_merged["Cluster Labels"] == 2, london_merged.columns[[0] + [2] + [3] + list(range(7, london_merged.shape[1]))]]
cluster_3.to_csv("Venues in the Neighbourhood of London - Cluster 3.csv")
cluster_3


# In[222]:


cluster_3.info()


# # <u>Results and Discussion</u>:<a name="Result"></a>

# ### The aim of this project is to help the Migrants and Tourists who want to explore the safest neighbourhoods of London. They can decide to stay or visit a specific neighbourhood based on their preferred cluster. Based on the type of clusters, different people, i.e., families with children, young couples, executives or tourists, can decide which neighbourhood is best suited for them.
# 
# ### - Cluster 1:
# **This cluster is mostly made up of Pubs, Coffee Shops, Cafe, Multi Cultural Restaurants, Bars, Gyms, Sports Clubs, Supermarkets, Grocery Stores, Shopping Plazas, Fast-food Joints, etc. Thus, this cluster is most suitable for young couples and executives.**
# 
# ### - Cluster 2:
# **This is the biggest cluster from our Dataset and is mostly made up of Supermarkets, Bakeries, Pharmacies, Auto Garages, Parks, Playgrounds, Sports Complexes, Multi Cultural Restaurants, Ice Cream Parlours, Fish & Chips Shops, Pubs, various stores like, Grocery, Convenience, Clothing, Furniture, Pet, Optical, Electronics, Warehouse, etc., and Train Stations. It has almost everything that a family requires. Thus, this cluster seems to be most suitable for families with children.**
# 
# ### - Cluster 3:
# **This cluster is mostly made up of Hotels, Pubs, Theatres, Art Galleries, Art Museums, Outdoor Sculptures and Plazas. Thus, this cluster is most suitable for Tourists.**
# 
# ### The above segmentation is also proved right from the PCA Chart. According to PCA, Cluster 1 and Cluster 2 seem to be Linearly Related, while Cluster 3 is not at all related to the other two clusters. As can be seen above, Clusters 1 & 2 seem to suit Migrants, who intend to stay in neighbourhoods falling in those clusters, while Cluster 3 seems to suit Tourists, who intend to visit neighbourhoods falling in that cluster.

# # <u>Conclusion</u>:<a name="Conclusion"></a>

# ### This Capstone Project will help families with children, young couples, executives and tourists, to understand,
# - **which are the safe Boroughs, Wards and Neighbourhoods of London**
# - **the most common venues in those neighbourhoods**
# - **the different types of neighbourhoods based on the cluster of venue catogeries**
# - **which neighbourhoods to choose as per their preference**
# 
# ### As can be seen from the data on clusters, the aim of the project to seems to have been fulfilled.
