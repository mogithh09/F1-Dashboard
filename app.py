import pandas as py
import numpy as np
import seaborn as sns
import streamlit as st 

##title##
st.image("https://logos-world.net/wp-content/uploads/2023/12/F1-Logo.png",width=200)
st.title("F1 Summary Dasboard")

##sidebar##
st.sidebar.write("Navigation")
page=st.sidebar.selectbox("Select option :",["Race summary","Race Stratergy"] )
if page =="Race summary":
  st.header("Race Summary")
else:
  st.header("Race stratergy")

import fastf1
year=2026
schedule=fastf1.get_event_schedule(year)
st.selectbox("2026 Races :"{schedule}

