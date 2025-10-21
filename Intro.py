import streamlit as st
from PIL import Image

st.title("Aplicaciones")

with st.sidebar:
    st.subheader("Aplicaciones con Inteligencia Artificial.")
    parrafo = "Estas son mis aplicaciones desarrolladas en clase"
    st.write(parrafo)

# Crear columnas
col1, col2, col3 = st.columns(3)

with col1:
    #APP1
    st.subheader("Conversión de texto a voz")
    image = Image.open('texto_avoz.jpg')
    st.image(image, width=190)
    st.write("En el siguiente enlace podrás usar nuestra aplicación de Inteligencia Artificial para convertir texto a voz:")

    # Botón rosado
    st.markdown(
        """
        <a href="https://intro3-cv4kbcjgxbiveh8ph2kmyp.streamlit.app/" target="_blank">
            <button style="
                background-color:#ff66b3;
                color:white;
                border:none;
                padding:12px 24px;
                border-radius:8px;
                font-size:16px;
                cursor:pointer;
            ">
                💗 Abrir aplicación de Texto a Voz
            </button>
        </a>
        """,
        unsafe_allow_html=True
    )

    st.subheader("Reconocimiento de Objetos")
    image = Image.open('txt_to_audio.png')
    st.image(image, width=200)
    st.write("En la siguiente enlace veremos cómo se detectan objetos en imágenes.")
    url = "https://xn3pg24ztuv6fdiqon8qn3.streamlit.app/"
    st.write(f"YOLO: [Enlace]({url})")

    st.subheader("Entrenando Modelos")
    image = Image.open('OIG5.jpg')
    st.image(image, width=200)
    st.write("En la siguiente enlace veremos cómo puedes usar tu modelo entrenado.")
    url = "https://xn3pg24ztuv6fdiqon8qn3.streamlit.app/"
    st.write(f"YOLO: [Enlace]({url})")

with col2:
    #APP 2
    # --- App 2: Audio a texto ---
    st.subheader("Audio a texto")
    image = Image.open('audio_atexto.jpg')
    st.image(image, width=200)
    st.write("En la siguiente enlace podrás usar la aplicación de Inteligencia Artificial que convierte archivos de audio a texto.")
    st.markdown(
    """
    <a href="https://intro2-fojj4mqk3pvfuy4gb5twvg.streamlit.app/" target="_blank">
        <button style="
            background-color:#ff66b3;
            color:white;
            border:none;
            padding:12px 24px;
            border-radius:8px;
            font-size:16px;
            cursor:pointer;
        ">
            🎧 Abrir aplicación de Audio a Texto
        </button>
    </a>
    """,
    unsafe_allow_html=True
    )
    st.subheader("Análisis de Datos")
    image = Image.open('data_analisis.png')
    st.image(image, width=190)
    st.write("En la siguiente enlace veremos cómo se pueden analizar datos usando agentes.")
    url = "https://asistpy-csv.streamlit.app/"
    st.write(f"Datos: [Enlace]({url})")

    st.subheader("Transcriptor Audio y Video")
    image = Image.open('OIG3.jpg')
    st.image(image, width=200)
    st.write("En la siguiente enlace veremos cómo realizamos transcripciones de audio/video.")
    url = "https://transcript-whisper.streamlit.app/"
    st.write(f"Transcriptor: [Enlace]({url})")

with col3:
    st.subheader("Generación en Contexto")
    image = Image.open('Chat_pdf.png')
    st.image(image, width=190)
    st.write("En la siguiente veremos una aplicación que usa RAG a partir de un documento (PDF).")
    url = "https://chatpdf-cc.streamlit.app/"
    st.write(f"RAG: [Enlace]({url})")

    st.subheader("Análisis de Imagen")
    image = Image.open('OIG4.jpg')
    st.image(image, width=200)
    st.write("En la siguiente enlace veremos la capacidad de análisis en imágenes.")
    url = "https://vision2-gpt4o.streamlit.app/"
    st.write(f"Visión: [Enlace]({url})")

    st.subheader("Sistema Ciberfísico")
    image = Image.open('OIG6.jpg')
    st.image(image, width=200)
    st.write("En la siguiente enlace veremos la capacidad de interacción con el mundo físico.")
    url = "https://vision2-gpt4o.streamlit.app/"
    st.write(f"Visión: [Enlace]({url})")

