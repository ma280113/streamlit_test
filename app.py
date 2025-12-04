import streamlit as st
import pandas as pd
import plotly.graph_objects as go  # Importación de plotly.graph_objects como go

st.header("Visualización de Datos de Vehículos")  # Encabezado de la aplicación

# Botón para construir el histograma
hist_button = st.button('Construir histograma')
if hist_button:
    # Escribir un mensaje en la aplicación
    st.write(
        'Creación de un histograma para el conjunto de datos de anuncios de venta de coches')

    # Crear un histograma utilizando plotly.graph_objects
    # Se crea una figura vacía y luego se añade un rastro de histograma
    fig = go.Figure(data=[go.Histogram(x=car_data['odometer'])])

    # Opcional: Puedes añadir un título al gráfico si lo deseas
    fig.update_layout(title_text='Distribución del Odómetro')

    # Mostrar el gráfico Plotly interactivo en la aplicación Streamlit
    # 'use_container_width=True' ajusta el ancho del gráfico al contenedor
    st.plotly_chart(fig, use_container_width=True)


# Botón para construir el diagrama de dispersión
disp_button = st.button('Construir diagrama de dispersión')
if disp_button:
    # Escribir un mensaje en la aplicación
    st.write('Creación de un diagrama de dispersión para el conjunto de datos de anuncios de venta de coches')

    # Crear un diagrama de dispersión utilizando plotly.graph_objects
    # Se crea una figura vacía y luego se añade un rastro de dispersión
    fig = go.Figure(data=go.Scatter(
        x=car_data['year'],
        y=car_data['price'],
        mode='markers'  # Modo de marcadores para el diagrama de dispersión
    ))

    # Opcional: Puedes añadir un título al gráfico si lo deseas
    fig.update_layout(title_text='Diagrama de Dispersión: Año vs Precio')

    # Mostrar el gráfico Plotly interactivo en la aplicación Streamlit
    st.plotly_chart(fig, use_container_width=True)
