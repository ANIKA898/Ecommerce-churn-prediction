import streamlit as st
import pandas as pd
import pickle

# Load the saved model
with open('churn_model.pkl', 'rb') as f:
    model = pickle.load(f)

# App title
st.title("🛒 E-Commerce Customer Churn Predictor")
st.write("Enter customer details below to predict churn risk!")

# Input fields
tenure = st.slider("Tenure (months)", 0, 72, 12)
cashback = st.slider("Cashback Amount (₹)", 0, 500, 150)
warehouse = st.slider("Warehouse to Home Distance (km)", 0, 100, 15)
address = st.slider("Number of Addresses", 1, 10, 2)
days = st.slider("Days Since Last Order", 0, 60, 10)

# Predict button
if st.button("PREDICT CHURN RISK"):
    
    sample = pd.DataFrame([{
        'Tenure': tenure,
        'PreferredLoginDevice': 1,
        'CityTier': 2,
        'WarehouseToHome': warehouse,
        'PreferredPaymentMode': 3,
        'Gender': 1,
        'HourSpendOnApp': 3,
        'NumberOfDeviceRegistered': 3,
        'PreferedOrderCat': 2,
        'SatisfactionScore': 3,
        'MaritalStatus': 1,
        'NumberOfAddress': address,
        'Complain': 0,
        'OrderAmountHikeFromlastYear': 15,
        'CouponUsed': 2,
        'OrderCount': 3,
        'DaySinceLastOrder': days,
        'CashbackAmount': cashback
    }])

    probability = model.predict_proba(sample)[0][1]

    st.write("---")
    
    if probability >= 0.30:
        st.error(f"😰 HIGH CHURN RISK — {probability*100:.1f}% probability")
        st.write("**Recommendation:** Send retention offer immediately!")
        st.write("Consider cashback boost or free delivery coupon!")
    elif probability >= 0.15:
        st.warning(f"😐 MEDIUM CHURN RISK — {probability*100:.1f}% probability")
        st.write("**Recommendation:** Monitor closely!")
        st.write("Send engagement notification or small discount!")
    else:
        st.success(f"😊 LOW CHURN RISK — {probability*100:.1f}% probability")
        st.write("**Recommendation:** Customer is stable!")
        st.write("Maintain current engagement strategy!")
