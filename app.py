import streamlit as st
import pandas as pd
import plotly.express as px

# Leer los datos
car_data = pd.read_csv('vehicles_us.csv')

# Encabezado de la aplicación
st.header("Visualización de Datos de Vehículos")

# Casilla de verificación para mostrar el histograma
show_histogram = st.checkbox('Mostrar Histograma')

if show_histogram:
    fig_hist = px.histogram(car_data, x="odometer", title="Histograma de Odometer")
    st.write("Histograma de la variable 'odometer':")
    st.plotly_chart(fig_hist)

# Casilla de verificación para mostrar el gráfico de dispersión
show_scatter = st.checkbox('Mostrar Gráfico de Dispersión')

if show_scatter:
    fig_scatter = px.scatter(car_data, x="odometer", y="price", title="Gráfico de Dispersión: Odometer vs. Price")
    st.write("Gráfico de dispersión entre 'odometer' y 'price':")
    st.plotly_chart(fig_scatter)