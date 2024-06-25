## SMS Spam Classifier

### Objective:
The primary objective of the Email Spam Classifier project is to develop a machine learning model capable of automatically classifying emails into two categories: spam and non-spam (ham). The classifier is trained on a labeled dataset containing examples of both spam and non-spam emails.

### Technical skill:

1. Python
2. pandas
3. Machine learning algorithms
4. NLP
5. Streamlit
6. Data manipulation

### Workflow Overview:
1. Data collection: Collected the data from Kaggle and also feeded the real time data.
2. Data pre-process: As the raw data cant be directly used for model because of data quality issue. I preprocessed the raw data to enhance the quality of data which increases the reliability on the model, accuracy of the prediction, consistenancy and decision making ability.
   > Dealing with Duplicate rows and Null values.
   > Case normalization.
   > Text cleaning.
   > Tokenization.
   > Stemming    
3. EDA: performed Exploratory data analysis to observe the data and find the insights for example in spam messages what are all most frequently words are used.
4. Feature creation: Created new feature which helped to increase the model's accuracy.
5. Model Training: First of all created input data by using text vectorization(TFIDF). then feed the data into diferent models like Naive bayes, Logistic regression, DecisionTreeClassifier, KNeighborsClassifier, RandomForestClassifier,AdaBoostClassifier,BaggingClassifier,ExtraTreesClassifier,GradientBoostingClassifier and XgbClassifier.
fit the model and calculated accuracy and precision of each model. then selected the model with highest precision and accuracy.
6. Model improvement: applied some improvement techniques to increase the models precision and accuracy like hyperparameter tuning, voting classifier, feature selection etc.
7. Model API: Created a web page so that any user can access and play with the product.


![Uber_analysis_dashboard](https://github.com/rockraj999/SMS-spam-classifier/blob/main/SpamOrNotSpamD.png)
 
   
  














