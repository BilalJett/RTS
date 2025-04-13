import numpy as np
import streamlit as st
import pandas as pd
defualtuseless =pd.DataFrame()

for i in range(4):
    if f"totalNO{i+1}" not in st.session_state:
        st.session_state[f"totalNO{i+1}"] =defualtuseless
    if f"datatempNO{i+1}" not in st.session_state:
        st.session_state[f"datatempNO{i+1}"] =defualtuseless
    if f"datadataNO{i+1}" not in st.session_state:
        st.session_state[f"datadataNO{i+1}"] =defualtuseless
    if f"dataqaNO{i+1}" not in st.session_state:
        st.session_state[f"dataqaNO{i+1}"] =defualtuseless
    if f"dataWNO{i+1}" not in st.session_state:
        st.session_state[f"dataWNO{i+1}"] =defualtuseless
if "total_roomROOF" not in st.session_state:
    st.session_state["total_roomROOF"] = defualtuseless
if "datatempROOF" not in st.session_state:
    st.session_state["datatempROOF"] = defualtuseless
if "datadataROOF" not in st.session_state:
    st.session_state["datadataROOF"] = defualtuseless
if "dataqaROOF" not in st.session_state:
    st.session_state["dataqaROOF"] = defualtuseless
if "dataWROOF" not in st.session_state:
    st.session_state["dataWROOF"] = defualtuseless

if "datalight" not in st.session_state:
    st.session_state["datalight"] = defualtuseless


#Graphing
st.header("Graphs and Tables")
st.divider()
st.subheader("Tsol vs Thourly")

c1,c2 =st.columns(2)

with c1:
    st.markdown("Wall #1")
    st.line_chart(data=(st.session_state["datatempNO1"]))
    st.markdown("Wall #3")
    st.line_chart(data=(st.session_state["datatempNO3"]))
    st.markdown("Roof")
    st.line_chart(data=(st.session_state["datatempROOF"]))

with c2:
    st.markdown("Wall #2")
    st.line_chart(data=(st.session_state["datatempNO2"]))
    st.markdown("Wall #4")
    st.line_chart(data=(st.session_state["datatempNO4"]))

st.divider()

st.subheader("Solar angles and irradiation")

st.markdown("Wall #1")
st.write(st.session_state["datadataNO1"])

st.markdown("Wall #2")
st.write(st.session_state["datadataNO2"])

st.markdown("Wall #3")
st.write(st.session_state["datadataNO3"])

st.markdown("Wall #4")
st.write(st.session_state["datadataNO4"])

st.markdown("Roof")

st.divider()

st.subheader("Walls cooling load")

co1,co2 =st.columns(2)

with co1:
    st.markdown("Wall #1")
    st.line_chart(data=(st.session_state["dataqaNO1"]))
    st.markdown("Wall #3")
    st.line_chart(data=(st.session_state["dataqaNO2"]))
    st.markdown("Wall #1")
    st.write(st.session_state["dataqaNO1"])
    st.markdown("Wall #3")
    st.write(st.session_state["dataqaNO3"])
st.markdown("Roof")
st.line_chart(data=(st.session_state["dataqaROOF"]))
st.markdown("Roof")
st.write(st.session_state["dataqaROOF"])


with co2:
    st.markdown("Wall #2")
    st.line_chart(data=(st.session_state["dataqaNO3"]))
    st.markdown("Wall #4")
    st.line_chart(data=(st.session_state["dataqaNO4"]))
    st.markdown("Wall #2")
    st.write(st.session_state["dataqaNO2"])
    st.markdown("Wall #4")
    st.write(st.session_state["dataqaNO4"])

st.divider()

st.subheader("Windows cooling load")

col1,col2=st.columns(2)

with col1:
    st.markdown("Window #1")
    st.line_chart(data=(st.session_state["dataWNO1"]))
    st.markdown("Window #3")
    st.line_chart(data=(st.session_state["dataWNO3"]))
    st.markdown("Window #1")
    st.write(st.session_state["dataWNO1"])
    st.markdown("Window #3")
    st.write(st.session_state["dataWNO3"])

st.markdown("Roof")
st.line_chart(data=(st.session_state["dataWROOF"]))
st.markdown("Roof")
st.write(st.session_state["dataWROOF"])

with col2:
    st.markdown("Window #2")
    st.line_chart(data=(st.session_state["dataWNO2"]))
    st.markdown("Window #4")
    st.line_chart(data=(st.session_state["dataWNO4"]))
    st.markdown("Window #2")
    st.write(st.session_state["dataWNO2"])
    st.markdown("Window #4")
    st.write(st.session_state["dataWNO4"])

st.divider()

st.subheader("Walls and windows (total per wall) cooling load")

colu1,colu2=st.columns(2)

with colu1:
    st.markdown("Total #1")
    st.line_chart(data=(st.session_state["totalNO1"]))
    st.markdown("Total #3")
    st.line_chart(data=(st.session_state["totalNO3"]))
    st.markdown("Total #1")
    st.write(st.session_state["totalNO1"])
    st.markdown("Total #3")
    st.write(st.session_state["totalNO3"])
st.markdown("Roof")
st.line_chart(data=(st.session_state["total_roomROOF"]))
st.markdown("Roof")
st.write(st.session_state["total_roomROOF"])

with colu2:
    st.markdown("Total #2")
    st.line_chart(data=(st.session_state["totalNO2"]))
    st.markdown("Total #4")
    st.line_chart(data=(st.session_state["totalNO4"]))
    st.markdown("Total #2")
    st.write(st.session_state["totalNO2"])
    st.markdown("Total #4")
    st.write(st.session_state["totalNO4"])
try:
    st.title("Total Room cooling load")
    totaltotaltotal = (np.nan_to_num(st.session_state["totalNO1"],nan=0)+
              np.nan_to_num(st.session_state["totalNO2"],nan=0)+
              np.nan_to_num(st.session_state["totalNO3"],nan=0)+
              np.nan_to_num(st.session_state["totalNO4"],nan=0)+
              np.nan_to_num(st.session_state["total_roomROOF"],nan=0)+
              np.nan_to_num(st.session_state["datalight"],nan=0))
    totaltotaltotal = totaltotaltotal[:, 0]
    st.line_chart(data=totaltotaltotal,x_label="Time (h)",y_label=f"Load {st.session_state.heat}")
except:
        pass