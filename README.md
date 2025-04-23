# TripleTen
Repositorio creado para el Sprint de TripleTen

# Visualización de Datos de Vehículos

## Descripción del Proyecto

Esta es una aplicación web interactiva creada con **Streamlit** que permite visualizar los datos de vehículos. Los datos son extraídos de un archivo CSV (`vehicles_us.csv`) que contiene información sobre los vehículos, como el kilometraje (`odometer`) y el precio de los mismos (`price`).

La aplicación proporciona dos tipos de visualización:

1. **Histograma**: Muestra la distribución de los valores de `odometer` (kilometraje de los vehículos) mediante un histograma interactivo.
2. **Gráfico de Dispersión**: Muestra una relación entre el `odometer` y el `price` (precio de los vehículos) a través de un gráfico de dispersión interactivo.

Los usuarios pueden seleccionar qué gráficos desean visualizar utilizando casillas de verificación.

## Funcionalidades

- **Mostrar Histograma**: Al seleccionar esta opción, se genera un histograma de la columna `odometer`, mostrando la distribución de los kilometrajes de los vehículos.
- **Mostrar Gráfico de Dispersión**: Al seleccionar esta opción, se genera un gráfico de dispersión que muestra la relación entre el kilometraje (`odometer`) y el precio (`price`) de los vehículos.

## Requisitos

Para ejecutar este proyecto en tu máquina local, necesitas tener instalado lo siguiente:

- **Python 3.x**
- **Streamlit**
- **Plotly**
- **Pandas**

## Instalación

Para instalar las dependencias necesarias, ejecuta el siguiente comando:

```bash
pip install streamlit plotly pandas