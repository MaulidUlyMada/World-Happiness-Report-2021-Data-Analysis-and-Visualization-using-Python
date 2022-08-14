# -*- coding: utf-8 -*-
"""World Happiness Report 2021 Data Analysis and Visualization using Python.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1Xf3rfZIfpFXRE2GNX1uojfYGMHgtRLQ8
"""

# Commented out IPython magic to ensure Python compatibility.
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
# %matplotlib inline

sns.set_style("whitegrid")
plt.rcParams['font.size'] = 15
plt.rcParams["figure.figsize"] = (10,7)
plt.rcParams ["figure.facecolor"] = "#FFE5B4"

from google.colab import drive
drive.mount('/content/drive')

happiness_data = pd.read_csv("/content/drive/My Drive/Dataset/world-happiness-report-2021.csv")

happiness_data.head()

happiness_data_columns = ["Country name", "Regional indicator", "Ladder score", "Logged GDP per capita", "Social support", "Healthy life expectancy", "Freedom to make life choices", "Generosity", "Perceptions of corruption"]

happiness_data = happiness_data[happiness_data_columns].copy()

happiness_df = happiness_data.rename(columns = {"Country name":"country_name", "Regional indicator":"regional_indicator", "Ladder score":"happiness_score", "Logged GDP per capita":"logged_gdp_per_capita", "Social support":"social_support", "Healthy life expectancy":"healthy_life_expectancy", "Freedom to make life choices":"freedom_to_make_life_choices", "Generosity":"generosity", "Perceptions of corruption":"perceptions_of_corruption"})

happiness_df.columns

happiness_df.head()

happiness_df.isnull().sum()

#Plot between happiness and GDP

plt.rcParams["figure.figsize"] = (15, 7)
plt.title("Plot between Happiness Score and GDP")
sns.scatterplot(x = happiness_df.happiness_score, y = happiness_df.logged_gdp_per_capita, hue = happiness_df.regional_indicator, s = 200);

plt.legend(loc = "upper left", fontsize = "10")
plt.xlabel("Happiness Score")
plt.ylabel("GDP per Capita")

gdp_region = happiness_df.groupby("regional_indicator")["logged_gdp_per_capita"].sum()

gdp_region

gdp_region.plot.pie(autopct = "%1.1f%%")
plt.title("GDP by Region")
plt.ylabel("")

#Total Counties

total_country = happiness_df.groupby("regional_indicator")[["country_name"]].count()
total_country

#Correlation Map

cor = happiness_df.corr(method = "pearson")
f, ax = plt.subplots(figsize = (10, 5))
sns.heatmap(cor, mask = np.zeros_like(cor, dtype = np.bool),
            cmap = "Blues", square = True, ax = ax)

#Corruption in Regions

corruption = happiness_df.groupby("regional_indicator")[["perceptions_of_corruption"]].mean()
corruption

plt.rcParams["figure.figsize"] = (12,8)
plt.title("Perceptions of Corruption in Various Regions")
plt.xlabel("Regions", fontsize = 15)
plt.ylabel("Corruption Index", fontsize = 15)
plt.xticks(rotation = 30, ha = "right")
plt.bar(corruption.index, corruption.perceptions_of_corruption)

top_10 = happiness_df.head(10)
bottom_10= happiness_df.tail(10)

fig, axes = plt.subplots(1,2,figsize = (16,6))
plt.tight_layout(pad = 2)

xlabels = top_10.country_name
axes[0].set_title("Top 10 Happiest Countries Life Expectancy")
axes[0].set_xticklabels(xlabels, rotation = 45, ha = "right")
sns.barplot(x = top_10.country_name, y = top_10.healthy_life_expectancy, ax = axes[0])
axes[0].set_xlabel("Country Name")
axes[0].set_ylabel("Life Axpectancy")

xlabels = bottom_10.country_name
axes[1].set_title("Bottom 10 Least Happy Countries Life Expectancy")
axes[1].set_xticklabels(xlabels, rotation = 45, ha = "right")
sns.barplot(x = bottom_10.country_name, y = bottom_10.healthy_life_expectancy, ax = axes[1])
axes[1].set_xlabel("Country Name")
axes[1].set_ylabel("Life Axpectancy")

plt.rcParams["figure.figsize"] = (15, 7)
sns.scatterplot(x = happiness_df.freedom_to_make_life_choices, y = happiness_df.happiness_score, hue = happiness_df.regional_indicator, s = 200)
plt.legend(loc = "upper left", fontsize = 12)
plt.title("Plot Between Freedom to Make Life Choices and Happiness Score")
plt.xlabel("Freedom to Make Life Choices")
plt.ylabel("Happines Score")

country = happiness_df.sort_values(by = "perceptions_of_corruption").head(10)
plt.rcParams["figure.figsize"] = (12, 6)
plt.title("Countries with Least Perception of Corruption")
plt.xlabel("Country", fontsize = 13)
plt.ylabel("Corruption Index", fontsize = 13)
plt.xticks(rotation = 30, ha = "right")
plt.bar(country.country_name, country.perceptions_of_corruption)

country = happiness_df.sort_values(by = "perceptions_of_corruption").tail(10)
plt.rcParams["figure.figsize"] = (12, 6)
plt.title("Countries with Most Perception of Corruption")
plt.xlabel("Country", fontsize = 13)
plt.ylabel("Corruption Index", fontsize = 13)
plt.xticks(rotation = 30, ha = "right")
plt.bar(country.country_name, country.perceptions_of_corruption)

#Corruption vs Happiness

plt.rcParams["figure.figsize"] = (15, 7)
sns.scatterplot(x = happiness_df.happiness_score, y = happiness_df.perceptions_of_corruption, hue = happiness_df.regional_indicator, s = 200)
plt.legend(loc = "lower left", fontsize = 14)
plt.title("Plot Between Corruption and Happiness Score")
plt.xlabel("Happiness Score")
plt.ylabel("Corruption")

