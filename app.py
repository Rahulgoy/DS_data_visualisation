import pandas as pd
import plotly.express as px
import streamlit as st
import seaborn as sns
import matplotlib.pyplot as plt


st.set_page_config(page_title="Google Play Store Stats",
                    page_icon=":bar_chart:",
                    layout="wide")
st.markdown(""" <style>
#MainMenu {visibility: hidden;}
footer {visibility: hidden;}
</style> """, unsafe_allow_html=True)

data = pd.read_csv("googleplaystore.csv")


# Header
st.header("Google Play Store Data Visualization")


# Metrices
categories = data['Category'].unique()
col01, col1, col2, col02= st.columns(4)
col1.metric("Total Apps", len(data))
col2.metric("Total Categories",len(categories))
# col3.metric("Humidity", "86%", "4%")


agree = st.checkbox('See the dataset!')
if agree:
    st.dataframe(data)


labels = 'Frogs', 'Hogs', 'Dogs', 'Logs'
sizes = [15, 30, 45, 10]
# explode = (0, 0.1, 0, 0)  # only "explode" the 2nd slice (i.e. 'Hogs')

fig1, ax1 = plt.subplots()
ax1.pie(data['Category'].value_counts(), labels=categories, autopct='%1.1f%%',
        shadow=True, startangle=90)
ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

# st.pyplot(fig1)
st.bar_chart(data['Category'].value_counts(), height=400)


# To implement correlation 
# fig, ax = plt.subplots()
# sns.heatmap(data.corr(), ax=ax)
# st.write(fig)



st.sidebar.header("Please Filter Here:")

# app = st.sidebar.multiselect(
#     "Select the apps",
#     options=data["App"].unique
# )
st.sidebar.write("Made with ❤ by Rahul Goyal")
