import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, PageBreak,Image,HRFlowable
from reportlab.lib.pagesizes import A4
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet,ParagraphStyle
from reportlab.lib.enums import TA_CENTER, TA_LEFT
from reportlab.lib.colors import black, HexColor
import os
import tempfile

#importing data
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

#setting some functions
def PandasToTable(dataframe):
    styles = getSampleStyleSheet()
    style = styles["BodyText"]
    style.fontSize = 8
    table_data = []
    table_data.append([Paragraph(str(col), style) for col in dataframe.columns])
    for _, row in dataframe.iterrows():
        table_data.append([Paragraph(str(cell), style) for cell in row])
    return table_data
def PandasToGraph(dataframe,title,x,y):
    plt.figure(figsize=(6, 4))
    plt.xlabel(x)
    plt.ylabel(y)
    plt.xlim([1,24])
    plt.plot(dataframe, marker='o',label=dataframe.columns.tolist())
    plt.title(title)
    plt.grid(True)
    plt.tight_layout()
    plt.legend(fontsize=8)
    chart_path = f"{title}.png"
    plt.savefig(chart_path)
    plt.close()
    return chart_path
def WallInfoTable(num):
    data = {
        "Wall area": str(st.session_state[f"area_of_wallNO{num}"]) + st.session_state.area,
        "Overall heat transfer coefficient": str(st.session_state[f"Ufactor_wallNO{num}"]) + st.session_state.U,
        "Surface color": str(st.session_state[f"Surface_colorNO{num}"]),
        "Wall azimuth": str(st.session_state[f"gammaaNO{num}"]) + "°",
        "Type of wall": str(st.session_state[f"wall_typeNO{num}"])
    }
    table_data = [["Property", "Value"]] + [[k, v] for k, v in data.items()]
    return table_data

def RoofInfoTable():
    data = {
        "Roof area": str(st.session_state[f"area_of_wallROOF"]) + st.session_state.area,
        "Overall heat transfer coefficient": str(st.session_state[f"Ufactor_wallROOF"]) + st.session_state.U,
        "Surface color": str(st.session_state[f"Surface_colorROOF"]),
        "Type of wall": str(st.session_state[f"wall_typeROOF"])
    }
    table_data = [["Property", "Value"]] + [[k, v] for k, v in data.items()]
    return table_data

temp_pdf = tempfile.NamedTemporaryFile(delete=False, suffix=".pdf")
file_name = temp_pdf.name
doc = SimpleDocTemplate(file_name, pagesize=A4, leftMargin=70, rightMargin=70, topMargin=60, bottomMargin=50)
styles = getSampleStyleSheet()
stlye_of_table = [
    ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor('#4A90E2')),
    ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
    ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
    ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
    ('FONTSIZE', (0, 0), (-1, 0), 12),
    ('BOTTOMPADDING', (0, 0), (-1, 0), 8),
    ('BACKGROUND', (0, 1), (-1, -1), colors.HexColor("#F5F7FA")),
    ('GRID', (0, 0), (-1, -1), 0.1, colors.blue),
]
title_style = ParagraphStyle(
    name='Title',
    fontName='Helvetica-Bold',
    fontSize=22,
    leading=26,
    alignment=TA_CENTER,
    textColor=black,
    spaceAfter=12
)
header_style = ParagraphStyle(
    name='Header',
    fontName='Helvetica-Bold',
    fontSize=14,
    leading=18,
    textColor=HexColor("#1F497D"),
    spaceBefore=12,
    spaceAfter=6
)
body_style = ParagraphStyle(
    name='BodyText',
    fontName='Helvetica',
    fontSize=10.5,
    leading=14,
    alignment=TA_LEFT,
    spaceAfter=8
)
caption_style = ParagraphStyle(
    name='Caption',
    fontName='Helvetica-Oblique',
    fontSize=8,
    leading=10,
    textColor=HexColor("#888888"),
    alignment=TA_LEFT,
    spaceAfter=4
)
row_heights = [80] + [15] * 24

layout = [
    Paragraph("Cooling Load Calculation Using RTSM",styles["Title"]),
    Spacer(1,12),
    Paragraph(f"This report shows the cooling loads for a room that is located at a Latitude of {st.session_state.Latitude} ° and a Longitude of {st.session_state.Longitude}°"
              f",having a solar declination angle of {st.session_state.delta} °, with a solar constant equal to {st.session_state.Solar_const} {st.session_state.irridation}"),
    Paragraph("It does the Calculations based on the ASHRAE's approach on the Radiant Time Series Method by splitting the loads to convection load and radiation"
              " loads, then processing them sepeartly by accounting for the last 24 hours heat gains and applying the appropiate coefficients based on things like the consrcution level."),
    Spacer(10,12),
    Paragraph("add more text here later "),
    PageBreak(),
    Paragraph("Cooling Load Calculation Using RTSM", styles["Title"]),
]

