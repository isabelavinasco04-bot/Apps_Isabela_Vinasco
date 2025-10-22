import streamlit as st
from PIL import Image

# --- CONFIGURACIÓN DE PÁGINA ---
st.set_page_config(page_title="Aplicaciones IA 💗", layout="wide")

# --- ESTILO VISUAL ROSADO Y CENTRADO ---
page_bg = """
<style>
[data-testid="stAppViewContainer"] {
    background: linear-gradient(180deg, #ffe6f2 0%, #ffccdf 100%);
    color: #333333;
}
[data-testid="stSidebar"] {
    background-color: #ffb3d9;
}
h1, h2, h3 {
    color: #ff3399;
    text-align: center;
}
div[data-testid="column"] {
    display: flex;
    flex-direction: column;
    align-items: center;
    text-align: center;
}
button {
    font-weight: bold;
}
</style>
"""
st.markdown(page_bg, unsafe_allow_html=True)

# --- TÍTULO PRINCIPAL ---
st.title("💗 Mis Aplicaciones con Inteligencia Artificial 💗")

# --- SIDEBAR ---
with st.sidebar:
    st.subheader("Aplicaciones con Inteligencia Artificial 🧠")
    st.write("Estas son mis aplicaciones desarrolladas en clase. 🌸 ¡Explora y experimenta con IA!")

# --- CREAR COLUMNAS ---
col1, col2, col3 = st.columns(3)

# 🔹 COLUMNA 1 🔹
with col1:
    # Mi Primera App
    st.subheader("Mi Primera App")
    image = Image.open('app1.jpg')
    st.image(image, width=220)
    st.write("Mi primera app desarrollada con Streamlit. 🌸 Un punto de partida en mi camino de exploración con la IA.")
    st.markdown(
        """
        <a href="https://miprimeraappisa.streamlit.app/" target="_blank">
            <button style="background-color:#ff66b3;color:white;border:none;padding:12px 24px;border-radius:10px;font-size:16px;cursor:pointer;">💗 Abrir</button>
        </a>
        """, unsafe_allow_html=True)

    # Conversión de texto a voz
    st.subheader("Conversión de Texto a Voz")
    image = Image.open('texto_avoz.jpg')
    st.image(image, width=220)
    st.write("Convierte texto a voz con esta app de IA 🎤")
    st.markdown(
        """
        <a href="https://intro3-cv4kbcjgxbiveh8ph2kmyp.streamlit.app/" target="_blank">
            <button style="background-color:#ff66b3;color:white;border:none;padding:12px 24px;border-radius:10px;font-size:16px;cursor:pointer;">🔊 Abrir</button>
        </a>
        """, unsafe_allow_html=True)

    # Analizador de Sentimientos
    st.subheader("Analizador de Sentimientos")
    image = Image.open('sentimientos.jpg')
    st.image(image, width=220)
    st.write("Analiza si un texto es positivo, negativo o neutro 💬")
    st.markdown(
        """
        <a href="https://isabelavinasco.streamlit.app/" target="_blank">
            <button style="background-color:#ff66b3;color:white;border:none;padding:12px 24px;border-radius:10px;font-size:16px;cursor:pointer;">💬 Abrir</button>
        </a>
        """, unsafe_allow_html=True)

    # Reconocimiento de Gestos
    st.subheader("Reconocimiento de Gestos")
    image = Image.open('gesto.jpg')
    st.image(image, width=220)
    st.write("Reconoce gestos humanos con YOLOv5 ✋")
    st.markdown(
        """
        <a href="https://yolov5-isa.streamlit.app/" target="_blank">
            <button style="background-color:#ff66b3;color:white;border:none;padding:12px 24px;border-radius:10px;font-size:16px;cursor:pointer;">✋ Abrir</button>
        </a>
        """, unsafe_allow_html=True)

    # Interpretación de Objetos
    st.subheader("Interpretación de Objetos en Imagen")
    image = Image.open('vision_app.jpg')
    st.image(image, width=220)
    st.write("Sube una imagen y la IA detectará los objetos 🖼️")
    st.markdown(
        """
        <a href="https://visionapp-isa-lpq3fitf2jwnkastes8odi.streamlit.app/" target="_blank">
            <button style="background-color:#ff66b3;color:white;border:none;padding:12px 24px;border-radius:10px;font-size:16px;cursor:pointer;">🖼️ Abrir</button>
        </a>
        """, unsafe_allow_html=True)

    # Control por Voz
    st.subheader("Control por Voz")
    image = Image.open('voice.jpg')
    st.image(image, width=220)
    st.write("Controla acciones mediante comandos de voz 🎙️")
    st.markdown(
        """
        <a href="https://ctrlvoiceisa.streamlit.app/" target="_blank">
            <button style="background-color:#ff66b3;color:white;border:none;padding:12px 24px;border-radius:10px;font-size:16px;cursor:pointer;">🎙️ Abrir</button>
        </a>
        """, unsafe_allow_html=True)


