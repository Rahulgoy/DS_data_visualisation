import pandas as pd
import plotly.express as px
import streamlit as st


st.set_page_config(page_title="Google Play Store Stats",
                    page_icon=":bar_chart:",
                    layout="wide")

data = pd.read_csv("googleplaystore.csv")
st.dataframe(df)
