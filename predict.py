import streamlit as st
import pickle 
import pandas as pd
import numpy as np
import sklearn
import plotly.express as px
import xgboost

df_eda=pd.read_csv("data.csv")
list1=df_eda["location"].unique().tolist()
list2=df_eda["rest_type"].unique().tolist()
list3=df_eda["cuisines"].unique().tolist()
list4=df_eda["listed_in(type)"].unique().tolist()
list5=df_eda["listed_in(city)"].unique().tolist()
model=pickle.load(open("model", 'rb')) #load model
st.header("You will be restaurant and you want to know if your restaurant will be succesfull or not. ")
st.write("Frist , entry some inforamtion for your restaurant ")
online_order=st.selectbox("The customer can book an order online or not :",['Yes', 'No'])
book_table=st.selectbox("The customer can book a table or not :",['Yes', 'No'])
phone=st.selectbox("The resturant have number or not :",['have phone', 'not have phone'])
location=st.selectbox("Location of a restaurant :",list1)
rest_type=st.selectbox("The type of service provided by the restaurant :",list2)
cuisines=st.selectbox("The type of cuisines provided by the restaurant :",list3)
approx_cost=st.number_input("approx cost for two people :")
menu_item=st.selectbox("The resturant have menu or not :",['have menu', 'not have menu'])
listed_in_type=st.selectbox("The type of service provided by the restaurant :",list4)
listed_in_city=st.selectbox("City of a resturant :",list5)
data={'online_order': online_order,
        'book_table': book_table,
        'phone':phone,
        'location':location,
        'rest_type':rest_type,
        'cuisines':cuisines,
        'approx_cost(for two people)':approx_cost,
        'menu_item':menu_item,
        'listed_in(type)':listed_in_type,
        'listed_in(city)':listed_in_city}
df_test=pd.DataFrame(data,index=[0])
#function predict
def prediction(df):
    value_predict=model.predict(df)[0]
    if value_predict ==1:
        return "This restaurant will be successful"
    else:
        return "This restaurant will be not successful"

#show the result
btn=st.button("Predict")
if btn:
    st.write(prediction(df_test))