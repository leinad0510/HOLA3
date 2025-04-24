import streamlit as st
import pandas as pd 
import matplotlib.pyplot as plt 
import seaborn as sns 

datos = pd.read_csv("datos_taller2.csv")
datos["Fecha"]  = pd.to_datetime(datos["Fecha"])
st.title("Gráficos de análisis macroeconómico")


fig, ax = plt.subplots(2, 2, figsize = (15,10))

ax[0,0].set_title("PIB real (trimestral) En miles de millones COP", fontsize = 15, color = "blue")
ax[0,1].set_title("Tasa política monetaria (anual) %", fontsize = 15, color = "blue")
ax[1,0].set_title("Tasa desempleo nacional (mensual) %", fontsize = 15, color = "blue")
ax[1,1].set_title("Tasa inflación (anual) %", fontsize = 15, color = "blue")

ax[0,0].plot(datos.set_index("Fecha")["PIB real (trimestral)"].dropna())#.plot()
ax[0,1].plot(datos.set_index("Fecha")["Tasa política monetaria (anual)"].dropna())
ax[1,0].plot(datos.set_index("Fecha")["Tasa desempleo nacional (mensual)"].dropna())
ax[1,1].plot(datos.set_index("Fecha")["Tasa inflación (anual)"].dropna())

st.pyplot(fig)

