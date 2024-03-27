from textblob import TextBlob
import pandas as pd
import streamlit as st
from googletrans import Translator

st.title('CocinaFacil - Análisis de Sentimientos')

st.video("gatitos4.mp4")
st.markdown("#### ¡Bienvenido a CocinaFacil con ChefIA, tu asistente de cocina personal! Describe tu día en una frase y te recomendaremos una receta adecuada para tu estado de ánimo:")

translator = Translator()

with st.expander('Analizar frase'):
    text = st.text_input('Escribe por favor: ')
    if text:

        translation = translator.translate(text, src="es", dest="en")
        trans_text = translation.text
        blob = TextBlob(trans_text)
        st.write('Polarity: ', round(blob.sentiment.polarity,2))
        st.write('Subjectivity: ', round(blob.sentiment.subjectivity,2))
        x=round(blob.sentiment.polarity,2)
        if x >= 0.5:
            st.write('Es un sentimiento Positivo 😊')
            st.subheader("¡Te recomendamos probar esta receta positiva!")
            st.write("Nombre: Ensalada de quinoa con aguacate, tomate y aderezo de limón")
            st.write("Ingredientes:")
            st.write("- 1 taza de quinoa cocida")
            st.write("- 1 aguacate maduro, cortado en cubitos")
            st.write("- 1 tomate grande, cortado en cubitos")
            st.write("- Zumo de 1 limón")
            st.write("- Sal y pimienta al gusto")
            st.write("- Hojas de lechuga (opcional)")
            st.write("Preparación:")
            st.write("1. En un tazón grande, mezcla la quinoa cocida, el aguacate y el tomate.")
            st.write("2. Exprime el zumo de limón sobre la ensalada y sazona con sal y pimienta al gusto.")
            st.write("3. Opcionalmente, sirve sobre hojas de lechuga.")
        elif x <= -0.5:
            st.write('Es un sentimiento Negativo 😔')
            st.subheader("¡Te recomendamos probar esta receta reconfortante!")
            st.write("Nombre: Sopa de verduras reconfortante")
            st.write("Ingredientes:")
            st.write("- 2 zanahorias, cortadas en rodajas")
            st.write("- 2 ramas de apio, picadas")
            st.write("- 1 cebolla, picada")
            st.write("- 2 dientes de ajo, picados")
            st.write("- 1 papa grande, pelada y cortada en cubos")
            st.write("- 4 tazas de caldo de verduras")
            st.write("- Sal y pimienta al gusto")
            st.write("- Perejil fresco picado (opcional, para decorar)")
            st.write("Preparación:")
            st.write("1. En una olla grande, saltea la cebolla y el ajo en un poco de aceite hasta que estén dorados.")
            st.write("2. Agrega las zanahorias, el apio y la papa, y cocina por unos minutos.")
            st.write("3. Vierte el caldo de verduras, lleva a ebullición y luego reduce el fuego. Cocina a fuego lento hasta que las verduras estén tiernas.")
            st.write("4. Sazona con sal y pimienta al gusto.")
            st.write("5. Sirve caliente, decorado con perejil fresco si lo deseas.")
        else:
            st.write('Es un sentimiento Neutral 😐')
            st.subheader("¡Te recomendamos probar esta receta neutra!")
            st.write("Nombre: Pasta con salsa de tomate y albahaca")
            st.write("Ingredientes:")
            st.write("- 250g de pasta de tu elección")
            st.write("- 2 tazas de salsa de tomate")
            st.write("- Un puñado de hojas de albahaca fresca")
            st.write("- Sal y pimienta al gusto")
            st.write("- Queso parmesano rallado (opcional, para servir)")
            st.write("Preparación:")
            st.write("1. Cocina la pasta según las instrucciones del paquete hasta que esté al dente. Escurre y reserva.")
            st.write("2. Calienta la salsa de tomate en una sartén grande.")
            st.write("3. Agrega las hojas de albahaca picadas y sazona con sal y pimienta al gusto.")
            st.write("4. Incorpora la pasta cocida a la salsa y mezcla bien.")
            st.write("5. Sirve caliente, con queso parmesano rallado si lo deseas.")



