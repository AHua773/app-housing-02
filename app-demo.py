import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv('housing.csv')

plt.style.use('seaborn')

st.title('Houhua Zhang')


price = st.sidebar.slider('Median House Price', 0, 500001, 200000)
location = st.sidebar.multiselect('Location', df.ocean_proximity.unique(), df.ocean_proximity.unique())
income = st.sidebar.radio('income level', ('Low', 'Medium', 'High'))

df = df[df.median_house_value <= price]
df = df[df.ocean_proximity.isin(location)]
if income is not None:
    if income == 'Low':
        df = df[df.median_income <= 2.5]
    elif income == 'Medium':
        df = df[(df.median_income > 2.5) & (df.median_income <= 4.5)]
    elif income == 'High':
        df = df[df.median_income > 4.5]
else:
    pass

fig, ax = plt.subplots()
house_price = df.median_house_value
house_price.hist(ax=ax, bins=30)

st.map(df)
st.pyplot(fig)
