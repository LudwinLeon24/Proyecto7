import pandas as pd
import plotly.express as px
import streamlit as st

# Cargar los datos
file_path = "vehicles_us.csv"
car_data = pd.read_csv(file_path)

# Encabezado
st.header("Análisis de Ventas de Autos")

# Casilla de verificación para el gráfico de los modelos más vendidos
show_top5_models = st.checkbox("Mostrar Top 5 Modelos Más Vendidos")

if show_top5_models:
    st.write("Los 5 modelos más vendidos en el conjunto de datos")
    
    # Calcular los 5 modelos más vendidos
    top_5_models = car_data['model'].value_counts().nlargest(5)
    
    # Crear gráfico de barras
    fig = px.bar(x=top_5_models.index, y=top_5_models.values, 
                 labels={'x': 'Modelo', 'y': 'Cantidad de ventas'},
                 title="Top 5 Modelos Más Vendidos")
    
    # Mostrar gráfico en Streamlit
    st.plotly_chart(fig, use_container_width=True)

# Casilla de verificación para el histograma de precios
show_price_histogram = st.checkbox("Mostrar Distribución de Precios")

if show_price_histogram:
    st.write("Distribución de precios de los autos en venta")
    
    # Crear histograma de precios
    fig = px.histogram(car_data, x="price", nbins=50, 
                       labels={'price': 'Precio del Auto'},
                       title="Distribución de Precios de Autos")
    
    # Mostrar gráfico en Streamlit
    st.plotly_chart(fig, use_container_width=True)
