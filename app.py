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
  url = "https://api.jolpi.ca/ergast/f1/2024.json"
  response = requests.get(url)
  data = response.json()
  races = data['MRData']['RaceTable']['Races']
  race_names = []
  for each race:
    race_names.append(race['raceName'])
  selected_race = st.sidebar.selectbox("Select Race", race_names)
  st.write("Selected Race:", selected_race)

