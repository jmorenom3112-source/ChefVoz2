import streamlit as st
from gtts import gTTS
import io

# Configuración estética de alto contraste y accesibilidad para el docente
st.set_page_config(page_title="ChefVoz - Menú Inclusivo", page_icon="🍲", layout="centered")

st.markdown("<h1 style='text-align: center; color: #FF4B4B;'>🍲 ChefVoz</h1>", unsafe_allow_html=True)
st.markdown("<h3 style='text-align: center; color: #7F8C8D;'>El Menú Gastronómico Inteligente e Inclusivo</h3>", unsafe_allow_html=True)
st.write("---")

# Simulación de la Base de Datos del menú
menu = [
    {
        "plato": "Fettuccine Alfredo",
        "categoria": "Pastas",
        "descripcion": "Pasta artesanal italiana con una salsa cremosa a base de queso parmesano legítimo y mantequilla premium.",
        "descripcion_en": "Artisanal Italian pasta with a creamy sauce made from authentic Parmesan cheese and premium butter.",
        "alergenos": "Gluten, Lácteos"
    },
    {
        "plato": "Ceviche Clásico",
        "categoria": "Mariscos",
        "descripcion": "Cubos de pescado fresco marinados en jugo de limón puro, acompañados de cebolla roja, camote dulce y maíz tierno.",
        "descripcion_en": "Fresh fish cubes marinated in pure lime juice, served with red onion, sweet potato, and tender corn.",
        "alergenos": "Pescado"
    }
]

# Selector de idioma en la barra lateral
idioma = st.sidebar.radio("🌐 Seleccione su Idioma / Select Language", ("Español", "English"))

st.sidebar.markdown("### 👁️ Accesibilidad")
alto_contraste = st.sidebar.checkbox("Activar Alto Contraste")

if alto_contraste:
    st.markdown("""
        <style>
        .stApp { background-color: #000000; color: #FFFFFF; }
        h1, h3, p { color: #FFFFFF !important; }
        </style>
    """, unsafe_allow_html=True)

# Despliegue de los platillos
for item in menu:
    with st.container():
        st.markdown(f"### 🍽️ {item['plato']}")
        st.caption(f"Categoría: {item['categoria']} | Alérgenos: {item['alergenos']}")
        
        # Lógica de traducción inteligente simulada por idioma
        if idioma == "Español":
            texto_a_leer = item['descripcion']
            st.write(texto_a_leer)
        else:
            texto_a_leer = item['descripcion_en']
            st.write(f"*{texto_a_upper if 'texto_a_upper' in locals() else texto_a_leer}*")
            
        # TECNOLOGÍA EMERGENTE: Generador de Texto a Voz por Inteligencia Artificial en tiempo real
        lang_code = 'es' if idioma == "Español" else 'en'
        tts = gTTS(text=texto_a_leer, lang=lang_code, slow=False)
        fp = io.BytesIO()
        tts.write_to_fp(fp)
        fp.seek(0)
        
        # Botón de reproducción de audio inclusivo nativo
        st.audio(fp, format='audio/mp3')
        st.write("---")
