import numpy as np
import streamlit as st
import pandas as pd
st.title("Lights")
lighting_conv =np.zeros(24)
lighting_rad =np.zeros(24)
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
    "Heavy Interior zone no carpet",)# reused from ASHRE, without permission

column1, column2 = st.columns(2)  # until now the second coumn is empty

if "light_wattage" not in st.session_state:
    st.session_state["light_wattage"] = 0
light_wattage = column1.number_input(f" Lights wattage (W)", value=st.session_state["light_wattage"])
st.session_state.light_wattage = light_wattage

if "light_allowance" not in st.session_state:
    st.session_state["light_allowance"] = 0.0
light_allowance = column2.number_input(f" Lights Allowance Factor", value=float(st.session_state["light_allowance"]),format="%.2f",min_value=0.0,max_value=1.0)
st.session_state.light_allowance = light_allowance

if "lights_on" not in st.session_state:
    st.session_state["lights_on"] = 5
    st.session_state["lights_of"] = 17
light_range = st.slider(f"select the use factor",  min_value=0, max_value=23,
                        value=(st.session_state["lights_on"],st.session_state["lights_of"]))
st.session_state.lights_on,st.session_state.lights_off = light_range

lights_Wattage = np.full(24, light_wattage)
Speical_Allowace_factor = np.full(24, light_allowance)
lights_use_factor = np.zeros(24)

lights_use_factor[st.session_state["lights_on"]:st.session_state["lights_off"]] = 1
if st.session_state.preferredscale == "Metric system":
    Qn_hour = lights_Wattage * lights_use_factor * Speical_Allowace_factor
else: Qn_hour = lights_Wattage * lights_use_factor * Speical_Allowace_factor * 3.41

lighting_conv = 0.43 * Qn_hour
for i in range(24):
    lighting_rad[i]= np.sum(
        np.array(RTS_NONSOLAR[construction_types_non_solar.index(st.session_state.construction_types_non_solar)])/100
        * np.concatenate([Qn_hour[i+1::-1], Qn_hour[23:i+1:-1]])) * 0.57
# # concatrenate is quite important and it will be used allot it this code, it basically join two array so I joined
# the two cut arrays togother. im thankful that I wont be graded on the cleanness of the code... hell yeah
Qlighting = lighting_conv + lighting_rad


# in the example that used table 21, it assumed that the radiant portion is 67%... why??? TODO check this
Temps = pd.DataFrame({
    f"Q Convection {st.session_state.heat}":lighting_conv,
    f"Q Radiation {st.session_state.heat}" : lighting_rad,
    f"Q total {st.session_state.heat}": Qlighting
})
Temps.index = Temps.index +1
st.write(Temps)
st.line_chart(data=Temps,x_label="Time (h)",y_label=f"Load {st.session_state.heat}")
if "Qlighting" not in st.session_state:
    st.session_state["Qlighting"] = np.zeros(24)
st.session_state.Qlighting = Qlighting
st.session_state["datalight"] = Temps