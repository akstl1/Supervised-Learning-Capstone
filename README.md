# Supervised-Learning-Capstone
Udemy Course Supervised Learning Capstone Project

This capstone project was done as part of the 2021 Python Machine Learning for Data Science course on Udemy.

The project involves loading in telecom customer data, with a goal of using it to predict customer churn.

To accomplish this task, I performed an initial exploratory data analysis by plotting variables like monthly charges, 
total charges and contract type against each other. When doing this, I discovered that there appeared to be a connection
between contract type and churn.

Upon further exploration, I discovered that contract type and customer tenure appeared to correlate with customer churn,
and created several customer tenure buckets to capture this in the data set.

After the initial analysis, I performed a train test split on the data and ran random forest, logistic regression, and KNN
models to determine which method could more accurately predict churn. In the end, the random forest and logistic regression
models both performed similarly, accurately classifying ~80% of the test data.
