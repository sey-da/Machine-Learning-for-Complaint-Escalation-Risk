# Machine-Learning-for-Complaint-Escalation-Risk
Predicting high risk financial complaints to improve decision making and complaint management.

# Financial Complaint Escalation Prediction

This project develops a machine learning pipeline to predict whether a financial complaint is likely to escalate into a disputed case. The objective is to support early identification of high risk complaints in products such as credit cards, consumer loans, mortgages, and other financial services.

## Project Overview

Financial institutions receive large volumes of customer complaints across multiple channels. Some complaints escalate into disputes, creating operational, regulatory, and reputational risks. This project builds a predictive model to classify complaints as disputed or non disputed based on historical complaint data.

The workflow includes:
- exploratory data analysis
- feature engineering
- preprocessing for numerical and categorical variables
- model training and evaluation
- model selection based on F1 score
- pipeline serialization for deployment readiness

## Business Objective

The goal is to help financial institutions identify escalation prone complaints earlier, so they can:
- prioritize high risk cases
- improve resolution workflows
- reduce false negatives
- support proactive complaint management

## Dataset

The project uses complaint level training data containing information such as:
- product type
- submission channel
- customer complaint attributes
- dispute outcome

The target variable is:

- **0** = non disputed complaint
- **1** = disputed complaint

## Exploratory Data Analysis

The EDA highlights several important findings:
- complaints submitted through digital channels show higher escalation rates
- the target variable is strongly imbalanced
- certain financial products such as virtual currency, mortgages, consumer loans, and credit cards show higher dispute rates

These findings provide both business insight and justification for the modeling approach.

## Machine Learning Approach

This project is framed as a **binary classification** problem.

### Models used
- **Logistic Regression**
- **Random Forest**

### Preprocessing pipeline
- missing value imputation
- scaling for numerical variables
- one hot encoding for categorical variables
- custom feature engineering integrated through a pipeline

### Model selection
The main evaluation metric is **F1 score**, since the dataset is imbalanced and the business problem requires balancing recall and precision.

## Results

Both models achieved similar performance, with Random Forest slightly outperforming Logistic Regression on the F1 metric.

Key evaluation metrics considered:
- Accuracy
- F1 Score
- Recall
- ROC AUC
- Confusion Matrix
- Classification Report

The final selected model was:
- **Random Forest**

## Deployment Readiness

The final trained pipeline was serialized and saved as a `.pkl` file to ensure reproducibility and deployment readiness.

This serialized artifact includes:
- feature engineering
- preprocessing
- trained model

The pipeline was also tested on an external dataset to confirm that it generates valid predictions in a production style setting.

## Project Structure

```bash
.
├── complaints_training.csv
├── complaints_modeltesting100.csv
├── feature_engineering.py
├── 70549_Complaints_Notebook.ipynb
├── 70549_Pipeline.pkl
└── README.md
