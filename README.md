# Ecommerce-churn-prediction
AI-powered e-commerce customer churn  prediction web app built with Python,  Random Forest and Streamlit


### Overview  
This project predicts whether a customer will churn or not using machine learning. It analyzes customer behaviour like app usage, order patterns, and engagement to identify high-risk customers.

### Problem Statement  
Customer churn is a major issue for ecommerce companies. This project helps identify customers who are likely to leave so that businesses can take preventive actions.

### Dataset  
- Ecommerce customer dataset (https://www.kaggle.com/datasets/ankitverma2010/ecommerce-customer-churn-analysis-and-prediction)  
- Sheet used: E Comm  
- Features include:  
  - Tenure  
  - Cashback Amount  
  - Warehouse distance  
  - Order behavior  
  - Preferred login device  
  - Payment mode  


### Tools and Technologies  
- Python  
- Pandas and NumPy  
- Matplotlib and Seaborn  
- Scikit-learn  


### Project Workflow  
1. Data Loading  
2. Data Cleaning (handling missing values using median)  
3. Encoding categorical variables  
4. Exploratory Data Analysis  
5. Model Building using Random Forest  
6. Model Evaluation  
7. Feature Importance Analysis  


### Model Used  
- Random Forest Classifier  


### Model Evaluation  
- Model Accuracy: 98%+  
- Confusion Matrix used for performance evaluation  
- Classification Report generated  


### Key Insights  
- Customer tenure and engagement significantly impact churn  
- Purchase behavior patterns help identify high-risk customers  
- Feature importance highlights key drivers of churn  


### Churn Prediction System  
- Built a function to take customer inputs and predict churn  
- Helps classify customers into risk categories  


### Model Saving  
- Model saved as churn_model.pkl using pickle  
- Can be reused without retraining  


### How to Run  
1. Upload the dataset (Excel file)  
2. Run the notebook or Python file  
3. Use prediction function to test new data  


### Screenshots  

![Screenshot1](churn%20prediction%20screenshots/Screenshot_15-3-2026_185616_localhost.jpeg)  
![Screenshot2](churn%20prediction%20screenshots/Screenshot_15-3-2026_185651_localhost.jpeg)  
![Screenshot3](churn%20prediction%20screenshots/Screenshot_15-3-2026_185658_localhost.jpeg)  
![Screenshot4](churn%20prediction%20screenshots/Screenshot_15-3-2026_18565_localhost.jpeg)  

### Author  
ANIKA ATTRI
