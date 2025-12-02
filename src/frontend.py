import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots


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

    posterior_df = pd.read_csv('posterior_mean_predictions.csv')
    observed_df = pd.read_csv('observed_ratings.csv')

    
    posterior_col = posterior_df.columns[0]
    observed_col = observed_df.columns[0]
    opacity = 0.7
    
    st.sidebar.header("Visualization Controls")
    
    posterior_color = st.sidebar.color_picker("Posterior Color", "#636EFA")
    observed_color = st.sidebar.color_picker("Observed Color", "#EF553B")
    
    layout_option = st.sidebar.radio("Layout", ["Side by Side", "Overlapping"])
        
    if layout_option == "Side by Side":
        fig = make_subplots(
            rows=1, cols=2,
            subplot_titles=("Posterior Histogram", "Observed Ratings Histogram"),
            horizontal_spacing=0.1
        )
        
        posterior_counts, posterior_bins = np.histogram(
            posterior_df[posterior_col], 
            bins=50, 
            range=(5.75, 6.05)
        )
        posterior_bin_centers = (posterior_bins[:-1] + posterior_bins[1:]) / 2
        
        fig.add_trace(
            go.Bar(
                x=posterior_bin_centers,
                y=posterior_counts,
                name="Posterior",
                marker_color=posterior_color,
                marker_line_color='black',
                marker_line_width=0.5,
                opacity=opacity,
                width=(posterior_bins[1] - posterior_bins[0]) * 0.9
            ),
            row=1, col=1
        )
        
        observed_counts, observed_bins = np.histogram(
            observed_df[observed_col], 
            bins=30,
            range=(observed_df[observed_col].min(), observed_df[observed_col].max())
        )
        observed_bin_centers = (observed_bins[:-1] + observed_bins[1:]) / 2
        
        fig.add_trace(
            go.Bar(
                x=observed_bin_centers,
                y=observed_counts,
                name="Observed",
                marker_color=observed_color,
                marker_line_color='black',
                marker_line_width=0.5,
                opacity=opacity,
                width=(observed_bins[1] - observed_bins[0]) * 0.9
            ),
            row=1, col=2
        )
        
        fig.update_xaxes(title_text="Rating", row=1, col=1)
        fig.update_xaxes(title_text="Rating", row=1, col=2)
        fig.update_yaxes(title_text="Frequency", row=1, col=1)
        fig.update_yaxes(title_text="Frequency", row=1, col=2)
        
    else:
        fig = go.Figure()
        
        posterior_counts, posterior_bins = np.histogram(
            posterior_df[posterior_col], 
            bins=15, 
            range=(5.75, 6.05)
        )
        posterior_bin_centers = (posterior_bins[:-1] + posterior_bins[1:]) / 2
        
        fig.add_trace(
            go.Bar(
                x=posterior_bin_centers,
                y=posterior_counts,
                name="Posterior",
                marker_color=posterior_color,
                marker_line_color='black',
                marker_line_width=0.5,
                opacity=opacity,
                width=(posterior_bins[1] - posterior_bins[0]) * 0.9
            )
        )
        
        observed_counts, observed_bins = np.histogram(
            observed_df[observed_col], 
            bins=50,
            range=(observed_df[observed_col].min(), observed_df[observed_col].max())
        )
        observed_bin_centers = (observed_bins[:-1] + observed_bins[1:]) / 2
        
        fig.add_trace(
            go.Bar(
                x=observed_bin_centers,
                y=observed_counts,
                name="Observed",
                marker_color=observed_color,
                marker_line_color='black',
                marker_line_width=0.5,
                opacity=opacity,
                width=(observed_bins[1] - observed_bins[0]) * 0.9
            )
        )
        
        fig.update_layout(barmode='overlay')
        fig.update_xaxes(title_text="Rating")
        fig.update_yaxes(title_text="Frequency")
    
    fig.update_layout(
        height=600,
        showlegend=True,
        hovermode='x unified'
    )
    
    st.plotly_chart(fig, use_container_width=True)