# 🔹 COLUMNA 2 🔹
with col2:
    # Audio a Texto
    st.subheader("Conversión de Audio a Texto")
    image = Image.open('audio_atexto.jpg')
    st.image(image, width=220)
    st.write("Convierte tus audios en texto 🎧")
    st.markdown(
        """
        <a href="https://intro2-fojj4mqk3pvfuy4gb5twvg.streamlit.app/" target="_blank">
            <button style="background-color:#ff66b3;color:white;border:none;padding:12px 24px;border-radius:10px;font-size:16px;cursor:pointer;">🎧 Abrir</button>
        </a>
        """, unsafe_allow_html=True)

    # Análisis de Documentos
    st.subheader("Análisis de Documentos")
    image = Image.open('analisis_texto.jpg')
    st.image(image, width=220)
    st.write("Analiza el contenido de documentos con IA 📑")
    st.markdown(
        """
        <a href="https://textoesp.streamlit.app/" target="_blank">
            <button style="background-color:#ff66b3;color:white;border:none;padding:12px 24px;border-radius:10px;font-size:16px;cursor:pointer;">📑 Abrir</button>
        </a>
        """, unsafe_allow_html=True)

    # Detección de Rostros
    st.subheader("Detección de Rostros")
    image = Image.open('OCR.jpg')
    st.image(image, width=220)
    st.write("Detecta rostros y obtén resultados multilenguaje 🧠")
    st.markdown(
        """
        <a href="https://ocr-isa2.streamlit.app/" target="_blank">
            <button style="background-color:#ff66b3;color:white;border:none;padding:12px 24px;border-radius:10px;font-size:16px;cursor:pointer;">🧠 Abrir</button>
        </a>
        """, unsafe_allow_html=True)

    # Reconocer el Dibujo
    st.subheader("Reconocer el Dibujo")
    image = Image.open('dibujo.jpg')
    st.image(image, width=220)
    st.write("Sube un dibujo y deja que la IA lo interprete 🎨")
    st.markdown(
        """
        <a href="https://reconnocer-el-dibujo.streamlit.app/" target="_blank">
            <button style="background-color:#ff66b3;color:white;border:none;padding:12px 24px;border-radius:10px;font-size:16px;cursor:pointer;">🎨 Abrir</button>
        </a>
        """, unsafe_allow_html=True)

    # Control LED
    st.subheader("Control LED (IoT)")
    image = Image.open('control.jpg')
    st.image(image, width=220)
    st.write("Controla un sistema LED con comandos MQTT 💡")
    st.markdown(
        """
        <a href="https://enviarcmqttisa.streamlit.app/" target="_blank">
            <button style="background-color:#ff66b3;color:white;border:none;padding:12px 24px;border-radius:10px;font-size:16px;cursor:pointer;">💡 Abrir</button>
        </a>
        """, unsafe_allow_html=True)


# 🔹 COLUMNA 3 🔹
with col3:
    # OCR Final
    st.subheader("Reconocimiento Óptico de Caracteres")
    image = Image.open('ocr_final.jpg')
    st.image(image, width=220)
    st.write("Convierte texto desde imágenes de forma precisa 🔤")
    st.markdown(
        """
        <a href="https://isavinasco.streamlit.app/" target="_blank">
            <button style="background-color:#ff66b3;color:white;border:none;padding:12px 24px;border-radius:10px;font-size:16px;cursor:pointer;">🔤 Abrir</button>
        </a>
        """, unsafe_allow_html=True)

    # Análisis de Textos en Inglés
    st.subheader("Análisis de Textos en Inglés")
    image = Image.open('texto_ingles.jpg')
    st.image(image, width=220)
    st.write("Analiza textos en inglés, sentimientos y temas 🇬🇧")
    st.markdown(
        """
        <a href="https://isabela-vinasco-docs.streamlit.app/" target="_blank">
            <button style="background-color:#ff66b3;color:white;border:none;padding:12px 24px;border-radius:10px;font-size:16px;cursor:pointer;">🇬🇧 Abrir</button>
        </a>
        """, unsafe_allow_html=True)

    # Chat con PDF
    st.subheader("Chat con PDF")
    image = Image.open('chat_pdf.jpg')
    st.image(image, width=220)
    st.write("Interactúa con un PDF usando IA 💬")
    st.markdown(
        """
        <a href="https://chatpdfejercicioisa.streamlit.app/" target="_blank">
            <button style="background-color:#ff66b3;color:white;border:none;padding:12px 24px;border-radius:10px;font-size:16px;cursor:pointer;">📄 Abrir</button>
        </a>
        """, unsafe_allow_html=True)

    # Historia a partir de un Dibujo
    st.subheader("Historia a partir de un Dibujo")
    image = Image.open('historia.jpg')
    st.image(image, width=220)
    st.write("Genera una historia completa a partir de un dibujo infantil ✨")
    st.markdown(
        """
        <a href="https://historia-infantil.streamlit.app/" target="_blank">
            <button style="background-color:#ff66b3;color:white;border:none;padding:12px 24px;border-radius:10px;font-size:16px;cursor:pointer;">🧚 Abrir</button>
        </a>
        """, unsafe_allow_html=True)
