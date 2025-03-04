import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px

# Aplicar estilos globales con CSS
st.markdown(
    """
    <style>
        /* Cambia el fondo de toda la aplicación */
        .stApp {
            background-color: #2E2E2E !important;  /* Color gris oscuro suave */
        }

        /* Cambia el fondo de la barra lateral */
        [data-testid="stSidebar"] {
            background-color: #383838 !important;  /* Gris más claro para la barra lateral */
        }

        /* Cambia el color del texto en la aplicación */
        html, body, .stTextInput, .stSelectbox, .stSlider, .stButton {
            color: white !important;
        }

        /* Cambia el color de los títulos */
        h1, h2, h3 {
            color: #FFA500 !important; /* Naranja */
        }

        /* Cambia el color de los botones */
        div.stButton > button {
            background-color: #FFA500 !important;
            color: white !important;
            color: black !important;
            border-radius: 10px !important;
            border: 1px solid white !important;
        }

        /* Cambia el color de los botones al pasar el mouse */
        div.stButton > button:hover {
            background-color: #FF8C00 !important;
            color: black !important;
        }
        
        /* 🔹 Estiliza los botones de descarga */
        div.stDownloadButton > button {
            background-color: #FFA500 !important;
            color: black !important;
            border-radius: 10px !important;
            border: 1px solid white !important;
            padding: 8px 15px !important;
            font-size: 14px !important;
            font-weight: bold !important;
        }

        /* 🔹 Cambia el color de los botones de descarga al pasar el mouse */
        div.stDownloadButton > button:hover {
            background-color: #FF8C00 !important;
            color: black !important;
        }
        
    </style>
    """,
    unsafe_allow_html=True
)

# Carga de datos
@st.cache_data
def load_data():
    df = sns.load_dataset('diamonds')
    return df

df_original = load_data()
df = df_original.copy()

# Colocar los botones en la parte superior derecha Para navegar entre las páginas
col1, col2, col3 = st.columns([7, 5, 5])
with col2:
    if st.button("⬅ Anterior"):
        st.switch_page("Home.py")
with col3:
    if st.button("➡ Siguiente"):
        st.switch_page("pages/2 🤖 Regresión.py")


st.title('Análisis Exploratorio de Datos (EDA) - Diamonds')
st.dataframe(df.head())

# Filtros Globales
st.header('Filtros Globales')

# Filtros categóricos
cut_options = df['cut'].unique().tolist()
selected_cut = st.multiselect('Corte', options=cut_options, default=cut_options)

color_options = df['color'].unique().tolist()
selected_color = st.multiselect('Color', options=color_options, default=color_options)

clarity_options = df['clarity'].unique().tolist()
selected_clarity = st.multiselect('Claridad', options=clarity_options, default=clarity_options)

# Filtro numérico de precio
price_min, price_max = st.slider('Rango de Precio',
                                 min_value=int(df['price'].min()),
                                 max_value=int(df['price'].max()),
                                 value=(int(df['price'].min()), int(df['price'].max())))

# Aplicar filtros
df = df[df['cut'].isin(selected_cut)]
df = df[df['color'].isin(selected_color)]
df = df[df['clarity'].isin(selected_clarity)]
df = df[df['price'].between(price_min, price_max)]

# Análisis Univariante
st.header('Análisis Univariante')

# Histograma de precios
fig, ax = plt.subplots(figsize=(6, 4))
sns.histplot(df['price'], bins=30, kde=True, ax=ax, color='skyblue')
ax.set_title('Distribución de Precios')
st.pyplot(fig)

# Boxplot de carat
fig, ax = plt.subplots(figsize=(6, 4))
sns.boxplot(x=df['carat'], ax=ax)
ax.set_title('Boxplot de Carat')
st.pyplot(fig)

# Countplot de cortes
fig, ax = plt.subplots(figsize=(6, 4))
sns.countplot(x=df['cut'], order=df['cut'].value_counts().index, ax=ax, palette='viridis')
ax.set_title('Distribución de Corte')
st.pyplot(fig)

# Análisis Bivariante
st.header('Análisis Bivariante')

# Scatterplot carat vs price
fig = px.scatter(df, x='carat', y='price', color='cut', title='Carat vs Price')
st.plotly_chart(fig)

# Boxplot precio por color
fig, ax = plt.subplots(figsize=(6, 4))
sns.boxplot(x='color', y='price', data=df, ax=ax, palette='coolwarm')
ax.set_title('Precio por Color')
st.pyplot(fig)

# Análisis Multivariante
st.header('Análisis Multivariante')

# Heatmap de correlación con solo columnas numéricas
st.subheader("Matriz de Correlación")
numeric_df = df.select_dtypes(include=['number'])
fig, ax = plt.subplots(figsize=(8, 6))
sns.heatmap(numeric_df.corr(), annot=True, cmap='coolwarm', ax=ax)
ax.set_title('Matriz de Correlación')
st.pyplot(fig)

# Pairplot
st.subheader("Pairplot de Variables Numéricas")
st.pyplot(sns.pairplot(numeric_df))

# Análisis de Valores Nulos y Tipos de Datos
st.header('Valores Nulos y Tipos de Datos')
st.write("Valores Nulos:")
st.dataframe(df.isnull().sum())

st.write("Valores Únicos por Columna:")
st.dataframe(df.nunique())

st.write("Tipos de Datos:")
st.dataframe(df.dtypes)

# Descargar datos filtrados
st.header('Descargar datos filtrados')
col1, col2 = st.columns(2)

with col1:
    st.download_button(
        label='Descargar datos originales',
        data=df_original.to_csv(index=False),
        file_name='diamonds.csv',
        mime='text/csv'
    )

with col2:
    st.download_button(
        label='Descargar datos filtrados',
        data=df.to_csv(index=False),
        file_name='diamonds_filtered.csv',
        mime='text/csv'
    )
