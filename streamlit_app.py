import streamlit as st
import pandas as pd

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
