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
data = data.dropna()

# Header
st.header("Google Play Store Data Visualization")


# 1. Metrices
categories = data['Category'].unique()
col01, col1, col2, col02= st.columns(4)
col1.metric("Total Apps", len(data))
col2.metric("Total Categories",len(categories))
# col3.metric("Humidity", "86%", "4%")


# 2. Show Dataset
agree = st.checkbox('See the dataset!')
if agree:
    st.dataframe(data)


#
fig1, ax1 = plt.subplots()
ax1.pie(data['Category'].value_counts(), labels=categories, autopct='%1.1f%%',
        shadow=True, startangle=90)
ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

# st.pyplot(fig1)

# 3. Category wise data distri
st.subheader("Category wise data distribution")
st.bar_chart(data['Category'].value_counts(), height=400)
# bar_fig = px.bar(data['Category'].value_counts())
# st.write(bar_fig)


center_col1,center_col2 = st.columns(2)
with center_col1:
    # 4. Content Rating
    content_categories = data['Content Rating'].unique()
    dataf = data['Content Rating'].value_counts()
    # st.write(data['Content Rating'].value_counts())
    st.subheader("Content Ratings")
    fig = px.pie(dataf, values="Content Rating", names=content_categories)
    fig.update_layout(margin=dict(l=1,r=1,b=1,t=1),paper_bgcolor="white", height=350, width=500, font_color="black")
    st.write(fig)
with center_col2:
    st.subheader("Rating wise App Count")
    group = data.groupby(['Rating']).count()
    # st.dataframe(group)
    st.line_chart(group['App'],use_container_width=False,width=500,height=350)


# 4.   Categorie wise rating
result = data.groupby(['Category']).mean()

st.subheader("Category wise average rating")
st.bar_chart(result['Rating'],height=350,use_container_width=True)
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


# Top 10 by categories with highest ratings

cat = st.selectbox("Select the categorie",options=categories)
# st.write(datafra)
# cat_fig = px.bar(datafra,x="Rating",y="App",orientation='h')
# cat_fig.update_layout(margin=dict(l=1,r=2,b=1,t=2),height=500, width=700)

# st.write(cat_fig)


cat_col1,cat_col2 = st.columns(2)

with cat_col1:
    st.subheader("Top 10 highest rated Apps by Categorie")
    datafra = data.query("Category == @cat")
    datafra = datafra.sort_values(by=['Rating'], ascending=False)
    datafra = datafra.iloc[:10]
    datafra = datafra[['App','Rating']]
    st.table(datafra)
with cat_col2:
    st.subheader("Top 10 Free Apps by Categorie")
    datafra = data.query("Category == @cat and Type == 'Free'")
    datafra = datafra.sort_values(by=['Rating'], ascending=False)
    datafra = datafra.iloc[:10]
    datafra = datafra[['App','Rating']]
    st.table(datafra)


