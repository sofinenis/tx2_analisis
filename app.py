import streamlit as st
from textblob import TextBlob
from googletrans import Translator

# 🌻 Configuración general
st.set_page_config(page_title="🌻 Analizador de Sentimientos Girasol", page_icon="🌻", layout="centered")

# 🌻 Estilo visual cálido y floral
st.markdown("""
    <style>
        body {
            background-color: #fff8dc;
        }
        .main {
            background-color: #fffbea;
            border-radius: 15px;
            padding: 25px;
            box-shadow: 0px 0px 15px rgba(245, 200, 30, 0.4);
        }
        h1, h2, h3 {
            color: #d4a017;
            text-align: center;
            font-family: 'Comic Sans MS', cursive;
        }
        .stTextArea>div>textarea {
            background-color: #fff5b0;
            border-radius: 10px;
            border: 2px solid #f1c40f;
            color: #4a3000;
            font-weight: bold;
        }
        .stExpander {
            border: 2px solid #e1a72a;
            border-radius: 10px;
            background-color: #fffde7;
        }
        .stButton>button {
            background-color: #ffd54f;
            color: #4a3000;
            border-radius: 12px;
            border: 2px solid #e1a72a;
            font-weight: bold;
            transition: all 0.3s;
        }
        .stButton>button:hover {
            background-color: #ffeb3b;
            transform: scale(1.05);
        }
        .stSidebar {
            background-color: #fff7d6;
        }
    </style>
""", unsafe_allow_html=True)

# 🌻 Inicialización del traductor
translator = Translator()

# 🌻 Título principal
st.title("🌻 Uso de TextBlob 🌞")
st.subheader("💛 Escribe una frase y deja que florezca su sentimiento 🌼")

# 🌻 Sidebar informativa
with st.sidebar:
    st.header("🌻 Polaridad y Subjetividad 🌞")
    st.markdown("""
    **🌼 Polaridad:**  
    Indica si el sentimiento expresado en el texto es positivo, negativo o neutral.  
    Rango:  
    🔹 **-1** (muy negativo)  
    🔹 **0** (neutral)  
    🔹 **1** (muy positivo)

    **🌻 Subjetividad:**  
    Mide cuánto del contenido es **subjetivo** (opiniones, emociones, creencias)  
    frente a **objetivo** (hechos).  
    Rango:  
    🔸 **0** = objetivo  
    🔸 **1** = subjetivo
    """)

# 🌻 Expander de análisis de sentimiento
with st.expander("🌞 Analizar Polaridad y Subjetividad en un texto 🌻"):
    text1 = st.text_area("🌼 Escribe tu frase aquí:")
    if text1:
        try:
            # Traducción al inglés (para análisis)
            translation = translator.translate(text1, src="es", dest="en")
            trans_text = translation.text
            blob = TextBlob(trans_text)
        except Exception:
            st.warning("⚠️ Error de traducción, analiza directamente en inglés.")
            blob = TextBlob(text1)
        
        # 🌻 Mostrar resultados
        polarity = round(blob.sentiment.polarity, 2)
        subjectivity = round(blob.sentiment.subjectivity, 2)
        st.write(f"🌻 **Polaridad:** {polarity}")
        st.write(f"🌞 **Subjetividad:** {subjectivity}")

        # 🌼 Clasificación visual del sentimiento
        if polarity >= 0.5:
            st.success("🌻 ¡Sentimiento positivo y brillante como un girasol! 😊💛")
        elif polarity <= -0.5:
            st.error("🌧️ Sentimiento triste... pero siempre hay sol después de la lluvia 😔🌻")
        else:
            st.info("🌤️ Sentimiento neutral — equilibrio como la naturaleza 🌿😐")

# 🌻 Expander de corrección gramatical
with st.expander("🌼 Corrección gramatical en inglés 🌻"):
    text2 = st.text_area("💬 Escribe un texto en inglés para corregir:", key="4")
    if text2:
        blob2 = TextBlob(text2)
        corrected_text = blob2.correct()
        st.success("🌻 Texto corregido:")
        st.write(corrected_text)
