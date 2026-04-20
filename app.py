import pandas as py
import numpy as np
import seaborn as sns
import streamlit as st 

##title##
st.image("https://wallpaperaccess.com/download/formula-1-logo-6122403",width=300)
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
  for race in  races:
    race_names.append(race['raceName'])
  selected_race = st.sidebar.selectbox("Select Race", race_names)
  st.write("Selected Race:", selected_race)
else:
  pass

##race winners##
def fetchurl(selected_race, races):
  for race in races:
    if race['raceName'] == selected_race:
      roundno = race['round']
      url=f"https://api.jolpi.ca/ergast/f1/2024/{roundno}/results.json"
      return url

result_url=fetchurl(selected_race, races)
st.write("Genrated Url:",result_url)


