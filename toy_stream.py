import matplotlib.pyplot as plt
import streamlit as st
import numpy as np
import pandas as pd
df = pd.read_csv('toy_dataset.csv')
city = df['City']
income = df['Income']
plt.barh(city, income)
plt.title('Income raised by each city')
plt.xlabel('Income')
plt.ylabel('City')
st.pyplot(plt)