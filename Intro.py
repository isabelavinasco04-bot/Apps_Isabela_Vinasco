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

   # --- App: Analizador de Sentimientos ---
    st.subheader("Analizador de Sentimientos")
    image = Image.open('sentimientos.jpg')  # 👈 asegúrate de que el archivo esté en la misma carpeta que Intro.py
    st.image(image, width=200)
    st.write("En esta aplicación podrás analizar el sentimiento de un texto y descubrir si es positivo, negativo o neutro, con ayuda de Inteligencia Artificial.")
    st.markdown(
    """
    <a href="https://isabelavinasco.streamlit.app/" target="_blank">
        <button style="
            background-color:#ff66b3;
            color:white;
            border:none;
            padding:12px 24px;
            border-radius:8px;
            font-size:16px;
            cursor:pointer;
        ">
            💬 Abrir Analizador de Sentimientos
        </button>
    </a>
    """,
    unsafe_allow_html=True
    )

     # --- App: Reconocimiento de Gestos ---
    st.subheader("Reconocimiento de Gestos")
    image = Image.open('gesto.jpg')  # 👈 asegúrate de que esté en la misma carpeta que Intro.py
    st.image(image, width=200)
    st.write("En esta aplicación podrás reconocer gestos humanos usando modelos de visión por computadora basados en YOLOv5. Ideal para interacción sin contacto y control gestual.")
    st.markdown(
    """
    <a href="https://yolov5-isa.streamlit.app/" target="_blank">
        <button style="
            background-color:#ff66b3;
            color:white;
            border:none;
            padding:12px 24px;
            border-radius:8px;
            font-size:16px;
            cursor:pointer;
        ">
            ✋ Abrir Reconocimiento de Gestos
        </button>
    </a>
    """,
    unsafe_allow_html=True
    )

    # --- App: Inter de Objetos en Imagen ---
    st.subheader("Interpretación de Objetos en Imagen")
    image = Image.open('vision_app.jpg')  # 👈 asegúrate de que este archivo esté en tu carpeta
    st.image(image, width=200)
    st.write("En esta aplicación podrás subir una imagen y el modelo de IA interpretará, mostrándolos en pantalla.")
    st.markdown(
    """
    <a href="https://visionapp-isa-lpq3fitf2jwnkastes8odi.streamlit.app/" target="_blank">
        <button style="
            background-color:#ff66b3;
            color:white;
            border:none;
            padding:12px 24px;
            border-radius:8px;
            font-size:16px;
            cursor:pointer;
        ">
            🖼️ Abrir Reconocimiento de Objetos
        </button>
    </a>
    """,
    unsafe_allow_html=True
    )

with col2:
    
    #APP 2
    # --- App 2: Audio a texto ---
    st.subheader("Conversión de Audio a texto")
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

    
    # --- App: Análisis de Documentos --- APP 5
    st.subheader("Análisis de Documentos")
    image = Image.open('analisis_texto.jpg')  # 👈 asegúrate de que esté en la misma carpeta que Intro.py
    st.image(image, width=200)
    st.write("En esta aplicación podrás analizar el contenido de documentos en texto, identificar temas clave y generar resúmenes con ayuda de Inteligencia Artificial.")
    st.markdown(
    """
    <a href="https://textoesp.streamlit.app/" target="_blank">
        <button style="
            background-color:#ff66b3;
            color:white;
            border:none;
            padding:12px 24px;
            border-radius:8px;
            font-size:16px;
            cursor:pointer;
        ">
            📑 Abrir Análisis de Documentos
        </button>
    </a>
    """,
    unsafe_allow_html=True
    )
    # --- App: Detección de Rostros ---
    st.subheader("Detección de Rostros")
    image = Image.open('OCR.jpg')  # 👈 usa tu imagen real
    st.image(image, width=200)
    st.write("En la siguiente aplicación podrás detectar rostros en una imagen o foto tomada con tu cámara, y escuchar el resultado en diferentes idiomas.")
    st.markdown(
    """
    <a href="https://ocr-isa2.streamlit.app/" target="_blank">
        <button style="
            background-color:#ff66b3;
            color:white;
            border:none;
            padding:12px 24px;
            border-radius:8px;
            font-size:16px;
            cursor:pointer;
        ">
            🧠 Abrir aplicación de Detección de Rostros
        </button>
    </a>
    """,
    unsafe_allow_html=True
    )

    # --- App: Reconocer el Dibujo ---
    st.subheader("Reconocer el Dibujo")
    image = Image.open('dibujo.jpg')  # 👈 asegúrate de que esté en la misma carpeta que Intro.py
    st.image(image, width=200)
    st.write("En esta aplicación podrás subir un dibujo o realizar uno a mano, y la Inteligencia Artificial intentará reconocer qué representa tu creación. 🎨")
    st.markdown(
    """
    <a href="https://reconnocer-el-dibujo.streamlit.app/" target="_blank">
        <button style="
            background-color:#ff66b3;
            color:white;
            border:none;
            padding:12px 24px;
            border-radius:8px;
            font-size:16px;
            cursor:pointer;
        ">
            🖌️ Abrir Reconocimiento de Dibujo
        </button>
    </a>
    """,
    unsafe_allow_html=True
    )


