# Heart Disease Analysis

Heart attack analysis with an overview of state heart disease mortality rates in connection with concentration of fast food restaurants.

## Project Overview:

The purpose of this project was to explore an overall analysis of heart disease in America and the potential implications of availability of unhealthy (meaning fast food) options on the disease and death rates. 

A presentation of our project can be found on the following [Google Slides](https://docs.google.com/presentation/d/1cJC_sjUArMiMfbOxWKrwwbX-4j2tHW_1R3M52RUsq64/edit?usp=sharing)

## Process:

Data Collection:

We collected datasets from Kaggle and the CDC website. Links to all can be found at the bottom of this document.
	* From the CDC, we procured heart disease rates from all states for the years 2005 and 2014-2020 as well as the number of deaths per 100,000 total population.

Two other datasets came from Kaggle:
	* The Heart Failure Prediction Dataset lists health statistics of individual patients and whether or not they had a heart attack. This data will be used to predict heart attacks.
	* The dataset of Fast Food Restaurants in the United States is a list of over nine thousand fast food restaurants throughout America and their locations. This will be used to determine if the availability of unhealthy food plays into the rate of heart disease in each state.

## Machine Learning:

The data will be imported into a SQL database and then used to perform a machine learning model that will predict the likelihood that a person will have a heart attack based on their personal health stats and data.

## Analysis, Presentation, and Visualization:

    The overall analysis will be written into a Google Slide presentation viewable [here](https://docs.google.com/presentation/d/1cJC_sjUArMiMfbOxWKrwwbX-4j2tHW_1R3M52RUsq64/edit?usp=sharing), as well as visualized on a webpage.

## Questions to Answer with the Data: 

	- Chance of having a heart attack based off your health stats from last physical
	- Does the availibity of fast food correlate to the rate of heart disease mortality?

## Description Communication Protocols: 

Slack, email, phone

## Machine Learning: 

Binary classification model - Will you have a heart attack (yes or no)?

## SQL Database Plan:
<img width="922" alt="QuickDBD" src="https://user-images.githubusercontent.com/106691255/199051875-cfa7d25b-8596-4991-9a9c-03400476a907.png">

## Description of the data exploration phase of the project:

	- Maggie cleaned the datasets using pandas (in jupyter notebook) and exported them to clean versions of the csv files.
	- Machine learning was difficult with the original 'heart attack' dataset because there were not enough data points for analyzing (only about 300). So, Aaron found a new data set that was very similar and has over 900 data points. We are hopeful that machine learning will go better with this data.
## Description of the analysis phase of the project:

	- Maggie realized that you cannot merge/join tables in SQL unless the column being joined has only unique values in it. The two tables that she was attempting to join could only be potentially be joined by the "US_State" column, but since the states occurred multiple times within each dataset, it was impossible to join them.
	- She was, however, able to use SQL to create separate datasets for each year with heart disease data for that year.

## Resources:

	* [Heart Failure Prediction Dataset](https://www.kaggle.com/datasets/fedesoriano/heart-failure-prediction)
	* [Heart Disease Mortality by State](https://www.cdc.gov/nchs/pressroom/sosmap/heart_disease_mortality/heart_disease.htm)
	* [Fast Food Restaurants in the United States](https://www.kaggle.com/datasets/thedevastator/fast-food-restaurants-in-the-united-states)

## Team Members:

	* [Aaron McCarty](https://github.com/AmccartyA)
	* [Maggie Stewart](https://github.com/stewamag)