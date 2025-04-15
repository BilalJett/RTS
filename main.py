import numpy as np
import streamlit as st
construction_types_solar = ("Light (with carpet 10%)",
    "Light (with carpet 50%)",
    "Light (with carpet 90%)",
    "Light (no carpet 10%)",
    "Light (no carpet 50%)",
    "Light (no carpet 90%)",
    "Medium (with carpet 10%)",
    "Medium (with carpet 50%)",
    "Medium (with carpet 90%)",
    "Medium (no carpet 10%)",
    "Medium (no carpet 50%)",
    "Medium (no carpet 90%)",
    "Heavy (with carpet 10%)",
    "Heavy (with carpet 50%)",
    "Heavy (with carpet 90%)",
    "Heavy (no carpet 10%)",
    "Heavy (no carpet 50%)",
    "Heavy (no carpet 90%)",)
construction_types_non_solar = ("Light (with carpet 10%)",
    "Light (with carpet 50%)",
    "Light (with carpet 90%)",
    "Light (no carpet 10%)",
    "Light (no carpet 50%)",
    "Light (no carpet 90%)",
    "Medium (with carpet 10%)",
    "Medium (with carpet 50%)",
    "Medium (with carpet 90%)",
    "Medium (no carpet 10%)",
    "Medium (no carpet 50%)",
    "Medium (no carpet 90%)",
    "Heavy (with carpet 10%)",
    "Heavy (with carpet 50%)",
    "Heavy (with carpet 90%)",
    "Heavy (no carpet 10%)",
    "Heavy (no carpet 50%)",
    "Heavy (no carpet 90%)",
    "light Interior zone with carpet",
    "light Interior zone no carpet",
    "Medium Interior zone with carpet",
    "Medium Interior zone no carpet",
    "Heavy Interior zone with carpet",
    "Heavy Interior zone no carpet",)
st.session_state.percentage_of_daily_range = np.array(
    [87, 92, 96, 99, 100, 98, 93, 84, 71, 56, 39, 23, 11, 3, 0, 3, 10, 21, 34, 47, 58, 68, 76, 82])


st.title("Calculating Cooling load using Radiant Time Series Method (RTSM)")
st.divider()

if st.session_state.get("preferredscale", "Imperial system") == "Imperial system":
    st.session_state.temp = "(°F)"
    st.session_state.U = "(BTU/(hr-ft²-F))"
    st.session_state.area = "(ft²)"
    st.session_state.irridation = "(BTU/(hr-ft²))"
    st.session_state.heat ="(BTU/hr)"

else:
    st.session_state.temp = "(°C)"
    st.session_state.U = "(W/(m²-K))"
    st.session_state.area = "(m²)"
    st.session_state.irridation = "(W/m²)"
    st.session_state.heat ="(W)"

st.subheader("Measurement system")
if "preferredscale" not in st.session_state:
    st.session_state["preferredscale"] = "Imperial system"
st.session_state.preferredscale = st.selectbox("Measurement system",("Imperial system","Metric system"),
                                               index=("Imperial system","Metric system").index(st.session_state["preferredscale"]))


st.divider()
st.subheader("Climate Data")
column1, column2 = st.columns(2)

if "Latitude" not in st.session_state:
    st.session_state["Latitude"] = 33.27
Latitude = column1.number_input(f"Latitude (°)", value=float(st.session_state["Latitude"]),min_value=-90.0,max_value=90.0,format="%.3f")
st.session_state.Latitude = Latitude

if "Longitude" not in st.session_state:
    st.session_state["Longitude"] = 44.23
Longitude = column2.number_input(f"Longitude (°)", value=float(st.session_state["Longitude"]),min_value=-180.0,max_value=180.0,format="%.3f")
st.session_state.Longitude = Longitude

if "ET" not in st.session_state:
    st.session_state["ET"] = -6.5
ET = column1.number_input(f"Equation of Time (min)", value=float(st.session_state["ET"]),min_value=-14.0 ,max_value=16.0)
st.session_state.ET = ET

if "LSM" not in st.session_state:
    st.session_state["LSM"] = 45
LSM = column2.number_input("Local Standard Meridian (°)", value=float(st.session_state["LSM"]),min_value=-180.0 ,max_value=180.0,format="%.3f")
st.session_state.LSM = LSM

if "delta" not in st.session_state:
    st.session_state["delta"] = 20.4
delta = column1.number_input(f"Solar declination angle (°)", value=float(st.session_state["delta"]),min_value=-23.45 ,max_value=23.45)
st.session_state.delta = delta

if "Solar_const" not in st.session_state:
    st.session_state["Solar_const"] = 428
Solar_const = column2.number_input(f"Solar constant {st.session_state.irridation}",
                                   value=float(st.session_state["Solar_const"]))
