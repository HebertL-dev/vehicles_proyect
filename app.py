import pandas as pd 
import streamlit as st 
import plotly.express as px 
car_data = pd.read_csv('vehicles_us.csv')
hist_button = st.button('Construir Histograma')
dispersion_button = st.button('Construir Diagrama de dispersion')

if hist_button: # al hacer clic en el botón
    # escribir un mensaje
    st.write('Creación de un histograma para el conjunto de datos de anuncios de venta de coches')
    # crear un histograma
    fig = px.histogram(car_data, x="odometer")
    # mostrar un gráfico Plotly interactivo
    st.plotly_chart(fig, use_container_width=True)
    
if dispersion_button:
    #write a message
    st.write('Creacion de un Diagrama de Dispersion para el conjunto de datos de anuncios de venta de coches')
    fig0 = px.scatter(car_data, x="odometer", y="price") # crear un gráfico de dispersión
    #mostrar un grafico Plotly interactivo
    st.plotly_chart(fig0, use_container_width=True)
    