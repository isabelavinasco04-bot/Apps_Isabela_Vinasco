import streamlit as st
from PIL import Image

# --- Configuración de la página ---
st.set_page_config(page_title="Aplicaciones IA 💗", layout="wide")

# --- Fondo rosado y estilo general ---
page_bg = """
<style>
[data-testid="stAppViewContainer"] {
    background-color: #ffe6f2; /* Fondo rosado suave */
    color: #333333;
}
[data-testid="stSidebar"] {
    background-color: #ffb3d9; /* Sidebar rosada más intensa */
}
h1, h2, h3 {
    color: #ff3399; /* Títulos en rosado fuerte */
    text-align: center;
}
button {
    font-weight: bold;
}
div[data-testid="column"] {
    align-items: center;
    text-align: center;
}
</style>
"""
st.markdown(page_bg, unsafe_allow_html=True)

# --- Título principal ---
st.title("💗 Mis Aplicaciones con Inteligencia Artificial 💗")

# --- Sidebar ---
with st.sidebar:
    st.subheader("Aplicaciones con Inteligencia Artificial 🧠")
    st.write("Estas son mis aplicaciones desarrolladas en clase. ¡Explora y experimenta con IA! 🚀")

# --- Crear columnas alineadas ---
col1, col2, col3 = st.columns(3)

# 🔹 COLUMNA 1 🔹
with col1:
    st.subheader("Mi Primera App")
    image = Image.open('app1.jpg')
    st.image(image, width=220)
    st.write("Mi primera app desarrollada con Streamlit 🌸. Un punto de partida en mi camino de IA.")
    st.markdown(
        """
        <a href="https://miprimeraappisa.streamlit.app/" target="_blank">
            <button style="
                background-color:#ff66b3;
                color:white;
                border:none;
                padding:12px 24px;
                border-radius:10px;
                font-size:16px;
                cursor:pointer;
            ">💗 Abrir</button>
        </a>
        """,
        unsafe_allow_html=True
    )

    st.subheader("Reconocimiento de Gestos")
    image = Image.open('gesto.jpg')
    st.image(image, width=220)
    st.write("Reconoce gestos humanos usando visión por computadora con YOLOv5. ✋")
    st.markdown(
        """
        <a href="https://yolov5-isa.streamlit.app/" target="_blank">
            <button style="
                background-color:#ff66b3;
                color:white;
                border:none;
                padding:12px 24px;
                border-radius:10px;
                font-size:16px;
                cursor:pointer;
            ">✋ Abrir</button>
        </a>
        """,
        unsafe_allow_html=True
    )

# 🔹 COLUMNA 2 🔹
with col2:
    st.subheader("Análisis de Documentos")
    image = Image.open('analisis_texto.jpg')
    st.image(image, width=220)
    st.write("Analiza el contenido de documentos, identifica temas clave y genera resúmenes. 📑")
    st.markdown(
        """
        <a href="https://textoesp.streamlit.app/" target="_blank">
            <button style="
                background-color:#ff66b3;
                color:white;
                border:none;
                padding:12px 24px;
                border-radius:10px;
                font-size:16px;
                cursor:pointer;
            ">📑 Abrir</button>
        </a>
        """,
        unsafe_allow_html=True
    )

    st.subheader("Reconocer el Dibujo")
    image = Image.open('dibujo.jpg')
    st.image(image, width=220)
    st.write("Sube un dibujo y deja que la IA adivine qué representa 🎨")
    st.markdown(
        """
        <a href="https://reconnocer-el-dibujo.streamlit.app/" target="_blank">
            <button style="
                background-color:#ff66b3;
                color:white;
                border:none;
                padding:12px 24px;
                border-radius:10px;
                font-size:16px;
                cursor:pointer;
            ">🎨 Abrir</button>
        </a>
        """,
        unsafe_allow_html=True
    )

# 🔹 COLUMNA 3 🔹
with col3:
    st.subheader("Chat con PDF")
    image = Image.open('chat_pdf.jpg')
    st.image(image, width=220)
    st.write("Interactúa con documentos PDF usando IA conversacional 💬")
    st.markdown(
        """
        <a href="https://chatpdfejercicioisa.streamlit.app/" target="_blank">
            <button style="
                background-color:#ff66b3;
                color:white;
                border:none;
                padding:12px 24px;
                border-radius:10px;
                font-size:16px;
                cursor:pointer;
            ">📄 Abrir</button>
        </a>
        """,
        unsafe_allow_html=True
    )

    st.subheader("Historia a partir de un Dibujo")
    image = Image.open('historia.jpg')
    st.image(image, width=220)
    st.write("Genera una historia completa a partir de un dibujo infantil. ✨")
    st.markdown(
        """
        <a href="https://historia-infantil.streamlit.app/" target="_blank">
            <button style="
                background-color:#ff66b3;
                color:white;
                border:none;
                padding:12px 24px;
                border-radius:10px;
                font-size:16px;
                cursor:pointer;
            ">🧚 Abrir</button>
        </a>
        """,
        unsafe_allow_html=True
    )