def Addwalltopdf(num):
    layout.append(Paragraph(f"Wall #{num}", title_style))
    layout.append(HRFlowable(width="100%", thickness=1, color="black", spaceBefore=10, spaceAfter=10))
    layout.append(Spacer(1, 12))
    layout.append(Paragraph(f"Solar Angles and Radiation on Wall #{num}", header_style))
    layout.append(Table(PandasToTable(st.session_state[f"datadataNO{num}"].round(2)), colWidths=40, rowHeights=row_heights,
                        style=stlye_of_table))
    layout.append(Spacer(1, 12))
    layout.append(Table(WallInfoTable(num), style=stlye_of_table, rowHeights=20))
    layout.append(HRFlowable(width="100%", thickness=1, color="black", spaceBefore=5, spaceAfter=5))
    layout.append(PageBreak())
    layout.append(Paragraph(f"Wall #{num}", title_style))
    layout.append(HRFlowable(width="100%", thickness=1, color="black", spaceBefore=10, spaceAfter=10))
    layout.append(
        Image(PandasToGraph(st.session_state[f"datatempNO1"], "T Hourly and T Solair", "Time", "Temperature"), width=350,
              height=250))
    layout.append(Image(
        PandasToGraph(st.session_state[f"dataqaNO{num}"], "Cooling load from wall", "Time", f"load {st.session_state.heat}"),
        width=350, height=250))
    layout.append(Spacer(10, 70))
    layout.append(HRFlowable(width="100%", thickness=1, color="black", spaceBefore=10, spaceAfter=10))
    layout.append(PageBreak())
    layout.append(Paragraph(f"Wall #{num}", title_style))
    layout.append(HRFlowable(width="100%", thickness=1, color="black", spaceBefore=10, spaceAfter=10))
    layout.append(Image(
        PandasToGraph(st.session_state[f"dataWNO{num}"], "Cooling load from window", "Time", f"load {st.session_state.heat}"),
        width=350, height=250))
    layout.append(Image(PandasToGraph(st.session_state[f"totalNO{num}"], f"Total cooling load from wall #{num}", "Time",
                                      f"load {st.session_state.heat}"), width=350, height=250))
    layout.append(Spacer(10, 70))
    layout.append(HRFlowable(width="100%", thickness=1, color="black", spaceBefore=10, spaceAfter=10))
    layout.append(PageBreak())
def addrooftopdf():
    layout.append(Paragraph("Roof", title_style))
    layout.append(HRFlowable(width="100%", thickness=1, color="black", spaceBefore=10, spaceAfter=10))
    layout.append(Spacer(1, 12))
    layout.append(Paragraph("Solar Angles and Radiation on roof", header_style))
    layout.append(Table(PandasToTable(st.session_state[f"datadataROOF"].round(2)), colWidths=40, rowHeights=row_heights,
                        style=stlye_of_table))
    print("passed")
    layout.append(Spacer(1, 12))
    layout.append(Table(RoofInfoTable(), style=stlye_of_table, rowHeights=20))
    layout.append(HRFlowable(width="100%", thickness=1, color="black", spaceBefore=5, spaceAfter=5))
    layout.append(PageBreak())
    layout.append(Paragraph("Roof", title_style))
    layout.append(HRFlowable(width="100%", thickness=1, color="black", spaceBefore=10, spaceAfter=10))
    layout.append(
        Image(PandasToGraph(st.session_state["datatempROOF"], "T Hourly and T Solair", "Time", "Temperature"),
              width=350,
              height=250))
    layout.append(Image(
        PandasToGraph(st.session_state["dataqaROOF"], "Cooling load from Roof", "Time",
                      f"load {st.session_state.heat}"),
        width=350, height=250))
    layout.append(Spacer(10, 70))
    layout.append(HRFlowable(width="100%", thickness=1, color="black", spaceBefore=10, spaceAfter=10))
    layout.append(PageBreak())
    layout.append(Paragraph("Roof", title_style))
    layout.append(HRFlowable(width="100%", thickness=1, color="black", spaceBefore=10, spaceAfter=10))
    layout.append(Image(
        PandasToGraph(st.session_state["dataWROOF"], "Cooling load from window", "Time",
                      f"load {st.session_state.heat}"),
        width=350, height=250))
    layout.append(Image(PandasToGraph(st.session_state["total_roomROOF"], f"Total cooling load from Roof", "Time",
                                      f"load {st.session_state.heat}"), width=350, height=250))
    layout.append(Spacer(10, 70))
    layout.append(HRFlowable(width="100%", thickness=1, color="black", spaceBefore=10, spaceAfter=10))
    layout.append(PageBreak())

try:
    Addwalltopdf(1)
    Addwalltopdf(2)
    Addwalltopdf(3)
    Addwalltopdf(4)
    addrooftopdf()
    doc.build(layout)
    with open(file_name, "rb") as f:
        st.download_button(
            label="Download PDF Report",
            data=f,
            file_name="Cooling_Load_Report.pdf",
            mime="application/pdf"
        )
except:st.write("Failed to make pdf report, Make sure you filled all the info in the previous page\n if you intend to leave some pages blank then just visit the page then leave it.")
