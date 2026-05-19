import pandas as py
import numpy as np
import seaborn as sns
import streamlit as st 

##Track info##
track_data = {
    "albert_park": {
        "name": "Albert Park Circuit",
        "location": "Melbourne, Australia",
        "length": "5.278 km",
        "corners": 14,
        "image": "https://upload.wikimedia.org/wikipedia/commons/0/0a/Albert_Park_Circuit_2021.svg"
    },
    "shanghai": {
        "name": "Shanghai International Circuit",
        "location": "Shanghai, China",
        "length": "5.451 km",
        "corners": 16,
        "image": "https://upload.wikimedia.org/wikipedia/commons/4/4c/Shanghai_International_Racing_Circuit_track_map.svg"
    },
    "suzuka": {
        "name": "Suzuka Circuit",
        "location": "Suzuka, Japan",
        "length": "5.807 km",
        "corners": 18,
        "image": "https://upload.wikimedia.org/wikipedia/commons/5/5c/Suzuka_circuit_map--2005.svg"
    },
    "bahrain": {
        "name": "Bahrain International Circuit",
        "location": "Sakhir, Bahrain",
        "length": "5.412 km",
        "corners": 15,
        "image": "https://upload.wikimedia.org/wikipedia/commons/2/29/Bahrain_International_Circuit--Grand_Prix_Layout.svg"
    },
    "jeddah": {
        "name": "Jeddah Corniche Circuit",
        "location": "Jeddah, Saudi Arabia",
        "length": "6.174 km",
        "corners": 27,
        "image": "https://upload.wikimedia.org/wikipedia/commons/0/0f/Jeddah_Street_Circuit_2021.svg"
    },
    "miami": {
        "name": "Miami International Autodrome",
        "location": "Miami, USA",
        "length": "5.412 km",
        "corners": 19,
        "image": "https://upload.wikimedia.org/wikipedia/commons/2/2b/Miami_International_Autodrome.svg"
    },
    "imola": {
        "name": "Imola Circuit",
        "location": "Imola, Italy",
        "length": "4.909 km",
        "corners": 19,
        "image": "https://upload.wikimedia.org/wikipedia/commons/2/21/Imola.svg"
    },
    "monaco": {
        "name": "Circuit de Monaco",
        "location": "Monaco",
        "length": "3.337 km",
        "corners": 19,
        "image": "https://upload.wikimedia.org/wikipedia/commons/4/4e/Monte_Carlo_Formula_1_track_map.svg"
    },
    "villeneuve": {
        "name": "Circuit Gilles Villeneuve",
        "location": "Montreal, Canada",
        "length": "4.361 km",
        "corners": 14,
        "image": "https://upload.wikimedia.org/wikipedia/commons/2/21/Circuit_Gilles_Villeneuve.svg"
    },
    "catalunya": {
        "name": "Circuit de Barcelona-Catalunya",
        "location": "Barcelona, Spain",
        "length": "4.657 km",
        "corners": 14,
        "image": "https://upload.wikimedia.org/wikipedia/commons/3/3f/Circuit_de_Barcelona-Catalunya.svg"
    },
    "red_bull_ring": {
        "name": "Red Bull Ring",
        "location": "Spielberg, Austria",
        "length": "4.318 km",
        "corners": 10,
        "image": "https://upload.wikimedia.org/wikipedia/commons/3/36/Red_Bull_Ring_2022.svg"
    },
    "silverstone": {
        "name": "Silverstone Circuit",
        "location": "Silverstone, UK",
        "length": "5.891 km",
        "corners": 18,
        "image": "https://upload.wikimedia.org/wikipedia/commons/2/25/Silverstone_Circuit_2020.svg"
    },
    "hungaroring": {
        "name": "Hungaroring",
        "location": "Budapest, Hungary",
        "length": "4.381 km",
        "corners": 14,
        "image": "https://upload.wikimedia.org/wikipedia/commons/9/91/Hungaroring.svg"
    },
    "spa": {
        "name": "Circuit de Spa-Francorchamps",
        "location": "Spa, Belgium",
        "length": "7.004 km",
        "corners": 19,
        "image": "https://upload.wikimedia.org/wikipedia/commons/5/54/Spa-Francorchamps_of_Belgium.svg"
    },
    "zandvoort": {
        "name": "Circuit Zandvoort",
        "location": "Zandvoort, Netherlands",
        "length": "4.259 km",
        "corners": 14,
        "image": "https://upload.wikimedia.org/wikipedia/commons/4/4e/Circuit_Zandvoort_2020.svg"
    },
    "monza": {
        "name": "Monza Circuit",
        "location": "Monza, Italy",
        "length": "5.793 km",
        "corners": 11,
        "image": "https://upload.wikimedia.org/wikipedia/commons/5/5c/Monza_track_map.svg"
    },
    "baku": {
        "name": "Baku City Circuit",
        "location": "Baku, Azerbaijan",
        "length": "6.003 km",
        "corners": 20,
        "image": "https://upload.wikimedia.org/wikipedia/commons/6/6e/Baku_City_Circuit.svg"
    },
    "marina_bay": {
        "name": "Marina Bay Street Circuit",
        "location": "Singapore",
        "length": "4.940 km",
        "corners": 19,
        "image": "https://upload.wikimedia.org/wikipedia/commons/6/6c/Marina_Bay_Street_Circuit_2023.svg"
    },
    "americas": {
        "name": "Circuit of the Americas",
        "location": "Austin, USA",
        "length": "5.513 km",
        "corners": 20,
        "image": "https://upload.wikimedia.org/wikipedia/commons/2/2e/Circuit_of_the_Americas.svg"
    },
    "rodriguez": {
        "name": "Autódromo Hermanos Rodríguez",
        "location": "Mexico City, Mexico",
        "length": "4.304 km",
        "corners": 17,
        "image": "https://upload.wikimedia.org/wikipedia/commons/3/36/Aut%C3%B3dromo_Hermanos_Rodr%C3%ADguez.svg"
    },
    "interlagos": {
        "name": "Interlagos Circuit",
        "location": "São Paulo, Brazil",
        "length": "4.309 km",
        "corners": 15,
        "image": "https://upload.wikimedia.org/wikipedia/commons/4/4b/Aut%C3%B3dromo_Jos%C3%A9_Carlos_Pace.svg"
    },
    "vegas": {
        "name": "Las Vegas Strip Circuit",
        "location": "Las Vegas, USA",
        "length": "6.201 km",
        "corners": 17,
        "image": "https://upload.wikimedia.org/wikipedia/commons/a/a4/Las_Vegas_Strip_Circuit_2023.svg"
    },
    "losail": {
        "name": "Losail International Circuit",
        "location": "Qatar",
        "length": "5.419 km",
        "corners": 16,
        "image": "https://upload.wikimedia.org/wikipedia/commons/3/3a/Losail_International_Circuit_2023.svg"
    },
    "yas_marina": {
        "name": "Yas Marina Circuit",
        "location": "Abu Dhabi, UAE",
        "length": "5.281 km",
        "corners": 16,
        "image": "https://upload.wikimedia.org/wikipedia/commons/2/21/Yas_Marina_Circuit_2021.svg"
    }
}

