## UNDERSTANDING THE PROBLEM 
-----------------------------------------------------

1. What is Fraud ?
- An unauthorized transaction such as an illegal purchase or money transfer   
  which is not performed by the actual account holder.

2. What is Fraud Detection in banking ? 
- Fraud detection in banking is using a set of tools and technologies to 
  reduce financial fraud risks to institutions and businesses by ensuring secure account access and monitoring user transactions for suspicious activities.

3. Types of Frauds 
- Transaction Fraud: Unauthorized card usage 
- Identification Threft: Fake KYC/ Stole Credentials
- Account Takeover Fraud: Hackers got the access  
- Credit/Loan Fraud

4. Why do banks care?
Because fraud causes:
- Financial loss
- Customer trust issues
- Regulatory issue

5. Factors might indicate fraud - 
- Very large transaction amount
- Many transactions in short time
- Foreign location
- New device
- Midnight transactions
- Sudden spending pattern change

6. Fraud Detection Challenges for Banks
- Banks need to monitor and analyze millions of transactions daily to identify 
  instances of fraudulent activities, anomalies, and loopholes each month to prevent fraudulent risks. Manually reviewing each transaction for potential fraud and anomalies gets challenging.
- According to a **global financial fraud report**, digital payment fraud
  schemes accounted for a total of $485.6 billion in projected losses worldwide.
- Credential theft is one of the most critical banking fraud challenges. 
  Fraudsters steal users' credentials, such as banking details and login information.
- Improving a bank’s security and cybersecurity attempts often impacts 
  customer experience, resulting in loss of customers or another negative impact.

7. Approches for this problem 
There are two types of approches people follow -  

(a) **Rule Based Approch** 
Setting up rules like - Block transaction > 1 million at midnight  

(b) **ML Based Approch** 
Model finds and learns the pattern automatically 

(C) **Hybrid Approch** 
Include both Rule Based Approch + ML Based Approch 


## APPROACH FOR THIS PROBLEM 
-----------------------------------------------------
1. This is a binary classification problem 

2. This is an imbalanced class problem 
- Dont considered Accuracy 
- Focus on Presion and Recall 
- Accuracy gives equal importance to both classes
- But in Imbalanced data, one class is huge so majority class dominate other class.
- Main focus will be on - Recall

3. Here for this project we will use - ML Based Approch 
- Machine Learning play a crucial role in detecting fraud in the banking and 
  financial sector. These technologies significantly streamline data analysis, making it easier to analyze large datasets, detect anomalies, and make quick decisions.

4. Too many FP can heart customers experience and too many FN can heart the 
   company financially. 

5. False Negatives and False Positives have different costs.

--------------------------------------------------------------

#### Life Cycle of ML Based Project 

1. Understanding the problem 
2. Data Collection 
3. Data Understanding 
4. EDA, Data Cleaning, Preprocessing 
5. Model Training and Evaluation



<!-- Notebook Development
EDA
Data cleaning
Feature engineering
Baseline model
Model comparison
Final model selection -->