with col3:
    # --- App: OCR Final ---
    st.subheader("OCR Final")
    image = Image.open('ocr_final.jpg')  # 👈 asegúrate de que esté en la misma carpeta que Intro.py
    st.image(image, width=200)
    st.write("En esta aplicación podrás realizar reconocimiento óptico de caracteres (OCR) y convertir texto desde imágenes de forma precisa y rápida.")
    st.markdown(
    """
    <a href="https://isavinasco.streamlit.app/" target="_blank">
        <button style="
            background-color:#ff66b3;
            color:white;
            border:none;
            padding:12px 24px;
            border-radius:8px;
            font-size:16px;
            cursor:pointer;
        ">
            🔤 Abrir Aplicación OCR Final
        </button>
    </a>
    """,
    unsafe_allow_html=True
)

    
    # --- App: Análisis de Textos en Inglés ---
    st.subheader("Análisis de Textos en Inglés")
    image = Image.open('texto_ingles.jpg')  # 👈 asegúrate de tener la imagen en la misma carpeta que Intro.py
    st.image(image, width=200)
    st.write("En esta aplicación podrás analizar textos en inglés, identificar sentimientos, temas principales y generar resúmenes con modelos de Inteligencia Artificial.")
    st.markdown(
    """
    <a href="https://isabela-vinasco-docs.streamlit.app/" target="_blank">
        <button style="
            background-color:#ff66b3;
            color:white;
            border:none;
            padding:12px 24px;
            border-radius:8px;
            font-size:16px;
            cursor:pointer;
        ">
            🇬🇧 Abrir Análisis de Textos en Inglés
        </button>
    </a>
    """,
    unsafe_allow_html=True
    )


    
    # --- App: Chat con PDF ---
    st.subheader("Chat con PDF")
    image = Image.open('chat_pdf.jpg')  # Asegúrate que la imagen esté en la carpeta correcta
    st.image(image, width=200)
    st.write("En esta aplicación podrás interactuar de forma conversacional con el contenido de un documento PDF usando IA.")
    st.markdown(
    """
    <a href="https://chatpdfejercicioisa.streamlit.app/" target="_blank">
        <button style="
            background-color:#ff66b3;
            color:white;
            border:none;
            padding:12px 24px;
            border-radius:8px;
            font-size:16px;
            cursor:pointer;
        ">
            📄 Abrir Chat con PDF
        </button>
    </a>
    """,
    unsafe_allow_html=True
    )
    # --- App: Historia a partir de un Dibujo ---
    st.subheader("Historia a partir de un Dibujo")
    image = Image.open('historia.jpg')  # 👈 asegúrate de que el archivo esté en la misma carpeta que Intro.py
    st.image(image, width=200)
    st.write("En esta aplicación podrás generar una historia completa a partir de un dibujo infantil. La Inteligencia Artificial interpreta la imagen y crea un cuento mágico inspirado en ella. ✨")
    st.markdown(
    """
    <a href="https://historia-infantil.streamlit.app/" target="_blank">
        <button style="
            background-color:#ff66b3;
            color:white;
            border:none;
            padding:12px 24px;
            border-radius:8px;
            font-size:16px;
            cursor:pointer;
        ">
            🧚 Abrir Historia a partir de un Dibujo
        </button>
    </a>
    """,
    unsafe_allow_html=True
    )


