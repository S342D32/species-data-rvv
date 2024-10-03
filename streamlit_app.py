import streamlit as st

st.title("Wellcome Here")
st.write(
    "Let's start building ML! For help and inspiration, head over to [docs.streamlit.io](https://docs.streamlit.io/)."
)
df=pd.read_csv("Iris.csv")
df.head()
