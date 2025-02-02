import pandas as pd
import plotly.express as px
import streamlit as st
import os

# Obtener la ruta del archivo CSV
file_path = os.path.join(os.path.dirname(__file__), 'vehicles_us.csv')

# Leer los datos en un DataFrame
car_data = pd.read_csv(file_path)

# Crear un encabezado en la app
st.header("Análisis de datos de ventas de coches en EE.UU.")

# Agregar botones para generar gráficos
hist_button = st.button("Construir histograma")
scatter_button = st.button("Construir gráfico de dispersión")

# Agregar casillas de verificación como alternativa
show_histogram = st.checkbox("Mostrar histograma")
show_scatter = st.checkbox("Mostrar gráfico de dispersión")

# Generar el histograma si el botón o la casilla de verificación están activados
if hist_button or show_histogram:
    st.write("Histograma del odómetro de los coches en venta")
    fig = px.histogram(car_data, x="odometer")
    st.plotly_chart(fig, use_container_width=True)

# Generar el gráfico de dispersión si el botón o la casilla de verificación están activados
if scatter_button or show_scatter:
    st.write("Gráfico de dispersión: Relación entre odómetro y precio")
    fig = px.scatter(car_data, x="odometer", y="price", title="Odómetro vs Precio", opacity=0.5)
    st.plotly_chart(fig, use_container_width=True)

