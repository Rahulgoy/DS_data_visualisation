import pandas as pd
import plotly.express as px
import streamlit as st
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.graph_objects as go

# --------------Page Configurations---------------------
st.set_page_config(page_title="Google Play Store Stats",
                    page_icon=":bar_chart:",
                    layout="wide")
st.markdown(""" <style>
#MainMenu {visibility: hidden;}
footer {visibility: hidden;}
</style> """, unsafe_allow_html=True)


#-----------------Drop Null Values--------------------------
data = pd.read_csv("googleplaystore.csv")
data = data.dropna()

# ----------------Header--------------------------------
st.header("Google Play Store Data Visualization")


# ----------------1. Metrices---------------------------
##To show overall number of apps and categories

categories = data['Category'].unique()
col01, col1, col2, col02= st.columns(4)
col1.metric("Total Apps", len(data))
col2.metric("Total Categories",len(categories))


# ----------------2. Show Dataset-----------------------
agree = st.checkbox('See the dataset!')
if agree:
    st.dataframe(data)


#---------------- 3. Category wise data distribution---------------
st.subheader("Category wise data distribution")

# Counting the individual values of each category and creating a bar chart
st.bar_chart(data['Category'].value_counts(), height=400)           


#------------------Center Content--------------------------------
center_col1,center_col2 = st.columns(2)
with center_col1:
    #----------------4. Rating wise App Count-----------------
    
    st.subheader("Rating wise App Count")

    # Grouping the dataset by rating and counting the apps for each unique rating value
    group = data.groupby(['Rating']).count()
    st.line_chart(group['App'],use_container_width=False,width=500,height=350)

with center_col2:
    # ---------------5. Content Rating-------------------------
       
    ## Counting apps based on unique Content Rating
    content_categories = data['Content Rating'].unique()
    dataf = data['Content Rating'].value_counts()

    ##Display a pie chart for the above data
    st.subheader("Content Ratings")
    colors = ['#4c78a8','royalblue','cyan','lightcyan']
    fig = px.pie(dataf, values="Content Rating", names=content_categories,color_discrete_sequence=pd.Series(colors))
    fig.update_layout(margin=dict(l=1,r=1,b=1,t=1),paper_bgcolor="#262730", height=350, width=500, font_color="white")
    fig.update_traces(textposition='inside', textinfo='percent+label')
    st.write(fig)






#-------------- 6.Categorie wise rating----------------

## Getting the mean of each feature by grouping it on the bases of category
result = data.groupby(['Category']).mean()
st.subheader("Category wise average rating")
## Bar chart for the average rating
st.bar_chart(result['Rating'],height=350,use_container_width=True)




#-------7. Top 10 by categories with highest ratings-----------

cat = st.selectbox("Select the categorie",options=categories)
cat_col1,cat_col2 = st.columns(2)

with cat_col1:
    st.subheader("Top 10 highest rated Apps by Categorie")
    # Query the category input by the user, sort and then display the first 10 apps
    datafra = data.query("Category == @cat")
    datafra = datafra.sort_values(by=['Rating'], ascending=False)
    datafra = datafra.iloc[:10]
    datafra = datafra[['App','Rating']]
    st.table(datafra)
with cat_col2:
    st.subheader("Top 10 Free Apps by Categorie")
    # Query the free category input by the user, sort and then display the first 10 apps
    datafra = data.query("Category == @cat and Type == 'Free'")
    datafra = datafra.sort_values(by=['Rating'], ascending=False)
    datafra = datafra.iloc[:10]
    datafra = datafra[['App','Rating']]
    st.table(datafra)



#------------8.Price Based Distribution-------------


##Individually finding all the Free and Paid apps
resp = data.groupby(['Category','Type']).count()
free = resp.query("Type=='Free'")
paid = resp.query("Type=='Paid'")



sub1,sub2,sub3 = st.columns(3)
with sub2:
    st.header("Price Based Distibution")

price_col1,price_col2,price_col3 = st.columns(3)
with price_col2:
    ## Create a stacked Bar graph for each category to show Free and Paid apps
    customscale=[
                [1.0, "rgb(76,120,168)"]]
    fig = go.Figure(data=[
        go.Bar(name='Paid', x=categories, y=paid['App'],marker=dict(color="#4c78a8",
                        colorscale=customscale)),
        go.Bar(name='Free', x=categories, y=free['App'],marker=dict(color="#92c2f7",
                        colorscale=customscale)),
        
    ])
    # Change the bar mode
    fig.update_traces(texttemplate='%{text:.2s}', textposition='outside')
    fig.update_layout(barmode='stack',margin=dict(l=1,r=1,b=1,t=1), uniformtext_minsize=8, uniformtext_mode='hide',width=1000,height=300)

    st.write(fig)

with price_col1:
    ## Calculating overall count of Free and Paid Apps and displaying in a bar chart
    free_c = resp.query("Type=='Free'")
    free_count = free_c['App'].sum()
    paid_c = resp.query("Type=='Paid'")
    paid_count = paid_c['App'].sum()
    counts = [free_count, paid_count]
    colors = ['#92c2f7','#4c78a8']
    
    fig = px.pie(values=counts, names=["Free","Paid"],color_discrete_sequence=pd.Series(colors))
    fig.update_layout(margin=dict(l=1,r=1,b=1,t=1),paper_bgcolor="#262730", height=270, width=380, font_color="white")
    fig.update_traces(textposition='inside', textinfo='percent+label')
    st.write(fig)



st.sidebar.write("Made with ❤ by Rahul Goyal")

