import numpy as np
import streamlit as st
import pandas as pd

#Defining things
st.title("wall #3")
T_design =st.session_state.get("T_design")
daily_range =st.session_state.get("daily_range")
percentage_of_daily_range = st.session_state.percentage_of_daily_range
T_indoor = st.session_state.get("T_indoor")
walls = ("wall number 1 (Curtain walls)",
        "wall number 2 (Curtain walls)",
        "wall number 3 (Curtain walls)",
        "wall number 4 (Stud walls)",
         "wall number 5 (Stud walls)",
         "wall number 6 (Stud walls)",
         "wall number 7 (Stud walls)",
         "wall number 8 (EIFS)",
         "wall number 9 (EIFS)",
         "wall number 10 (EIFS)",
         "wall number 11 (Brick walls)",
         "wall number 12 (Brick walls)",
         "wall number 13 (Brick walls)",
         "wall number 14 (Brick walls)",
         "wall number 15 (Brick walls)",
         "wall number 16 (Brick walls)",
         "wall number 17 (Brick walls)",
         "wall number 18 (Brick walls)",
         "wall number 19 (Brick walls)",
         "wall number 20 (Brick walls)",
         "wall number 21 (Concrete block wall)",
         "wall number 22 (Concrete block wall)",
         "wall number 23 (Concrete block wall)",
         "wall number 24 (Concrete block wall)",
         "wall number 25 (Concrete block wall)",
         "wall number 26 (Concrete block wall)",
         "wall number 27 (Precast and cast-in-place concrete walls)",
         "wall number 28 (Precast and cast-in-place concrete walls)",
         "wall number 29 (Precast and cast-in-place concrete walls)",
         "wall number 30 (Precast and cast-in-place concrete walls)",
         "wall number 31 (Precast and cast-in-place concrete walls)",
         "wall number 32 (Precast and cast-in-place concrete walls)",
         "wall number 33 (Precast and cast-in-place concrete walls)",
         "wall number 34 (Precast and cast-in-place concrete walls)",
         "wall number 35 (Precast and cast-in-place concrete walls)",)
