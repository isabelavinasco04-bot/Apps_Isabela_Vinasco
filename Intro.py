import streamlit as st
from PIL import Image

# --- Configuración general ---
st.set_page_config(page_title="Aplicaciones IA 💗", layout="wide")

# Fondo rosado
page_bg = """
<style>
[data-testid="stAppViewContainer"] {
    background-color: #ffe6f2;
}
[data-testid="stSidebar"] {
    background-color: #ffb3d9;
}
h1, h2, h3, p {
    color: #333333;
    text-align: center;
}
button {
    display: block;
    margin: 0 auto;
}

/* 💗 --- FIX para quitar las líneas azules de los enlaces --- */
a, a:visited, a:hover, a:active {
    text-decoration: none !important;
    outline: none !important;
    box-shadow: none !important;
}
</style>
"""
st.markdown(page_bg, unsafe_allow_html=True)

st.title("Aplicaciones")

with st.sidebar:
    st.subheader("Aplicaciones con Inteligencia Artificial.")
    parrafo = "Estas son mis aplicaciones desarrolladas en clase"
    st.write(parrafo)

# --- App: Mi Primera App ---
st.subheader("Mi Primera App")
image = Image.open('app1.jpg')  
st.image(image, width=200)
st.write("Esta fue mi primera aplicación desarrollada con Streamlit. 🌸 Un punto de partida en mi camino de exploración con la Inteligencia Artificial, la programación y la creatividad digital.")
st.markdown(
    """
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
    """,
    unsafe_allow_html=True
)

# --- Crear columnas alineadas ---
col1, col2, col3 = st.columns([1, 1, 1], gap="large")

with col1:
    st.markdown("<div style='text-align:center'>", unsafe_allow_html=True)
    st.subheader("Conversión de texto a voz")
    image = Image.open('texto_avoz.jpg')
    st.image(image, width=190)
    st.write("En el siguiente enlace podrás usar nuestra aplicación de Inteligencia Artificial para convertir texto a voz:")
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

    st.subheader("Analizador de Sentimientos")
    image = Image.open('sentimientos.jpg')
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

    st.subheader("Reconocimiento de Gestos")
    image = Image.open('gesto.jpg')
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

    st.subheader("Interpretación de Objetos en Imagen")
    image = Image.open('vision_app.jpg')
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

    st.subheader("Control por Voz")
    image = Image.open('voice.jpg')
    st.image(image, width=200)
    st.write("En esta aplicación podrás controlar acciones mediante comandos de voz, usando reconocimiento de habla y procesamiento de lenguaje natural.")
    st.markdown(
    """
    <a href="https://ctrlvoiceisa.streamlit.app/" target="_blank">
        <button style="
            background-color:#ff66b3;
            color:white;
            border:none;
            padding:12px 24px;
            border-radius:8px;
            font-size:16px;
            cursor:pointer;
        ">
            🎙️ Abrir Control por Voz
        </button>
    </a>
    """,
    unsafe_allow_html=True
    )
    st.markdown("</div>", unsafe_allow_html=True)


with col2:
    st.markdown("<div style='text-align:center'>", unsafe_allow_html=True)
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

    st.subheader("Análisis de Documentos")
    image = Image.open('analisis_texto.jpg')
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

    st.subheader("Detección de Rostros")
    image = Image.open('OCR.jpg')
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

    st.subheader("Reconocer el Dibujo")
    image = Image.open('dibujo.jpg')
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

    st.subheader("Control LED (IoT)")
    image = Image.open('control.jpg')
    st.image(image, width=200)
    st.write("En esta aplicación podrás controlar un sistema LED mediante comandos MQTT, interactuando con dispositivos IoT en tiempo real. 💡")
    st.markdown(
    """
    <a href="https://enviarcmqttisa.streamlit.app/" target="_blank">
        <button style="
            background-color:#ff66b3;
            color:white;
            border:none;
            padding:12px 24px;
            border-radius:8px;
            font-size:16px;
            cursor:pointer;
        ">
            💡 Abrir Control LED (IoT)
        </button>
    </a>
    """,
    unsafe_allow_html=True
    )
    st.markdown("</div>", unsafe_allow_html=True)


with col3:
    st.markdown("<div style='text-align:center'>", unsafe_allow_html=True)
    st.subheader("Reconocimiento Óptico de Caracteres")
    image = Image.open('ocr_final.jpg')
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

    st.subheader("Análisis de Textos en Inglés")
    image = Image.open('texto_ingles.jpg')
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

    st.subheader("Chat con PDF")
    image = Image.open('chat_pdf.jpg')
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

    st.subheader("Historia a partir de un Dibujo")
    image = Image.open('historia.jpg')
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
    st.markdown("</div>", unsafe_allow_html=True)

