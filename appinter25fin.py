import streamlit as st
import pandas as pd
import os

st.set_page_config(page_title="Exposiciones 18 de julio 2025", page_icon="📚")

st.title("📚 Exposiciones - 18 de julio de 2025")
st.subheader("Profesor Javier Gutiérrez - Salón F 307 USA")
st.markdown("""
Cada grupo debe:
- Escribir el nombre de su grupo.
- Elegir solo un horario disponible.
- Pulsar **Reservar**.

✅ Una vez reservado, el horario quedará bloqueado para otros grupos.
""")

# Horarios disponibles
horarios = [
    "8:00 – 8:25",
    "8:25 – 8:50",
    "8:50 – 9:15",
    "9:15 – 9:40",
    "9:40 – 10:05",
    "10:05 – 10:30",
    "10:30 – 10:55",
    "10:55 – 11:20"
]

archivo = 'reservas.csv'

# Crear archivo si no existe
if not os.path.exists(archivo):
    df_init = pd.DataFrame(columns=['Grupo', 'Horario'])
    df_init.to_csv(archivo, index=False)

# Leer reservas existentes
df = pd.read_csv(archivo)

# Calcular horarios que aún están libres
horarios_disponibles = [h for h in horarios if h not in df['Horario'].values]

grupo = st.text_input("Nombre del grupo:")
horario = st.selectbox("Elige un horario disponible:", horarios_disponibles)

if st.button("Reservar"):
    if grupo.strip() == "":
        st.warning("⚠️ Por favor escribe el nombre del grupo.")
    elif horario in df['Horario'].values:
        st.error(f"⚠️ El horario '{horario}' ya fue tomado. Recarga la página para ver horarios actualizados.")
    else:
        # Guardar reserva
        nueva_reserva = pd.DataFrame([[grupo, horario]], columns=['Grupo', 'Horario'])
        df = pd.concat([df, nueva_reserva], ignore_index=True)
        df.to_csv(archivo, index=False)
        st.success(f"✅ ¡Gracias {grupo}! Has reservado el horario '{horario}'.")

st.markdown("---")
st.markdown("### 📄 **Reservas confirmadas hasta ahora:**")
st.dataframe(df)
