import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px

st.set_page_config(
    page_title="DS4420 Final Project",
    page_icon="🚀",
    layout="wide"
)

st.sidebar.title("Page Navigator")
page = st.sidebar.radio("Go to", ["Home Page", "Interactive Visualization"])

if page == "Home Page":
    st.title("DS4420 Final Project")
    st.markdown("---")
        
    st.header("Project Overview")
    st.write("""
    In this project, we set out to answer the question if movies runtimes have any impact on their rating, since the rise of
    short form content. Using a dataset of movies released from 2012 to 2025, we analyzed the relationship between movie runtimes and their corresponding IMDb ratings using two models: MLP Neural Network and Bayesian Regression. 
    """)
        

elif page == "Interactive Visualization":
    st.title("Interactive Visualization")
    st.markdown("---")
    