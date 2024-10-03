import streamlit as st
import pandas as pd

st.title("Wellcome Here")
st.write(
    "Let's start building ML! For help and inspiration, head over to [docs.streamlit.io](https://docs.streamlit.io/)."
)

with st.expander('Data'):
    df = pd.read_csv("penguins.csv")
    st.write(df.head())
    st.write(++x++)
   
    x = 0
    st.write(x + 1)  # Correct way to increment and display x
    
    # Drop the 'species' column
    x = df.drop("species", axis=1)
    st.write(x)  # Display the dataframe without the 'species' column