##title##
st.image("https://upload.wikimedia.org/wikipedia/commons/thumb/3/33/F1.svg/500px-F1.svg.png",width=300)
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



##Track info## 
def get_circuit_id(selected_race, races):
    for race in races:
        if race['raceName'] == selected_race:
            return race['Circuit']['circuitId']

circuit_id = get_circuit_id(selected_race, races)
info = track_data.get(circuit_id)
st.subheader("🏁 Track Info")

if info:
    col1, col2 = st.columns(2)

    with col1:
        image_path = f"{circuit_id}.WEBP"
        st.image(image_path, use_container_width=True)

    with col2:
        st.markdown(f"### {info['name']}")
        st.write("📍🌍",info["location"])
        st.metric("Length:", info["length"])
        st.metric("Corners:", info["corners"])



##race winners##

def fetchurl(selected_race, races):
    for race in races:
        if race['raceName'] == selected_race:
            roundno = race['round']
            url = f"https://api.jolpi.ca/ergast/f1/2024/{roundno}/results.json"
            return url


url = fetchurl(selected_race, races)

if url:
    response = requests.get(url)
    data = response.json()

    races_data = data['MRData']['RaceTable']['Races']

    if races_data:
        results = races_data[0].get('Results', [])
        top3 = results[:3]
        p1 = top3[0]
        p2 = top3[1]
        p3 = top3[2]
        p1_img = f"{p1['Driver']['driverId']}.jpeg"
        p2_img = f"{p2['Driver']['driverId']}.jpeg"
        p3_img = f"{p3['Driver']['driverId']}.jpeg"
        st.subheader('🏆Podium')
        col1, col2, col3 = st.columns(3)
        with col1:
            st.image(p2_img)
            st.markdown(f"## 🥈 {p2['Driver']['familyName']}")
        with col2:
            st.image(p1_img)
            st.markdown(f"## 🥇 {p1['Driver']['familyName']}")
        with col3:
            st.image(p3_img)
            st.markdown(f"## 🥉 {p3['Driver']['familyName']}")
        

        for r in top3:
            st.write(r['Driver']['givenName'])

    else:
        st.error("No race data found")

else:
    st.error("Invalid race selection")


##Fastest lap### 
st.markdown("""
<style>
.fastest-lap-card {
    background: #111111;
    padding: 25px;
    border-radius: 20px;
    border: 3px solid #bb00ff;
    box-shadow: 0 0 40px #bb00ff;
}
</style>
""", unsafe_allow_html=True)
st.markdown('<div class="fastest-lap-card">', unsafe_allow_html=True)
time=results[0]['FastestLap']['Time']['time']
st.header('🟣FASTEST LAP')
driver=results[0]['Driver']['familyName']
driver_img=f"{results[0]['Driver']['driverId']}.jpeg"
col1,col2=st.columns([1,2])
with col1:
   st.image(driver_img, width=150)
with col2:
    st.subheader(driver)
    st.write(time)

