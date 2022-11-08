# Heart Disease Analysis

Heart attack analysis with an overview of state heart disease mortality rates in connection with concentration of fast food restaurants.

## Project Overview:

The purpose of this project was to explore an overall analysis of heart disease in America and the potential implications of availability of unhealthy (meaning fast food) options on the disease and death rates. 

A presentation of our project can be found on the following [Google Slides](https://docs.google.com/presentation/d/1cJC_sjUArMiMfbOxWKrwwbX-4j2tHW_1R3M52RUsq64/edit?usp=sharing)

## Process:

### Data Collection:

We collected datasets from Kaggle and the CDC website. Links to all can be found at the bottom of this document.
From the CDC, we procured heart disease rates from all states for the years 2005 and 2014-2020 as well as the number of deaths per 100,000 total population.

Two other datasets came from Kaggle:
The Heart Failure Prediction Dataset lists health statistics of individual patients and whether or not they had a heart attack. This data will be used to predict heart attacks.
The dataset of Fast Food Restaurants in the United States is a list of over nine thousand fast food restaurants throughout America and their locations. This will be used to determine if the availability of unhealthy food plays into the rate of heart disease in each state.

### Machine Learning:

The data will be imported into a SQL database and then used to perform a machine learning model that will predict the likelihood that a person will have a heart attack based on their personal health stats and data.

### Analysis, Presentation, and Visualization:

The overall analysis will be written into a Google Slide presentation viewable [here](https://docs.google.com/presentation/d/1cJC_sjUArMiMfbOxWKrwwbX-4j2tHW_1R3M52RUsq64/edit?usp=sharing), as well as visualized on a webpage.

## Technology:

<img width="772" alt="Screen Shot 2022-11-07 at 8 06 15 PM" src="https://user-images.githubusercontent.com/106691255/200474283-66d25dc0-7475-49b3-9975-9777a702662d.png">

Pandas Python library was employed through jupyter notebook to clean data and perform machine learning.

pgAdmin 4 was used to build a postgres SQL database.

Visualizations were created using Tableau.

HTMLand Flask were used to create an interactive website to deploy the information to the public, which can be viewed [here]().

## Database

Aaron created one database for the purchase of Machine Learning. 

His database had 3 tables from a dataset of combined heart attack data from 900 different patients. The database was created in PostgresSQL (pgAdmin 4) and then linked back into jupyter notebook for Machine Learning. 

![pgAdminHeart_Attack](https://user-images.githubusercontent.com/106691255/200472664-c19cab5e-1604-4d15-8816-d0485a524efe.png)

Maggie created a second database with the purpose of creating files for each year of heart disease data for use in Tableau visualizations.

Her database had 9 tables created from a dataset from the CDC containing heart disease rates by state from the years 2005 and 2014-2020. Maggie used SQL to separate this file into individual years for visualization purposes.

<img width="631" alt="Screen Shot 2022-11-07 at 7 54 35 PM" src="https://user-images.githubusercontent.com/106691255/200472701-1f2221e4-f57f-4c12-bfa8-3c1b0c13cdeb.png">

## Machine Learning Model

View the Machine Learning Model [here](https://github.com/stewamag/Heart_Disease/blob/main/Heart_Pandas_Pickle.ipynb).

In this machine learning analysis, we look to explore the relationship of various demographic and health variables with heart disease to see if we can predict whether someone is likely to have a cardiac event or not.

Machine Learning Goal: To use the data to predict whether a user will suffer from a heart attack with 80% accuracy.

Implications: By using key variables to predict whether or not a subject is likely to have a heart event, the individual can take steps to change their lifestyle to prevent it before it happens.

Data Variables Explored:
Age
Sex
Chest Pain Type
Resting Blood Pressure
Cholesterol
Fasting Blood Pressure
Resting ECG
Max Heart Rate
Exercise Induced Angina
Previous Peak
Heart Rate Slope

## Preliminary Data Preprocessing

View Code for the Data Preprocessing [here](https://github.com/stewamag/Heart_Disease/blob/main/heart_disease_clean_data.ipynb).

Before being able to load the data into PostgresSQL, it needed to be reformatted. Data was cleaned in jupyter notebook using Python Pandas. Columns were renamed for uniformity and unnecessary columns were dropped.

CSV files were then connected to the PostgresSQL database.

SQL tables were created and queries were employed to create separate files for each year of heart disease.

## Preliminary Feature Engineering, Feature Selection, and Decision-Making Process

View Code for the Feature Engineering [here](https://github.com/stewamag/Heart_Disease/blob/main/Heart_Pandas_Pickle.ipynb).

**Target**: Whether or not someone will have a heart attack (0 or 1)

**Features**: Demographic and health information: age, sex, chest pain type, resting blood pressure, etc.

**Feature Engineering**: 
<img width="876" alt="Screen Shot 2022-11-07 at 8 04 34 PM" src="https://user-images.githubusercontent.com/106691255/200472877-28a32f4e-2487-4e27-944e-0145765a651d.png">

## Training and Testing Sets

The machine learning model split the data into two sets: training and testing. The training set was used to create the model and the testing set to check its performance. The purpose of saving some of the data for the testing set is to ensure that the model is working properly when introduced to unknown data. The SciKit library was used to split the data into the testing and training sets, then run the model on both.

<img width="722" alt="Screen Shot 2022-11-07 at 7 38 22 PM" src="https://user-images.githubusercontent.com/106691255/200473026-57b797ef-d78a-45df-a9e7-8257acb063ab.png">

<img width="185" alt="Screen Shot 2022-11-07 at 7 38 32 PM" src="https://user-images.githubusercontent.com/106691255/200473000-d72217ae-0fd7-4c22-aa91-dbdd01d7fdf4.png">

## Model Choice: Limitations and Benefits

We used a supervised machine learning model because we were dealing with labeled datasets with an expected binary outcome.

**Benefits of the Model**: Linear regression performs exceptionally well for linearly separable data. We got a higher accuracy rate and were only looking for a yes or no result. Logistic regression just made the most sense. It was easier to implement, interpret and more efficient to train

**Drawbacks of the Model**: The only drawback was that when dealing with non-numerical values, it had to be processed differently. Our data does not give early detection. It would not be preventative for daily life choices. 

## Model Results:

<img width="304" alt="Screen Shot 2022-11-07 at 7 39 35 PM" src="https://user-images.githubusercontent.com/106691255/200472984-26fcf671-aaad-4636-a388-ed287a2fc27e.png">

<img width="436" alt="Screen Shot 2022-11-07 at 7 39 44 PM" src="https://user-images.githubusercontent.com/106691255/200472974-fe5f44ce-7e7e-427c-b014-0543ec9ae25e.png">

**Accuracy**: The model received an accuracy score of 0.83, which means that 83% of the testing data was accurately predicted by the model. 

**Precision**: The positive predictive value (PPV), or precision, is how likely that a predicted positive is a true positive. This number can be found by dividing the number of true positives by the total number of positives (true and false). Our precision for this model was 0.84.

**Sensitivity/Recall**: The sensitivity, also know as recall, measures how many true positives were actually predicted as such. The sensitivity of our model was 0.84, which means that the model is 84% likely to accurately guess whether or not someone will have a heart attack.

**F1 Score**: Tests that are highly sensitive are great because they are likely to do a good job at detecting true positives. They also have the potential, however, to detect false positives. Precise models are also good because it shows that the bulk of the positive results were indeed true positives. However, it is possible with a precise model that true positives might not always be detected (and be tagged as a false negative instead). The F1 Score is like a balancing act between the two. An imbalanced model would yield a low F1 score. Our model's F1 was 0.84.

## Machine Learning Results:

<img width="653" alt="Screen Shot 2022-11-07 at 7 40 05 PM" src="https://user-images.githubusercontent.com/106691255/200472938-56479b72-93dd-48fa-a01f-3a54f37fe9b4.png">

## Visualizations:

We incorporated our Tableau visualizations into our [Google Slides](https://docs.google.com/presentation/d/1cJC_sjUArMiMfbOxWKrwwbX-4j2tHW_1R3M52RUsq64/edit?usp=sharing) as well as our [webpage]().

## Description of the data exploration phase of the project:

Maggie cleaned the datasets using pandas (in jupyter notebook) and exported them to clean versions of the .csv files.

Machine learning was difficult with the original 'heart attack' dataset because there were not enough data points for analyzing (only about 300). So, Aaron found a new data set that was very similar and has over 900 data points. We are hopeful that machine learning will go better with this data.

## Description of the analysis phase of the project:

Maggie realized that you cannot merge/join tables in SQL unless the column being joined has only unique values in it. The two tables that she was attempting to join could only be potentially be joined by the "US_State" column, but since the states occurred multiple times within each dataset, it was impossible to join them.

She was, however, able to use SQL to create separate datasets for each year with heart disease data for that year.

## Resources:

[Heart Failure Prediction Dataset](https://www.kaggle.com/datasets/fedesoriano/heart-failure-prediction)

[Heart Disease Mortality by State](https://www.cdc.gov/nchs/pressroom/sosmap/heart_disease_mortality/heart_disease.htm)

[Fast Food Restaurants in the United States](https://www.kaggle.com/datasets/thedevastator/fast-food-restaurants-in-the-united-states)

## Team Members:

[Aaron McCarty](https://github.com/AmccartyA)

[Maggie Stewart](https://github.com/stewamag)