st.session_state.Solar_const = Solar_const


st.divider()
st.subheader("Design Conditions")
c1,c2 =st.columns(2)

if "construction_types_solar" not in st.session_state:
    st.session_state["construction_types_solar"] = "Medium (with carpet 50%)"
construction_types_solar = c1.selectbox("level of construction (solar)",construction_types_solar,
                                             index=construction_types_solar.index(st.session_state["construction_types_solar"]))
st.session_state.construction_types_solar = construction_types_solar

if "construction_types_non_solar" not in st.session_state:
    st.session_state["construction_types_non_solar"] = "Medium (with carpet 50%)"
construction_types_non_solar = c2.selectbox("level of construction (non-solar)",construction_types_non_solar,
                                                 index=construction_types_non_solar.index(st.session_state["construction_types_non_solar"]))
st.session_state.construction_types_non_solar = construction_types_non_solar

if "T_design" not in st.session_state:
    st.session_state["T_design"] = 120
T_design = c2.number_input(f"The outdoor design temperature {st.session_state.temp}",
                           value=float(st.session_state["T_design"]))
st.session_state.T_design = T_design

if "T_indoor" not in st.session_state:
    st.session_state["T_indoor"] = 77
T_indoor = c1.number_input(f"The required temperature inside the room {st.session_state.temp}",
                           value=float(st.session_state["T_indoor"]))
st.session_state.T_indoor = T_indoor

if "daily_range" not in st.session_state:
    st.session_state["daily_range"] = 28
daily_range = c1.number_input(f"The daily range {st.session_state.temp}",
                              value=float(st.session_state["daily_range"]))
st.session_state.daily_range = daily_range



st.divider()

st.subheader("Advanced Settings")
cc1,cc2 = st.columns(2)
if "taub" not in st.session_state:
    st.session_state["taub"] = 0.515
taub = cc1.number_input("Beam transmittance", value=float(st.session_state["taub"])
                        ,format="%.4f")
st.session_state.taub = taub

if "taud" not in st.session_state:
    st.session_state["taud"] = 2.066
taud = cc1.number_input("Diffuse transmittance", value=float(st.session_state["taud"])
                        ,format="%.4f")
st.session_state.taud = taud

if "ground_reflectance" not in st.session_state:
    st.session_state["ground_reflectance"] = 0.2
ground_reflectance = cc2.number_input("ground reflectance", value=float(st.session_state["ground_reflectance"]),
                                      format="%.4f",min_value=0.0 ,max_value=1.0 )
st.session_state.ground_reflectance = ground_reflectance

if "precise_DR" not in st.session_state:
    st.session_state["precise_DR"] = False
precise_DR = cc2.toggle("Enter outdoor temperatures manually (more accurate)", value=st.session_state["precise_DR"])
st.session_state.precise_DR = precise_DR
st.divider()

c = st.columns(4)
Temp24 = np.zeros(24)
percentage_of_daily_range = np.zeros(24)
if st.session_state.precise_DR == True:
    if "Temp24" not in st.session_state:
        st.session_state.Temp24 = Temp24
    for i, e in enumerate(range(24)):
        with c[i % 4]:
            Temp24[i] = st.number_input(f"Temperature at time {i+1} {st.session_state.temp}", value=float(st.session_state.Temp24[i]),format='%.2f')
    st.session_state.Temp24 = Temp24

elif st.session_state.precise_DR == False:
    if "Temp24" not in st.session_state:
        st.session_state.Temp24 = Temp24


st.session_state["totalNO1"] = np.zeros(24)
st.session_state["totalNO2"] = np.zeros(24)
st.session_state["totalNO3"] = np.zeros(24)
st.session_state["totalNO4"] = np.zeros(24)
st.session_state["total_roomROOF"] = np.zeros(24)
st.session_state["Qlighting"] = np.zeros(24)
st.session_state.TsolairNO1 = np.zeros(24)
st.session_state.TsolairNO2 = np.zeros(24)
st.session_state.TsolairNO3 = np.zeros(24)
st.session_state.TsolairNO4 = np.zeros(24)
st.session_state.TsolairROOF = np.zeros(24)
if "total_roomNO1" not in st.session_state:
    st.session_state["total_roomNO1"] = np.zeros(24)
if "total_roomNO2" not in st.session_state:
    st.session_state["total_roomNO2"] = np.zeros(24)
if "total_roomNO3" not in st.session_state:
    st.session_state["total_roomNO3"] = np.zeros(24)
if "total_roomNO4" not in st.session_state:
    st.session_state["total_roomNO4"] = np.zeros(24)
if "total_roomROOF" not in st.session_state:
    st.session_state["total_roomROOF"] = np.zeros(24)
if "Qlighting" not in st.session_state:
    st.session_state["Qlighting"] = np.zeros(24)
