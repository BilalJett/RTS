import numpy as np
import streamlit as st
import pandas as pd

#Graphing
st.divider()
st.subheader("Graphs and Tables")
datawindow = pd.DataFrame({
    "Total load from wall #1 ":np.array(st.session_state.totalNO1).ravel(),
    "Total load from wall #2 ":np.array(st.session_state.totalNO2).ravel(),
    "Total load from wall #3 ":np.array(st.session_state.totalNO3).ravel(),
    "Total load from wall #4 ":np.array(st.session_state.totalNO4).ravel(),
    "Total load from roof ":   np.array(st.session_state.total_roomROOF).ravel(),
    "Total load from lighting":np.array(st.session_state.Qlighting).ravel(),
    "Total cooling load" :np.array(st.session_state.totalNO1).ravel()+np.array(st.session_state.totalNO2).ravel()+
                          np.array(st.session_state.totalNO3).ravel()+np.array(st.session_state.totalNO4).ravel()+
                          np.array(st.session_state.total_roomROOF).ravel()+np.array(st.session_state.Qlighting).ravel()
})
datawindow.index =datawindow.index+1

Temps = pd.DataFrame({
    "Tsolair on wall #1": st.session_state.TsolairNO1,
    "Tsolair on wall #2": st.session_state.TsolairNO2,
    "Tsolair on wall #3": st.session_state.TsolairNO3,
    "Tsolair on wall #4": st.session_state.TsolairNO4,
    "Tsolair on Roof": st.session_state.TsolairROOF,
})
Temps.index = Temps.index + 1

# Qs = pd.DataFrame({
#     "Q convection":Qcn,
#     "Q Radiation":Qrn,
#     "Q total": Qwall,
# })
# Qs.index = Qs.index +1

# data=pd.DataFrame({
#     "AST":AST,
#     "Hour Angle":H,
#     "Solar Altitude": np.degrees(beta) ,
#     "Solar Azimuth":np.degrees(phi),
#     "solar Air Mass":m,
#     "Normal Beam irridiation" : Eb,
#     "Surface Incidence Angle" : np.degrees(incident_angle),
#     "Surface Beam Irridiation" : ED,
#     "Diffuse Solar Heat Gain" : Ed,
#     "Ground Diffuse" : Er,
#     "Y ratio" : Y,
#     "Sky Diffuse" : Etd,
#     "Diffused Total" : Er + Etd,
#     "Total Surface irradiation" : Et
# })
# data.index = data.index +1

# total_room = pd.DataFrame({
#     "Total cooling load from Roof" : Qwall + Qwcn + Qwbn + Qwdn
# })
# total_room.index = total_room.index+1

st.subheader("Solair Temperatures")
st.area_chart(data=Temps)
# st.subheader("Solar irradiation on Roof")
# st.write(data)
# st.subheader("cooling load from Roof")
# st.write(Qs)
# st.area_chart(data=Qs)

st.subheader("Total heat gain")
st.write(datawindow)
st.area_chart(data=datawindow)
