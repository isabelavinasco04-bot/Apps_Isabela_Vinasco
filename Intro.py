import streamlit as st
from PIL import Image

# --- CONFIGURACIÓN GENERAL ---
st.set_page_config(page_title="Aplicaciones de Isa 💗", layout="wide")

# Fondo rosado mediante CSS personalizado
st.markdown(
    """
    <style>
    body {
        background-color: #ffe6f0;
    }
    [data-testid="stAppViewContainer"] {
        background-color: #ffe6f0;
    }
    [data-testid="stSidebar"] {
        background-color: #ffb3cc;
        color: white;
    }
    h1, h2, h3, h4, h5, h6, p {
        text-align: center;
    }
    .app-card {
        background-color: white;
        border-radius: 15px;
        padding: 20px;
        box-shadow: 0px 2px 8px rgba(0,0,0,0.1);
        margin-bottom: 25px;
        text-align: center;
    }
    .app-card img {
        border-radius: 10px;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# --- TÍTULO ---
st.title("🌸 Aplicaciones desarrolladas por Isa 🌸")

# --- SIDEBAR ---
with st.sidebar:
    st.subheader("Aplicaciones con Inteligencia Artificial 💫")
    st.write("Estas son mis aplicaciones desarrolladas en clase, un recorrido por mi aprendizaje en IA, programación y creatividad digital.")

# --- APP PRINCIPAL ---
st.markdown("<br>", unsafe_allow_html=True)
st.subheader("Mi Primera App 💗")
image = Image.open('app1.jpg')
st.image(image, width=230)
st.write("Esta fue mi primera aplicación desarrollada con Streamlit. 🌸 Un punto de partida en mi camino de exploración con la Inteligencia Artificial, la programación y la creatividad digital.")
st.markdown(
    """
    <div style="text-align:center;">
        <a href="https://miprimeraappisa.streamlit.app/" target="_blank">
            <button style="
                background-color:#ff66b3;
                color:white;
                border:none;
                padding:12px 24px;
                border-radius:8px;
                font-size:16px;
                cursor:pointer;
            ">
                💗 Abrir Mi Primera App
            </button>
        </a>
    </div>
    """,
    unsafe_allow_html=True
)

st.markdown("<br><hr><br>", unsafe_allow_html=True)

# --- COLUMNAS ALINEADAS ---
col1, col2, col3 = st.columns(3)

# --------- COLUMNA 1 ---------
with col1:
    apps_col1 = [
        ("Conversión de texto a voz", "texto_avoz.jpg", "https://intro3-cv4kbcjgxbiveh8ph2kmyp.streamlit.app/", "💗 Abrir aplicación de Texto a Voz"),
        ("Analizador de Sentimientos", "sentimientos.jpg", "https://isabelavinasco.streamlit.app/", "💬 Abrir Analizador de Sentimientos"),
        ("Reconocimiento de Gestos", "gesto.jpg", "https://yolov5-isa.streamlit.app/", "✋ Abrir Reconocimiento de Gestos"),
        ("Interpretación de Objetos en Imagen", "vision_app.jpg", "https://visionapp-isa-lpq3fitf2jwnkastes8odi.streamlit.app/", "🖼️ Abrir Reconocimiento de Objetos"),
        ("Control por Voz", "voice.jpg", "https://ctrlvoiceisa.streamlit.app/", "🎙️ Abrir Control por Voz")
    ]

    for title, img, link, button in apps_col1:
        with st.container():
            st.markdown(f"<div class='app-card'><h3>{title}</h3>", unsafe_allow_html=True)
            st.image(Image.open(img), width=200)
            st.markdown(f"""
                <p></p>
                <a href="{link}" target="_blank">
                    <button style="
                        background-color:#ff66b3;
                        color:white;
                        border:none;
                        padding:12px 24px;
                        border-radius:8px;
                        font-size:16px;
                        cursor:pointer;
                    ">{button}</button>
                </a></div>
            """, unsafe_allow_html=True)

# --------- COLUMNA 2 ---------
with col2:
    apps_col2 = [
        ("Conversión de Audio a Texto", "audio_atexto.jpg", "https://intro2-fojj4mqk3pvfuy4gb5twvg.streamlit.app/", "🎧 Abrir aplicación de Audio a Texto"),
        ("Análisis de Documentos", "analisis_texto.jpg", "https://textoesp.streamlit.app/", "📑 Abrir Análisis de Documentos"),
        ("Detección de Rostros", "OCR.jpg", "https://ocr-isa2.streamlit.app/", "🧠 Abrir aplicación de Detección de Rostros"),
        ("Reconocer el Dibujo", "dibujo.jpg", "https://reconnocer-el-dibujo.streamlit.app/", "🖌️ Abrir Reconocimiento de Dibujo"),
        ("Control LED (IoT)", "control.jpg", "https://enviarcmqttisa.streamlit.app/", "💡 Abrir Control LED (IoT)")
    ]

    for title, img, link, button in apps_col2:
        with st.container():
            st.markdown(f"<div class='app-card'><h3>{title}</h3>", unsafe_allow_html=True)
            st.image(Image.open(img), width=200)
            st.markdown(f"""
                <p></p>
                <a href="{link}" target="_blank">
                    <button style="
                        background-color:#ff66b3;
                        color:white;
                        border:none;
                        padding:12px 24px;
                        border-radius:8px;
                        font-size:16px;
                        cursor:pointer;
                    ">{button}</button>
                </a></div>
            """, unsafe_allow_html=True)

# --------- COLUMNA 3 ---------
with col3:
    apps_col3 = [
        ("Reconocimiento Óptico de Caracteres", "ocr_final.jpg", "https://isavinasco.streamlit.app/", "🔤 Abrir Aplicación OCR Final"),
        ("Análisis de Textos en Inglés", "texto_ingles.jpg", "https://isabela-vinasco-docs.streamlit.app/", "🇬🇧 Abrir Análisis de Textos en Inglés"),
        ("Chat con PDF", "chat_pdf.jpg", "https://chatpdfejercicioisa.streamlit.app/", "📄 Abrir Chat con PDF"),
        ("Historia a partir de un Dibujo", "historia.jpg", "https://historia-infantil.streamlit.app/", "🧚 Abrir Historia a partir de un Dibujo")
    ]

    for title, img, link, button in apps_col3:
        with st.container():
            st.markdown(f"<div class='app-card'><h3>{title}</h3>", unsafe_allow_html=True)
            st.image(Image.open(img), width=200)
            st.markdown(f"""
                <p></p>
                <a href="{link}" target="_blank">
                    <button style="
                        background-color:#ff66b3;
                        color:white;
                        border:none;
                        padding:12px 24px;
                        border-radius:8px;
                        font-size:16px;
                        cursor:pointer;
                    ">{button}</button>
                </a></div>
            """, unsafe_allow_html=True)
