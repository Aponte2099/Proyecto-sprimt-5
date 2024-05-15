# app.py
import pandas as pd
import plotly.express as px
import streamlit as st

# Leer los datos
car_data = pd.read_csv('vehicles_us.csv')

# Crear un botón para construir un histograma
hist_button = st.button('Construir histograma')

if hist_button:
    # Crear un histograma para la columna 'odometer'
    fig = px.histogram(car_data, x="odometer")
    st.plotly_chart(fig, use_container_width=True)

# Crear un botón para construir un gráfico de dispersión
scatter_button = st.button('Construir gráfico de dispersión')

if scatter_button:
    # Crear un gráfico de dispersión para las columnas 'odometer' y 'price'
    fig = px.scatter(car_data, x="odometer", y="price")
    st.plotly_chart(fig, use_container_width=True)






