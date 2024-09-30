import streamlit as st
from streamlit_option_menu import option_menu
import pickle
import pandas as pd
import statsmodels as sm
import datetime
from datetime import date,timedelta
import numpy as np

def login():
    st.title("Login")
    username=st.text_input("Username")
    password=st.text_input("Password",type="password")
    if st.button("Login"):
        if username=="Oshim" and password=="123401234":
            st.session_state.logged_in=True
            st.success("Login Successful")
        else:
            st.error("Invalid User Name or Password")

def dashboard():
    with st.sidebar:
        selected = option_menu(
            menu_title="Menu",
            options=["Home", "About", "Contact","Logout"],
            icons=["house-heart-fill", "calendar2-heart-fill", "envelope-heart-fill","lock-fill"],
            menu_icon="three-dots",
            default_index=0,
        )

    if selected == "Home":
        st.write("### :violet[Welcome Md.Oshim Akram !]")
        option = st.sidebar.selectbox("Select Operation",
                                      ("Sesonal Sales Pradiction", "Sales Pradiction", "New Material Entry", "Receivd", "Issued",
                                       "Stock Report"))
        if option == "Sesonal Sales Pradiction":
            st.title("Seasonal Sales Prediction")
            loaded_model = pickle.load(open('D:/Monthly_Sales_Prediction\seasonalpklt5.sav', 'rb'))

            Start_Date = st.date_input("Start Date", date(2025, 1, 1))
            End_Date = st.date_input("End Date", date(2025, 5, 1))
            button = st.button("Predict")

            if button:
                prediction = loaded_model.predict(Start_Date, End_Date)
                st.write("Seasonal Sales Forecust :", prediction)
        if option == "Sales Pradiction":
            st.title("Sales Prediction page under construction")

        if option == "New Material Entry":
            st.title("New Material Entry page under construction")

        if option == "Received":
            st.title("Received page under construction")

        if option == "Issued":
            st.title("Issued page under construction")

        if option == "Stock":
            st.title("Stock page under construction")


    if selected == "About":
        st.write("### :violet[About myself]")
        st.write("### :violet[I am Md. Oshim Akram. I have completed my Graduation. Now I am working a group of company as In-Charge of Inventory & warehouse. About 13 years experienced along five comppanies in this sector.]")

    if selected == "Contact":
        st.title(f"Welcome to the {selected} page")

    if selected=="Logout":
        st.button("### :red[Logout]")
        st.session_state.logged_in = False
        st.rerun()
if "logged_in" not in st.session_state:
    st.session_state.logged_in=False
if st.session_state.logged_in:
        dashboard()
else:
    login()

