from textblob import TextBlob
import pandas as pd
import streamlit as st
from googletrans import Translator

st.title('CocinaFacil - Análisis de Sentimientos')

st.video("gatitos4.mp4")
st.markdown(f"#### ¡Bienvenido a CocinaFacil con ChefIA, tu asistente de cocina personal! Describe tu día en una frase y te recomendaremos una receta adecuada para tu estado de ánimo:")

translator = Translator()

with st.expander('Analizar texto'):
    text = st.text_input('Escribe por favor: ')
    if text:

        translation = translator.translate(text, src="es", dest="en")
        trans_text = translation.text
        blob = TextBlob(trans_text)
        st.write('Polarity: ', round(blob.sentiment.polarity,2))
        st.write('Subjectivity: ', round(blob.sentiment.subjectivity,2))
        x=round(blob.sentiment.polarity,2)
        if x >= 0.5:
            st.write( 'Es un sentimiento Positivo 😊')
        elif x <= -0.5:
            st.write( 'Es un sentimiento Negativo 😔')
        else:
            st.write( 'Es un sentimiento Neutral 😐')
            



