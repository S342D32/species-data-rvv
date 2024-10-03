import streamlit as st
import pandas as pd
import numpy as np

st.title("Welcome Here")
st.write(
    "Let's start building ML! For help and inspiration, head over to docs.streamlit.io."
)

with st.expander('Data'):
    df = pd.read_csv("penguins.csv")
    st.write(df.head())
    
    # Initialize x with a valid value
    x = 0
    st.write(x + 1)  # Correct way to increment and display x
    
    # Drop the 'species' column
    x = df.drop("species", axis=1)
    st.write(x)  # Display the dataframe without the 'species' column
with st.expander('Data Visualization'):
    
    st.scatter_chart(data =df,x='bill_length_mm',y ='body_mass_g',color='species')
with st.sidebar:
    st.header('Input Feature')
    island = st.selectbox('Island',('Biscoe','Dream','Targersen'))
    bill_length_mm=st.sidebar('Bill length(mm)',32.1,59.6,43.9)
    bill_depth_mm =st.sidebar('Bill depth(mm)',13.1,21.5,17.2)
    flipper_length_mm = st.sidebar('flipper_length_mm',172.0,231.0,201.0)
    body_mass_g=st.sidebar('body mass (g)',2700.0,6300.0,4207.0)
    gender =st.selectbox('Gender',('Male','Female'))

data={'island':island,
      'bill_length_mm':bill_length_mm,
      'bill_depth_mm':bill_depth_mm,
      'flipper_length_mm':flipper_length_mm,
      'body_mass_g':body_mass_g,
      'gender':gender 
     }
input_df = pd.DataFrame(data,index[0])
input_penguines = pd.concat([input_df,x],axis=0)
input_df
