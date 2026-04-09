import pandas as py
import numpy as np
import seaborn as sns
import streamlit as st 

##title##
st.image("https://logos-world.net/wp-content/uploads/2023/12/F1-Logo.png",width=200)
st.title("F1 Summary Dasboard")

##sidebar##
st.sidebar.write("Navigation")
page=st.sidebar.selectbox("Select option :",["Race summary"] )
if page =="Race summary":
  st.header("Race Summary")
  import requests
  url = "http://ergast.com/api/f1/2026.json"
  response = requests.get(url)
  data = response.json()
  st.write(data)

