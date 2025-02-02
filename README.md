# 🚗 Análisis de Datos de Ventas de Coches en EE.UU.

## 📌 Descripción del Proyecto
Esta es una aplicación web interactiva creada con **Streamlit** que permite visualizar datos sobre anuncios de venta de coches en Estados Unidos. La aplicación carga un archivo CSV con información sobre los vehículos y genera gráficos interactivos para su análisis.

## 🛠 Funcionalidades
- **Histograma del odómetro**: Permite visualizar la distribución de los kilómetros recorridos por los coches en venta.
- **Gráfico de dispersión**: Muestra la relación entre el precio y el odómetro de los coches.
- **Interfaz interactiva**: Se pueden generar los gráficos a través de botones o casillas de verificación.

## 🚀 Cómo Ejecutar
1. Asegúrate de tener Python instalado y las dependencias necesarias:
   ```bash
   pip install streamlit pandas plotly
   ```
2. Clona este repositorio o descarga los archivos.
3. Ejecuta el siguiente comando en la terminal desde la carpeta del proyecto:
   ```bash
   streamlit run app.py
   ```
4. La aplicación se abrirá automáticamente en el navegador.

## 📂 Estructura del Proyecto
```
my_project_s_7/
│── .streamlit/           # Configuración de Streamlit
│── app.py                # Código principal de la aplicación
│── vehicles_us.csv       # Conjunto de datos utilizado
│── requirements.txt      # Dependencias necesarias
│── README.md             # Descripción del proyecto
│── notebooks/            # Análisis exploratorio previo en Jupyter Notebook
```

## 📊 Tecnologías Utilizadas
- **Python** 🐍
- **Streamlit** para la interfaz web 🖥
- **Plotly Express** para visualización 📈
- **Pandas** para manipulación de datos 🗂

## 🤝 Contribuciones
¡Las contribuciones son bienvenidas! Si tienes ideas para mejorar la aplicación, no dudes en abrir un *issue* o hacer un *pull request*.

---
**Desarrollado por:** Noe Álvarez 🚀
