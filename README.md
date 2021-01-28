# Personal Loan Prediction
![Kaggle](https://img.shields.io/badge/Dataset-Kaggle-blue.svg) ![Python 3.7](https://img.shields.io/badge/Python-3.7-blueviolet.svg) ![Seaborn](https://img.shields.io/badge/Library-Seaborn-success.svg) ![Scikit-learn](https://img.shields.io/badge/Library-Scikit_Learn-orange.svg)

This project is about **classification** of personal loans using a vast choices of **algorithms** for **Supervised Machine Learning**.
The dataset we use contains details of **346 customers** whose loan are already **paid off** or **defaulted**. It includes following fields:

| **Field** | **Description** |
|-------|-------------|
|**Loan status**|*Whether a loan is paid off on in collection*|
|**Principal**|*Basic principal loan amount*|
|**Terms**|*Origination terms which can be weekly (7 days), biweekly, and monthly payoff schedule*|
|**Effective date**|*When the loan got originated and took effects*|
|**Due date**|*Since it’s one-time payoff schedule, each loan has one single due date*|
|**Age**|*Age of applicant*|
|**Education**|*Education of applicant*|
|**Gender**|*The gender of applicant*|

Working on this dataset, we proceed to all the **preprocessing steps**, **feature engineering** & **model selection** to choose the best classifier.

The objective is then to build an **end-to-end** Personal Loan Simulator for **new clients** to predict if future loans will be **paid off**, or **defaulted**.
The outcome allows us to decide whether or not the loan will be granted to the client!

The **full deployed** model is available here on **Heroku** : https://personal-loan-simulator.herokuapp.com/

And here is a **glimpse** of the Web App:

<img src="personal-loan.gif" width="700" height="552"/>