CTS = [
[18, 58, 20, 4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
[25, 57, 15, 3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
[8, 45, 32, 11, 3, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
[19, 59, 18, 3, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
[6, 42, 33, 13, 4, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
[7, 44, 32, 12, 4, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
[5, 41, 34, 13, 4, 2, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
[11, 50, 26, 9, 3, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
[2, 25, 31, 20, 11, 5, 3, 2, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
[1, 2, 6, 9, 9, 9, 8, 7, 6, 6, 5, 5, 4, 4, 3, 3, 3, 2, 2, 2, 2, 1, 1, 0],
[0, 5, 14, 17, 15, 12, 9, 7, 5, 4, 3, 2, 2, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0],
[0, 4, 13, 17, 15, 12, 9, 7, 5, 4, 3, 2, 2, 2, 2, 1, 1, 1, 0, 0, 0, 0, 0, 0],
[0, 1, 7, 12, 13, 13, 11, 9, 7, 6, 5, 4, 3, 2, 2, 1, 1, 1, 1, 1, 0, 0, 0, 0],
[1, 1, 2, 5, 8, 9, 9, 9, 8, 7, 7, 6, 5, 4, 4, 3, 3, 2, 2, 2, 1, 1, 1, 0],
[2, 2, 2, 3, 5, 6, 7, 7, 7, 7, 6, 6, 5, 5, 5, 4, 4, 3, 3, 3, 3, 2, 2, 1],
[2, 2, 2, 4, 5, 6, 6, 7, 7, 6, 6, 6, 5, 5, 5, 4, 4, 4, 3, 3, 3, 2, 2, 1],
[1, 1, 3, 6, 7, 8, 8, 8, 8, 7, 6, 6, 5, 4, 4, 3, 3, 3, 2, 2, 2, 1, 1, 1],
[3, 3, 3, 3, 3, 4, 4, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 4, 4, 4, 4, 4, 4, 3],
[4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 5, 5, 5, 5, 4, 4, 4, 4, 4, 4, 4, 4, 4],
[3, 3, 3, 4, 4, 4, 5, 5, 5, 5, 5, 5, 5, 5, 5, 4, 4, 4, 4, 4, 4, 4, 3, 3],
[0, 4, 13, 16, 14, 11, 9, 7, 6, 4, 3, 3, 2, 2, 2, 1, 1, 1, 1, 0, 0, 0, 0, 0],
[1, 1, 5, 9, 11, 10, 9, 8, 7, 6, 5, 4, 4, 3, 3, 3, 2, 2, 2, 1, 1, 1, 1, 1],
[0, 2, 8, 12, 12, 11, 9, 8, 7, 6, 5, 4, 3, 2, 2, 2, 1, 1, 1, 1, 1, 1, 1, 0],
[1, 11, 21, 20, 15, 10, 7, 5, 3, 2, 2, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
[0, 3, 12, 16, 15, 12, 10, 8, 6, 4, 3, 3, 2, 2, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0],
[1, 1, 2, 5, 7, 9, 9, 8, 8, 7, 6, 6, 5, 4, 4, 3, 3, 2, 2, 2, 2, 2, 1, 1],
[1, 10, 20, 18, 14, 10, 7, 5, 4, 3, 2, 2, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0],
[0, 8, 18, 18, 14, 11, 8, 6, 4, 3, 2, 2, 2, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0],
[1, 1, 3, 6, 8, 9, 9, 9, 8, 7, 7, 6, 5, 4, 4, 3, 2, 2, 1, 1, 1, 1, 1, 1],
[2, 2, 3, 5, 6, 6, 6, 6, 6, 6, 5, 5, 5, 5, 4, 4, 4, 3, 3, 3, 3, 3, 3, 2],
[1, 2, 3, 6, 7, 8, 8, 7, 7, 6, 6, 5, 5, 4, 4, 3, 3, 3, 2, 2, 2, 2, 2, 2],
[3, 3, 4, 5, 6, 6, 6, 5, 5, 5, 5, 5, 4, 4, 4, 4, 4, 4, 4, 3, 3, 3, 3, 2],
[1, 2, 5, 8, 9, 9, 8, 7, 6, 6, 5, 5, 4, 4, 3, 3, 3, 2, 2, 2, 2, 2, 1, 1],
[2, 2, 3, 3, 5, 5, 6, 6, 6, 6, 6, 5, 5, 5, 4, 4, 4, 4, 4, 3, 3, 3, 3, 3],
[1, 2, 4, 7, 8, 8, 8, 8, 7, 6, 6, 5, 4, 4, 4, 3, 3, 3, 2, 2, 2, 1, 1, 1],
[6, 45, 33, 11, 3, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
[10, 57, 27, 5, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
[27, 62, 10, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
[1, 17, 31, 24, 14, 7, 4, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
[1, 17, 34, 25, 13, 6, 3, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
[1, 12, 25, 22, 15, 10, 6, 4, 2, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
[0, 7, 18, 18, 15, 11, 8, 6, 5, 3, 3, 2, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0],
[1, 3, 8, 10, 10, 9, 8, 7, 6, 5, 5, 4, 4, 3, 3, 3, 2, 2, 2, 2, 1, 1, 1, 0],
[18, 61, 18, 3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
[4, 41, 35, 14, 4, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
[8, 53, 30, 7, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
[1, 23, 38, 22, 10, 4, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
[0, 10, 22, 20, 14, 10, 7, 5, 4, 3, 2, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
[1, 2, 8, 11, 11, 10, 9, 7, 6, 5, 5, 4, 3, 3, 3, 2, 2, 2, 1, 1, 1, 1, 1, 1],
[2, 2, 3, 6, 7, 8, 8, 7, 7, 6, 5, 5, 5, 4, 4, 3, 3, 3, 3, 2, 2, 2, 2, 1],
[2, 2, 3, 4, 5, 6, 6, 6, 6, 6, 6, 5, 5, 5, 4, 4, 4, 4, 3, 3, 3, 3, 3, 2],
[2, 2, 5, 6, 7, 7, 6, 6, 6, 5, 5, 5, 4, 4, 4, 4, 3, 3, 3, 3, 3, 3, 2, 2],
[3, 3, 3, 5, 6, 6, 6, 6, 6, 5, 5, 5, 5, 4, 4, 4, 4, 4, 3, 3, 3, 3, 2, 2],
[1, 2, 6, 8, 8, 8, 7, 7, 6, 5, 5, 5, 4, 4, 3, 3, 3, 3, 2, 2, 2, 2, 2, 2],

]
RTS_SOLAR = [[53, 17, 9, 5, 3, 2, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0],
[55, 17, 9, 5, 3, 2, 2, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
[56, 17, 9, 5, 3, 2, 2, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
[44, 19, 11, 7, 5, 3, 3, 2, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
[45, 20, 11, 7, 5, 3, 2, 2, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
[46, 20, 11, 7, 5, 3, 2, 2, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
[52, 16, 8, 5, 3, 2, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0],
[54, 16, 8, 4, 3, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0],
[55, 15, 8, 4, 3, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0],
[28, 15, 10, 7, 6, 5, 4, 4, 3, 3, 2, 2, 2, 2, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0],
[29, 15, 10, 7, 6, 5, 4, 3, 3, 3, 2, 2, 2, 2, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0],
[29, 15, 10, 7, 6, 5, 4, 3, 3, 3, 2, 2, 2, 2, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0],
[47, 11, 6, 4, 3, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1],
[49, 12, 6, 4, 3, 2, 2, 2, 2, 2, 2, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
[51, 12, 6, 3, 3, 2, 2, 2, 2, 2, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
[26, 12, 7, 5, 4, 4, 3, 3, 3, 3, 3, 3, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2],
[27, 13, 7, 5, 4, 4, 3, 3, 3, 3, 3, 3, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 1, 1],
[28, 13, 7, 5, 4, 4, 3, 3, 3, 3, 3, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 1, 1]]
RTS_NONSOLAR = [
[47, 19, 11, 6, 4, 3, 2, 2, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
[50, 18, 10, 6, 4, 3, 2, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
[53, 17, 9, 5, 3, 2, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0],
[41, 20, 12, 8, 5, 4, 3, 2, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
[43, 19, 11, 7, 5, 3, 3, 2, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
[46, 19, 11, 7, 5, 3, 2, 2, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
[46, 18, 10, 6, 4, 2, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0],
[49, 17, 9, 5, 3, 2, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0],
[52, 16, 8, 5, 3, 2, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0],
[31, 17, 11, 8, 6, 4, 4, 3, 3, 2, 2, 2, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0],
[33, 16, 10, 7, 5, 4, 3, 3, 2, 2, 2, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0],
[35, 15, 10, 7, 5, 4, 3, 3, 2, 2, 2, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0],
[34, 9, 6, 4, 4, 4, 3, 3, 3, 3, 3, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 1, 1],
[38, 9, 6, 4, 4, 3, 3, 3, 3, 3, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 1, 1, 1, 1],
[42, 9, 5, 4, 4, 3, 3, 3, 3, 2, 2, 2, 2, 2, 2, 2, 2, 2, 1, 1, 1, 1, 1, 1],
[22, 10, 6, 5, 5, 4, 4, 4, 4, 3, 3, 3, 3, 3, 3, 2, 2, 2, 2, 2, 2, 2, 2, 2],
[25, 9, 6, 5, 5, 4, 4, 4, 3, 3, 3, 3, 3, 3, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2],
[28, 9, 6, 5, 4, 4, 4, 4, 3, 3, 3, 3, 3, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 1],
[46, 19, 11, 6, 4, 3, 2, 2, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
[40, 20, 12, 8, 5, 4, 3, 2, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
[46, 18, 10, 6, 3, 2, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0],
[31, 17, 11, 8, 6, 4, 4, 3, 3, 2, 2, 2, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0],
[33, 9, 6, 5, 4, 4, 3, 3, 3, 3, 3, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 1, 1],
[21, 9, 6, 5, 5, 4, 4, 4, 4, 3, 3, 3, 3, 3, 3, 3, 3, 2, 2, 2, 2, 2, 2, 2],
]
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
all = walls
surface_color = ("Light Colored Surface","Dark Colored Surface")

#Qs
Qn = np.zeros(24)
Qin = np.zeros(24)
Qcn = np.zeros(24)
Qrn = np.zeros(24)
TsolairNO3 = np.zeros(24)

#Solar angles
AST = np.zeros(24)
H = np.zeros(24)
beta = np.zeros(24)
phi = np.zeros(24)
gammaaNO3 = np.zeros(24)
ED = np.zeros(24)
Ed = np.zeros(24)
Er = np.zeros(24)
Y=np.zeros(24)
m=np.zeros(24)
taub =  st.session_state["taub"]
taud =  st.session_state["taud"]
ground_reflectance =  st.session_state["ground_reflectance"]
ET= st.session_state["ET"]
LSM=st.session_state["LSM"]
Longitude=st.session_state["Longitude"]
Latitude = st.session_state["Latitude"]
delta = st.session_state["delta"]
Solar_const = st.session_state["Solar_const"]

#window stuff
SHGC={
'Uncoated Single Glazing 1a 3 mm CLR ': [0.86, 0.84, 0.82, 0.78, 0.67, 0.42, 0.78],
'Uncoated Single Glazing 1b 6 mm CLR ': [0.81, 0.80, 0.78, 0.73, 0.62, 0.39, 0.73],
'Uncoated Single Glazing 1c 3 mm BRZ ': [0.73, 0.71, 0.68, 0.64, 0.55, 0.34, 0.65],
'Uncoated Single Glazing 1d 6 mm BRZ ': [0.62, 0.59, 0.57, 0.53, 0.45, 0.29, 0.54],
'Uncoated Single Glazing 1e 3 mm GRN ': [0.70, 0.68, 0.66, 0.62, 0.53, 0.33, 0.63],
'Uncoated Single Glazing 1f 6 mm GRN ': [0.60, 0.58, 0.56, 0.52, 0.45, 0.29, 0.54],
'Uncoated Single Glazing 1g 3 mm GRY ': [0.70, 0.68, 0.66, 0.61, 0.53, 0.33, 0.63],
'Uncoated Single Glazing 1h 6 mm GRY ': [0.59, 0.57, 0.55, 0.51, 0.44, 0.28, 0.52],
'Uncoated Single Glazing 1i 6 mm BLUGRN': [0.62, 0.59, 0.57, 0.54, 0.46, 0.30, 0.55],
'Reflective Single Glazing 1j 6 mm SS on CLR 8%' : [0.19, 0.19, 0.19, 0.18, 0.16, 0.10, 0.18],
'Reflective Single Glazing 1k 6 mm SS on CLR 14%': [0.25, 0.25, 0.24, 0.23, 0.20, 0.13, 0.23],
'Reflective Single Glazing 1l 6 mm SS on CLR 20%': [0.31, 0.30, 0.30, 0.28, 0.24, 0.16, 0.28],
'Reflective Single Glazing 1m 6 mm SS on GRN 14%': [0.25, 0.25, 0.24, 0.23, 0.21, 0.14, 0.23],
'Reflective Single Glazing 1n 6 mm TI on CLR 20%': [0.29, 0.29, 0.28, 0.27, 0.23, 0.15, 0.27],
'Reflective Single Glazing 1o 6 mm TI on CLR 30%': [0.39, 0.38, 0.37, 0.35, 0.30, 0.20, 0.35],
'Uncoated Double Glazing 5a 3 mm CLR CLR': [0.76, 0.74, 0.71, 0.64, 0.50, 0.26, 0.66],
'Uncoated Double Glazing 5b 6 mm CLR CLR': [0.70, 0.67, 0.64, 0.58, 0.45, 0.23, 0.60],
'Uncoated Double Glazing 5c 3 mm BRZ CLR': [0.62, 0.60, 0.57, 0.51, 0.39, 0.20, 0.53],
'Uncoated Double Glazing 5d 6 mm BRZ CLR': [0.49, 0.46, 0.44, 0.39, 0.31, 0.17, 0.41],
'Uncoated Double Glazing 5e 3 mm GRN CLR': [0.60, 0.57, 0.54, 0.49, 0.38, 0.20, 0.51],
'Uncoated Double Glazing 5f 6 mm GRN CLR': [0.49, 0.46, 0.44, 0.39, 0.31, 0.17, 0.41],
'Uncoated Double Glazing 5g 3 mm GRY CLR': [0.60, 0.57, 0.54, 0.48, 0.37, 0.20, 0.51],
'Uncoated Double Glazing 5h 6 mm GRY CLR': [0.47, 0.44, 0.42, 0.37, 0.29, 0.16, 0.39],
'Uncoated Double Glazing 5i 6 mm BLUGRN CLR': [0.50, 0.47, 0.45, 0.40, 0.32, 0.17, 0.43],
'Uncoated Double Glazing 5j 6 HI-P GRN CLR':  [0.39, 0.37 ,0.35, 0.31, 0.25, 0.14, 0.33],
'Reflective Double Glazing 5k 6 mm SS on CLR 8%, CLR  ': [0.13 ,0.12 ,0.12 ,0.11 ,0.10 ,0.06, 0.11],
'Reflective Double Glazing 5l 6 mm SS on CLR 14%, CLR ': [0.17 ,0.17 ,0.16 ,0.15 ,0.13 ,0.08, 0.16],
'Reflective Double Glazing 5m 6 mm SS on CLR 20%, CLR ': [0.22 ,0.21 ,0.21 ,0.19 ,0.16 ,0.09, 0.20],
'Reflective Double Glazing 5n 6 mm SS on GRN 14%, CLR ': [0.16 ,0.16 ,0.15 ,0.14 ,0.12 ,0.08, 0.14],
'Reflective Double Glazing 5o 6 mm TI on CLR 20%, CLR ': [0.21 ,0.20 ,0.19 ,0.18 ,0.15 ,0.09, 0.18],
'Reflective Double Glazing 5p 6 mm TI on CLR 30%, CLR': [0.29, 0.28, 0.27, 0.25, 0.20, 0.12, 0.25],
'Low-e Double Glazing, e = 0.2 on surface 2 17a 3 mm LE CLR': [0.65, 0.64, 0.61, 0.56, 0.43, 0.23, 0.57],
'Low-e Double Glazing, e = 0.2 on surface 2 17b 6 mm LE CLR': [0.60, 0.59, 0.57, 0.51, 0.40, 0.21, 0.53],
'Low-e Double Glazing, e = 0.2 on surface 3 17c 3 mm CLR LE': [0.70, 0.68, 0.65, 0.59, 0.46, 0.24, 0.61],
'Low-e Double Glazing, e = 0.2 on surface 3 17d 6 mm CLR LE': [0.65, 0.63, 0.60, 0.54, 0.42, 0.21, 0.56],
'Low-e Double Glazing, e = 0.2 on surface 3 17e 3 mm BRZ LE': [0.57, 0.54, 0.51, 0.46, 0.35, 0.18, 0.48],
'Low-e Double Glazing, e = 0.2 on surface 3 17f 6 mm BRZ LE': [0.45, 0.42, 0.40, 0.35, 0.27, 0.14, 0.38],
'Low-e Double Glazing, e = 0.2 on surface 3 17g 3 mm GRN LE': [0.55, 0.52, 0.50, 0.44, 0.34, 0.17, 0.46],
'Low-e Double Glazing, e = 0.2 on surface 3 17h 6 mm GRN LE': [0.41, 0.39, 0.36, 0.32, 0.25, 0.13, 0.34],
'Low-e Double Glazing, e = 0.2 on surface 3 17i 3 mm GRY LE': [0.54, 0.51, 0.49, 0.44, 0.33, 0.17, 0.46],
'Low-e Double Glazing, e = 0.2 on surface 3 17j 6 mm GRY LE': [0.39, 0.37, 0.35, 0.31, 0.24, 0.13, 0.33],
'Low-e Double Glazing, e = 0.2 on surface 3 17k 6 mm BLUGRN LE ': [0.45 ,0.42 ,0.40 ,0.35 ,0.27 ,0.14 ,0.37],
'Low-e Double Glazing, e = 0.2 on surface 3 17l 6 mm HI-P GRN LE': [0.34, 0.31, 0.30, 0.26, 0.20, 0.11, 0.28],
'Low-e Double Glazing, e = 0.1 on surface 2 21a 3 mm LE CLR': [0.65, 0.64, 0.62, 0.56, 0.43 ,0.23, 0.57],
'Low-e Double Glazing, e = 0.1 on surface 2 21b 6 mm LE CLR': [0.60, 0.59, 0.57, 0.51, 0.40 ,0.21, 0.53],
'Low-e Double Glazing, e = 0.1 on surface 3 21c 3 mm CLR LE': [0.60, 0.58, 0.56, 0.51, 0.40 ,0.22, 0.52],
'Low-e Double Glazing, e = 0.1 on surface 3 21d 6 mm CLR LE': [0.56, 0.55, 0.52, 0.48, 0.38 ,0.20, 0.49],
'Low-e Double Glazing, e = 0.1 on surface 3 21e 3 mm BRZ LE': [0.48, 0.46, 0.44, 0.40, 0.31 ,0.17, 0.42],
'Low-e Double Glazing, e = 0.1 on surface 3 21f 6 mm BRZ LE': [0.39, 0.37, 0.35, 0.31, 0.24 ,0.13, 0.33],
'Low-e Double Glazing, e = 0.1 on surface 3 21g 3 mm GRN LE': [0.46, 0.44, 0.42, 0.38, 0.30 ,0.16, 0.40],
'Low-e Double Glazing, e = 0.1 on surface 3 21h 6 mm GRN LE': [0.36, 0.33, 0.31, 0.28, 0.22 ,0.12, 0.30],
'Low-e Double Glazing, e = 0.1 on surface 3 21i 3 mm GRY LE': [0.46, 0.44, 0.42, 0.38, 0.30 ,0.16, 0.39],
'Low-e Double Glazing, e = 0.1 on surface 3 21j 6 mm GRY LE': [0.34, 0.32, 0.30, 0.27, 0.21 ,0.12, 0.28],
'Low-e Double Glazing, e = 0.1 on surface 3 21k 6 mm BLUGRN LE ':         [0.39, 0.37, 0.34, 0.31, 0.24, 0.13, 0.33],
'Low-e Double Glazing, e = 0.1 on surface 3 21l 6 mm HI-P GRN W/LE CLR':  [0.31, 0.30, 0.29, 0.26, 0.21, 0.12, 0.27],
'Low-e Double Glazing, e = 0.05 on surface 2 25a 3 mm LE CLR':             [0.41, 0.40, 0.38, 0.34, 0.27, 0.14, 0.36],
'Low-e Double Glazing, e = 0.05 on surface 2 25b 6 mm LE CLR':             [0.37, 0.36, 0.34, 0.31, 0.24, 0.13, 0.32],
'Low-e Double Glazing, e = 0.05 on surface 2 25c 6 mm BRZ W/LE CLR':       [0.26, 0.25, 0.24, 0.22, 0.18, 0.10, 0.23],
'Low-e Double Glazing, e = 0.05 on surface 2 25d 6 mm GRN W/LE CLR':       [0.31, 0.30, 0.28, 0.26, 0.21, 0.12, 0.27],
'Low-e Double Glazing, e = 0.05 on surface 2 25e 6 mm GRY W/LE CLR ':      [0.24, 0.23, 0.22, 0.20, 0.16, 0.09, 0.21],
'Low-e Double Glazing, e = 0.05 on surface 2 25f 6 mm BLUE W/LE CLR ':     [0.27, 0.26, 0.25, 0.23, 0.18, 0.11, 0.24],
'Low-e Double Glazing, e = 0.05 on surface 2 25g 6 mm HI-P GRN W/LE CLR ': [0.27, 0.26, 0.25, 0.23, 0.18, 0.11, 0.23],
'Triple Glazing 29a 3 mm CLR CLR CLR ':       [0.68, 0.65, 0.62, 0.54, 0.39, 0.18, 0.57],
'Triple Glazing 29b 6 mm CLR CLR CLR ':       [0.61, 0.58, 0.55, 0.48, 0.35, 0.16, 0.51],
'Triple Glazing 29c 6 mm HI-P GRN CLR CLR':   [0.32, 0.29, 0.27, 0.24, 0.18, 0.10, 0.26],
'Triple Glazing, e = 0.2 on surface 2 32a 3 mm LE CLR CLR ':        [0.60, 0.58, 0.55, 0.48, 0.35, 0.17, 0.51],
'Triple Glazing, e = 0.2 on surface 2 32b 6 mm LE CLR CLR ':        [0.53, 0.50, 0.47, 0.41, 0.29, 0.14, 0.44],
'Triple Glazing, e = 0.2 on surface 5 32c 3 mm CLR CLR LE ':        [0.62, 0.60, 0.57, 0.49, 0.36, 0.16, 0.52],
'Triple Glazing, e = 0.2 on surface 5 32d 6 mm CLR CLR LE ':        [0.56, 0.53, 0.50, 0.44, 0.32, 0.15, 0.47],
'Triple Glazing, e = 0.1 on surface 2 and 5 40a 3 mm LE CLR LE ':         [0.41, 0.39, 0.37, 0.32, 0.24, 0.12, 0.34],
'Triple Glazing, e = 0.1 on surface 2 and 5 40b 6 mm LE CLR LE ':         [0.36, 0.34, 0.32, 0.28, 0.21, 0.10, 0.30],
'Triple Glazing, e = 0.05 on surface 2 and 4 49 3 mm LE LE CLR':           [0.27, 0.25, 0.24, 0.21, 0.16, 0.08, 0.23],
'Triple Glazing, e = 0.05 on surface 2 and 4 50 6 mm LE LE CLR':           [0.26, 0.25, 0.23, 0.21, 0.16, 0.08, 0.22],
}
SHGC_list=list(SHGC.keys())
Qwbn = np.zeros(24)
Qwdn = np.zeros(24)

#UI (Wall)

st.divider()
st.subheader("Solid Wall")
column1, column2 = st.columns(2)

if "area_of_wallNO3" not in st.session_state:
    st.session_state["area_of_wallNO3"] = 0
area_of_wallNO3 = column1.number_input(f"The area of the wall  {st.session_state.area}", value=float(st.session_state["area_of_wallNO3"]))
st.session_state.area_of_wallNO3 = area_of_wallNO3

if "Ufactor_wallNO3" not in st.session_state:
    st.session_state["Ufactor_wallNO3"] = 0
Ufactor_wallNO3 = column1.number_input(f" The overall heat transfer coefficient {st.session_state.U}", value=float(st.session_state["Ufactor_wallNO3"]),format="%.4f")
st.session_state.Ufactor_wallNO3 = Ufactor_wallNO3

if "Surface_colorNO3" not in st.session_state:
    st.session_state["Surface_colorNO3"] = "Light Colored Surface"
Surface_colorNO3 = column2.selectbox("Surface Color",surface_color,
                                  index=surface_color.index(st.session_state["Surface_colorNO3"]))
st.session_state.Surface_colorNO3 = Surface_colorNO3

if "irr_or_sol" not in st.session_state:
    st.session_state["irr_or_sol"] = "Calculate Tsol using irridation"
irr_or_sol = column2.selectbox("use irridation or Tsol",("Calculate Tsol using irridation","Enter Tsol values manually"),
                                  index=("Calculate Tsol using irridation","Enter Tsol values manually").index(st.session_state["irr_or_sol"]))
st.session_state.irr_or_sol = irr_or_sol

if "convection_fraction_wallNO3" not in st.session_state:
    st.session_state["convection_fraction_wallNO3"] = 0.54
convection_fraction_wallNO3 = column1.number_input(f"the fraction of convection for the wall",
                                                value=float(st.session_state["convection_fraction_wallNO3"]))
st.session_state.convection_fraction_wallNO3 = convection_fraction_wallNO3

if "wall_typeNO3" not in st.session_state:
    st.session_state["wall_typeNO3"] = "wall number 1 (Curtain walls)"
wall_typeNO3 = column2.selectbox("Type of wall", all,index=all.index(st.session_state["wall_typeNO3"]))
st.session_state.wall_typeNO3 = wall_typeNO3


if "gammaaNO3" not in st.session_state:
    st.session_state["gammaaNO3"] = 0
gammaaNO3 = column1.number_input(f"Wall Azimuth (Orientation of wall )", value=float(st.session_state["gammaaNO3"]))
st.session_state.gammaaNO3 = gammaaNO3



#Irridation Calcuations
LST = np.arange(1,25)
AST = np.full(24,LST+ET/60 +(LSM-Longitude)/15)
H = np.full(24,15*(AST-12))
Latitude = np.full(24,Latitude)
beta = np.arcsin(np.cos(np.radians(Latitude))*np.cos(np.radians(delta))*np.cos(np.radians(H)) + np.sin(np.radians(Latitude))*np.sin(np.radians(delta)))
phi =  np.arccos((np.sin((beta))*np.sin(np.radians(Latitude)) - np.sin(np.radians(delta)))/( np.cos(beta)* np.cos(np.radians(Latitude))))
phi[0:12]=-phi[0:12]
g = abs(np.degrees(phi)-gammaaNO3)
incident_angle = np.arccos(np.cos(beta)* np.cos(np.radians(g)))
for e,i in enumerate(beta):
    if np.degrees(beta[e])<0:
        m[e]=None
    else:m[e] = 1/(np.sin(beta[e])+0.50572*((6.07995+(np.degrees(beta[e])))**(-1.6364)))
ab = 1.454-0.406 * st.session_state.taub - 0.268 * st.session_state.taud + 0.021*st.session_state.taud * st.session_state.taub
Eb = Solar_const * np.exp(-taub*(m**ab))
ED = Eb*np.cos(incident_angle)
for i in range(len(ED)):
    if ED[i]<0:
        ED[i]=0
ad = 0.507 + 0.205 * taub - 0.080 * taud - 0.190 * taub*taud
Ed= Solar_const * np.exp(-taud*(m**ad))
for i,e in enumerate(incident_angle):
    if np.cos(e)>-0.2:
        Y[i]=0.55+0.437*np.cos(e)+0.313*(np.cos(e)**2)
    else:Y[i]=0.45
Etd = Ed * Y
Er=1/2 * ground_reflectance* (Eb* np.sin(beta)+Ed)
Et = ED + Etd + Er

#Calculating Tsolair ()
c = st.columns(4)
if st.session_state.precise_DR == True:
    T_hourly = st.session_state.Temp24
else:
    T_hourly = T_design - percentage_of_daily_range * daily_range / 100
if st.session_state.irr_or_sol == "Calculate Tsol using irridation":
    for i in range(len(Et)):
        if np.isnan(Et[i]):
            Et[i] = 0
    if st.session_state.preferredscale == "Imperial system":
        if Surface_colorNO3 == surface_color[0]:
            TsolairNO3 = T_hourly + Et * 0.15
        if Surface_colorNO3 == surface_color[1]:
            TsolairNO3 = T_hourly + Et * 0.30
    else:
        if Surface_colorNO3 == surface_color[0]:
            TsolairNO3 = T_hourly + Et * 0.02655
        if Surface_colorNO3 == surface_color[1]:
            TsolairNO3 = T_hourly + Et * 0.05310

elif st.session_state.irr_or_sol == "Enter Tsol values manually":
    if "TsolairNO3" not in st.session_state:
        st.session_state.TsolairNO3 = np.zeros(24)
    for i, e in enumerate(range(24)):
        with c[i % 4]:
            st.session_state.TsolairNO3[i] = st.number_input(f"T sol air at time {i}", value=st.session_state.TsolairNO3[i])
            TsolairNO3 = st.session_state.TsolairNO3
st.session_state.TsolairNO3 = TsolairNO3
#calculating Q (for wall)
Qin = Ufactor_wallNO3 * area_of_wallNO3 * (TsolairNO3 - T_indoor)

for i, e in enumerate(Qn):
    Qn[i] = np.sum(np.array(CTS[walls.index(wall_typeNO3)]) * np.concatenate([Qin[i::-1],Qin[23:i:-1]])/100)
Qcn = convection_fraction_wallNO3 * Qn
for i, e in enumerate(Qrn):
    Qrn[i] = np.sum(np.array(RTS_NONSOLAR[construction_types_non_solar.index(st.session_state.construction_types_non_solar)])/100
                     * np.concatenate([Qn[i::-1], Qn[23:i:-1]]))*(1-convection_fraction_wallNO3)

Qwall = Qcn + Qrn
st.divider()

#UI (Window)
st.subheader("Window")
col1,col2 = st.columns(2)
if "area_of_WindowNO3" not in st.session_state:
    st.session_state["area_of_WindowNO3"] = 0
area_of_WindowNO3 = col1.number_input(f"The area of the Window {st.session_state.area}", value=float(st.session_state["area_of_WindowNO3"]))
st.session_state.area_of_WindowNO3 = area_of_WindowNO3

if "window_typeNO3" not in st.session_state:
    st.session_state["window_typeNO3"] = 'Uncoated Single Glazing 1a 3 mm CLR '
window_typeNO3 = col2.selectbox("Type of windows", SHGC_list,index=SHGC_list.index(st.session_state["window_typeNO3"]))
st.session_state.window_typeNO3 = window_typeNO3

if "Ufactor_windowNO3" not in st.session_state:
    st.session_state["Ufactor_windowNO3"] = 0
Ufactor_windowNO3 = col1.number_input(f" The overall heat transfer coefficient for the window {st.session_state.U}", value=float(st.session_state["Ufactor_windowNO3"]),format="%.4f")
st.session_state.Ufactor_windowNO3 = Ufactor_windowNO3

#Calculating Q (for window)
def interpolate_SHGC(angle,key):
    angles = (0.0,40.0,50.0,60.0,70.0,80.0)
    min_angle=0
    max_angle=0
    val=0
    for e,i in enumerate(angles):
        if angle>80 and angle<82:
            val = SHGC[key][5]
            smax=0
            smin=0
            max_angle=0
            min_angle=0
        elif angle>82:
            val =0
            smax=0
            smin=0
            max_angle=0
            min_angle=0
        elif angle>i:
            min_angle=i
            max_angle=angles[e+1]
            smax = SHGC[key][e+1]
            smin = SHGC[key][e]
            val=smin+((angle-min_angle)/(max_angle-min_angle))*(smax-smin)
    # print(val, smin,smax, min_angle,max_angle, angle)
    print(SHGC[key])
    return val
Qwcn = Ufactor_windowNO3 * area_of_WindowNO3 * (T_hourly- T_indoor)
for e,i in enumerate(Qwbn):
    print(e+1)
    Qwbn[e] = ED[e] * area_of_WindowNO3 * interpolate_SHGC(np.degrees(incident_angle[e]),window_typeNO3)
    print(ED[e],interpolate_SHGC(np.degrees(incident_angle[e]),window_typeNO3))
Qwdn =  (Er + Etd) * area_of_WindowNO3 * SHGC[window_typeNO3][6]

Qwcn = np.nan_to_num(Qwcn,nan=0.0)
Qwbn = np.nan_to_num(Qwbn,nan=0.0)
Qwdn = np.nan_to_num(Qwdn,nan=0.0)

#Graphing
st.divider()
st.subheader("Graphs and Tables")

datawindow = pd.DataFrame({
    f"Q Window Conduction  {st.session_state.heat}":Qwcn,
    f"Q Window Direct Beam heat gain {st.session_state.heat}":Qwbn,
    f"Q Window Diffuse heat gain {st.session_state.heat}":Qwdn,
    f"Total Window heat gain {st.session_state.heat}":Qwcn + Qwbn + Qwdn,
})
datawindow.index =datawindow.index+1

Temps = pd.DataFrame({
    f"T hourly {st.session_state.temp}":T_hourly,
    f"Tsol {st.session_state.temp}": TsolairNO3,
})
Temps.index = Temps.index + 1

Qs = pd.DataFrame({
    f"Q convection {st.session_state.heat}":Qcn,
    f"Q Radiation {st.session_state.heat}":Qrn,
    f"Q total {st.session_state.heat}": Qwall,
})
Qs.index = Qs.index +1

data=pd.DataFrame({
    "Apparent Solar Time (h)":AST,
    "Hour Angle (°)":H,
    "Solar Altitude (°)": np.degrees(beta) ,
    "Solar Azimuth (°)":np.degrees(phi),
    "solar Air Mass":m,
    f"Normal Beam irridiation {st.session_state.irridation}" : Eb,
    "Surface Incidence Angle" : np.degrees(incident_angle),
    f"Surface Beam Irridiation  {st.session_state.irridation}" : ED,
    f"Diffuse Solar Heat Gain  {st.session_state.irridation}" : Ed,
    f"Ground Diffuse  {st.session_state.irridation}" : Er,
    "Y ratio" : Y,
    f"Sky Diffuse  {st.session_state.irridation}" : Etd,
    f"Diffused Total {st.session_state.irridation}" : Er + Etd,
    f"Total Surface irradiation  {st.session_state.irridation}" : Et
})
data.index = data.index +1
total =  Qcn + Qrn + Qwcn + Qwbn + Qwdn

total_room = pd.DataFrame({
    f"Total cooling load from wall {st.session_state.heat} " :total
})
total_room.index = total_room.index+1

st.subheader("Hourly and Solair Temperatures")
st.line_chart(data=Temps,x_label="Time (h)",y_label=f"Temperature {st.session_state.temp}",)
st.subheader("Solar irradiation on wall")
st.write(data)
st.subheader("cooling load from wall")
st.write(Qs)
st.line_chart(data=Qs,x_label="Time (h)",y_label=f"Load {st.session_state.heat}",)

st.subheader("Heat gain from window")
st.write(datawindow)
st.line_chart(data=datawindow,x_label="Time (h)",y_label=f"Load {st.session_state.heat}",)

st.subheader("Total Cooling Load Wall #3")
st.line_chart(data=total_room,x_label="Time (h)",y_label=f"Load {st.session_state.heat}",)


st.session_state["totalNO3"]=total_room
st.session_state["datatempNO3"] = Temps
st.session_state["datadataNO3"] = data
st.session_state["dataqaNO3"] = Qs
st.session_state["dataWNO3"] = datawindow