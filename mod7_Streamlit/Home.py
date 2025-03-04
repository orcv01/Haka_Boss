import streamlit as st

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
    </style>
    """,
    unsafe_allow_html=True
)

# Título de la aplicación
st.title('Predicción del Precio y Calidad del Corte de Diamantes')

# Colocar los botones en la parte superior derecha
col1, col2, col3 = st.columns([7, 5, 5])  
with col3:
    if st.button("➡ Página siguiente"):
        st.switch_page("pages/1 📊 EDAs.py")

# Texto explicativo sobre lo que hace la aplicación
st.write("""
    Esta aplicación tiene como objetivo predecir el precio y el corte de un diamante en base a ciertos parámetros.
    A través de un modelo de regresión y clasificación, podemos predecir:
    - **El mejor precio** para un diamante dado.
    - **La mejor calidad de corte** basándonos en las características del diamante.

    Los usuarios pueden ingresar datos de diferentes características de los diamantes, como el peso, el color, la claridad, y el corte, para obtener estas predicciones.

    Utilizamos técnicas de análisis exploratorio de datos (EDA), regresión y clasificación aplicadas a unos modelos entrenados para ofrecer recomendaciones precisas basadas en los datos de entrada.
""")

# Verificar si el usuario tiene la barra lateral visible
with st.sidebar:
    menu_expanded = st.checkbox("Ocultar menú", value=False)

if menu_expanded:
    st.sidebar.empty()  # Oculta elementos del sidebar
    col1, col2, col3 = st.columns(3)
    with col1:
        if st.button('Ir a EDAs'):
            st.switch_page('pages/1 📊 EDAs.py')
    with col2:
        if st.button('Ir a Regresión'):
            st.switch_page('pages/2 🤖 Regresión.py')
    with col3:
        if st.button('Ir a Clasificación'):
            st.switch_page('pages/3 🤖 Clasificación.py')

else:
    with st.sidebar:
        st.page_link("pages/1 📊 EDAs.py", label="EDAs", icon="📊")
        st.page_link("pages/2 🤖 Regresión.py", label="Regresión", icon="📈")
        st.page_link("pages/3 🤖 Clasificación.py", label="Clasificación", icon="📉")
