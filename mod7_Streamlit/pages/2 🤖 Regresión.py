import streamlit as st
import joblib
import seaborn as sns
import pandas as pd

@st.cache_resource
def load_scikit_model():
    return joblib.load('models/pipeline_regresion.joblib')

st.set_page_config(
    page_title='Predicción de Precio de Diamantes', 
    page_icon=':gem:'
)


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
            color: black !important;
            border-radius: 10px !important;
            border: 1px solid white !important;
        }

        /* Cambia el color de los botones al pasar el mouse */
        div.stButton > button:hover {
            background-color: #FF8C00 !important;
            color: black !important;
        }
        
        # /*  Aplicar estilo al botón de st.form_submit_button */
        # [data-testid="stFormSubmitButton"] {
        #     background-color: #FFA500 !important;
        #     color: white !important;
        #     border-radius: 10px !important;
        #     border: 1px solid white !important;
        #     font-weight: bold !important;
        #     padding: 8px 15px !important;
        # }

        # /* Cambia color al pasar el mouse */
        # [data-testid="stFormSubmitButton"]:hover {
        #     background-color: #FF8C00 !important;
        #     color: black !important;
        # }
        
    </style>
    """,
    unsafe_allow_html=True
)

# Colocar los botones en la parte superior derecha Para navegar entre las páginas
col1, col2, col3 = st.columns([7, 5, 5])
with col2:
    if st.button("⬅ Anterior"):
        st.switch_page("pages/1 📊 EDAs.py")
with col3:
    if st.button("➡ Siguiente"):
        st.switch_page("pages/3 🤖 Clasificación.py")


st.title('Predicción de Precio de Diamantes')

model = load_scikit_model()

st.write('Ejemplo de los datos')
df = sns.load_dataset('diamonds')
price_mean = df['price'].mean()  # Precio medio de los diamantes

st.table(df.head())

# Formulario para predicción
st.header('Introduce datos para la predicción')

with st.form("diamonds_form"):
    carat = st.number_input(
        'Introduce el peso en quilates (carat)', 
        min_value=0.1, max_value=5.0, 
        value=df['carat'].mean(), 
        step=0.01
    )
    cut = st.selectbox('Introduce la calidad del corte (cut)', df['cut'].unique())
    color = st.selectbox('Introduce el color (color)', df['color'].unique())
    clarity = st.selectbox('Introduce la claridad (clarity)', df['clarity'].unique())
    depth = st.number_input(
        'Introduce la profundidad porcentual (depth)',
        min_value=40.0, max_value=80.0,
        value=df['depth'].mean(),
        step=0.1
    )
    table = st.number_input(
        'Introduce el ancho de la tabla en porcentaje (table)',
        min_value=40.0, max_value=100.0,
        value=df['table'].mean(),
        step=0.1
    )
    x = st.number_input('Introduce la longitud en mm (x)', min_value=0.1, max_value=10.0, value=df['x'].mean(), step=0.1)
    y = st.number_input('Introduce el ancho en mm (y)', min_value=0.1, max_value=10.0, value=df['y'].mean(), step=0.1)
    z = st.number_input('Introduce la profundidad en mm (z)', min_value=0.1, max_value=10.0, value=df['z'].mean(), step=0.1)
    
    boton_enviar = st.form_submit_button("Generar predicción")

    if boton_enviar:
        X_new = pd.DataFrame({
            'carat': [carat],
            'cut': [cut],
            'color': [color],
            'clarity': [clarity],
            'depth': [depth],
            'table': [table],
            'x': [x],
            'y': [y],
            'z': [z]
        })
        
        prediccion = model.predict(X_new)[0]
        delta_value = prediccion - price_mean
        
        col1, col2 = st.columns(2)
        col1.metric('Precio estimado (predicción)', value=f'{prediccion:.2f} $', delta=f'{delta_value:.2f} $')
        col2.metric('Precio medio', value=f'{price_mean:.2f} $')

    
    