import streamlit as st
from datetime import datetime, date
import pandas as pd

# ==========================================
# CONFIGURACIÓN DE LA PÁGINA
# ==========================================
st.set_page_config(
    page_title="Prog. Operativo Cirugía General",
    page_icon="⚕️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ==========================================
# BASE DE DATOS SIMULADA (Extraída del PDF)
# ==========================================
# Diccionario principal de residentes con sus datos
RESIDENTES = {
    # R4
    "Beltrán Delgado Jorge Omar": {
        "grado": "R4",
        "tesis": "Estado nutricional en pacientes ingresados para cirugía de urgencia en Hospital Civil de Culiacán",
        "vacaciones": [("2026-10-05", "2026-10-16"), ("2027-01-18", "2027-01-29")],
        "rotaciones": {3: "Rotación campo", 4: "Rotación campo", 5: "Rotación campo", 6: "Rotación campo", 8: "Cirugía Pediátrica (HPS)", 9: "Cirugía Pediátrica (HPS)"}
    },
    "Soto Valle José Emaús": {
        "grado": "R4",
        "tesis": "Correlación entre aspectos clínicos y proteína C reactiva como marcadores para fuga anastomótica intestinal",
        "vacaciones": [("2026-11-30", "2026-12-11"), ("2026-05-04", "2026-05-15")], # Ajuste de año lógico según PDF
        "rotaciones": {5: "Coloproctología (HCG)", 7: "Rotación campo", 8: "Rotación campo", 9: "Rotación campo", 10: "Rotación campo", 1: "Cirugía Pediátrica"}
    },
    "Villegas Rodríguez José": {
        "grado": "R4",
        "tesis": "Utilidad de escalas de Parkland y Nassar para conversión a cirugía abierta en colecistectomía difícil",
        "vacaciones": [("2026-04-06", "2026-04-17"), ("2027-04-20", "2027-05-01")],
        "rotaciones": {9: "Oncocirugía (CMN 20 Nov)", 11: "Rotación campo", 12: "Rotación campo", 1: "Cirugía Pediátrica", 2: "Cirugía Pediátrica"}
    },
    # R3
    "Almanza Orduño Athmir Antonio": {
        "grado": "R3",
        "tesis": "Eficiencia de la safenoablación con láser vs safenectomía abierta en enfermedad venosa crónica",
        "vacaciones": [("2026-06-15", "2026-06-26"), ("2026-08-31", "2026-09-11")],
        "rotaciones": {3: "Cirugía Vascular (HCG)", 6: "Cirugía de Tórax (HCG)", 7: "Cirugía Vascular (HCG)"}
    },
    "Bueno López Daniela Alejandra": {
        "grado": "R3",
        "tesis": "Prevalencia de complicaciones locales tempranas y tardías de pancreatitis aguda en el HCC",
        "vacaciones": [("2026-11-16", "2026-11-27"), ("2027-01-18", "2027-01-29")],
        "rotaciones": {3: "Coloproctología (HGM)", 4: "Cirugía Vascular (HCG)", 11: "Oncocirugía (CMN 20 Nov)"}
    },
    "Cordero Medina Marielos": {
        "grado": "R3",
        "tesis": "Utilidad de la escala Portsmouth-POSSUM para predecir morbilidad y mortalidad en cirugía...",
        "vacaciones": [("2026-06-01", "2026-06-12"), ("2027-02-15", "2027-02-26")],
        "rotaciones": {8: "Oncocirugía (CMN 20 Nov)", 10: "Cirugía de Tórax (HCG)", 11: "Cirugía Vascular (HCG)"}
    },
    "Ojeda Valenzuela José Antonio": {
        "grado": "R3",
        "tesis": "Pruebas de función hepática como predictores de coledocolitiasis",
        "vacaciones": [("2026-04-20", "2026-05-01"), ("2026-11-02", "2026-11-13")],
        "rotaciones": {3: "Cirugía oncológica (CMN 20 Nov)", 8: "Cirugía de tórax (HCG)"}
    },
    # R2
    "Angulo Sánchez Rolando": {
        "grado": "R2",
        "tesis": "Por definir",
        "vacaciones": [("2026-03-02", "2026-03-13"), ("2026-11-30", "2026-12-11")],
        "rotaciones": {4: "Coloproctología (ISSSTE)", 9: "Cirugía vascular (HCG)"}
    },
    "Luna Borboa Jorge Luis": {
        "grado": "R2",
        "tesis": "Por definir",
        "vacaciones": [("2027-01-04", "2027-01-15"), ("2026-11-30", "2026-12-11")],
        "rotaciones": {5: "Coloproctología (ISSSTE)"}
    },
    "Maldonado Guardado Diana Guadalupe": {
        "grado": "R2",
        "tesis": "Por definir",
        "vacaciones": [("2026-07-06", "2026-07-17"), ("2026-06-01", "2026-06-12")],
        "rotaciones": {11: "Coloproctología (ISSSTE)"}
    },
    "Valenzuela Pardo Mariana": {
        "grado": "R2",
        "tesis": "Por definir",
        "vacaciones": [("2026-03-16", "2026-03-27"), ("2026-11-02", "2026-11-13")],
        "rotaciones": {8: "Coloproctología (ISSSTE)"}
    },
    # R1
    "López Félix Jesús Arturo": {
        "grado": "R1", "tesis": "Por definir",
        "vacaciones": [("2026-05-18", "2026-05-29"), ("2026-11-16", "2026-11-27")], "rotaciones": {}
    },
    "Portugal Beltran Emma": {
        "grado": "R1", "tesis": "Por definir",
        "vacaciones": [("2026-04-20", "2026-05-01"), ("2026-10-05", "2026-10-16")], "rotaciones": {}
    },
    "Rendon Sánchez Manuel": {
        "grado": "R1", "tesis": "Por definir",
        "vacaciones": [("2026-06-15", "2026-06-26"), ("2027-01-18", "2027-01-29")], "rotaciones": {}
    },
    "Romero Molina Geovana Clarisa": {
        "grado": "R1", "tesis": "Por definir",
        "vacaciones": [("2026-06-01", "2026-06-12"), ("2026-11-30", "2026-12-11")], "rotaciones": {}
    },
    "Valdez Valdez Ricardo Antonio": {
        "grado": "R1", "tesis": "Por definir",
        "vacaciones": [("2026-07-06", "2026-07-17"), ("2027-02-01", "2027-02-12")], "rotaciones": {}
    }
}

# Lista de clases (Muestra representativa basada en el programa)
CLASES = [
    {"fecha": "2026-03-03", "tema": "Historia de la cirugía", "ponente": "López Félix Jesús Arturo", "modulo": "Introducción"},
    {"fecha": "2026-03-04", "tema": "Asepsia y antisepsia", "ponente": "Portugal Beltran Emma", "modulo": "Introducción"},
    {"fecha": "2026-03-12", "tema": "Líquidos y electrolitos en el paciente quirúrgico", "ponente": "López Félix Jesús Arturo", "modulo": "Bases Quirúrgicas"},
    {"fecha": "2026-03-17", "tema": "Nutrición en cirugía", "ponente": "Luna Borboa Jorge Luis", "modulo": "Bases Quirúrgicas"},
    {"fecha": "2026-03-24", "tema": "Anatomía anterior y posterior de la región inguinal", "ponente": "Almanza Orduño Athmir Antonio", "modulo": "Pared Abdominal"},
    {"fecha": "2026-03-25", "tema": "Fisiopatología y Genesis herniaria", "ponente": "Villegas Rodríguez José", "modulo": "Pared Abdominal"},
    {"fecha": "2026-03-26", "tema": "Hernia ventral primaria", "ponente": "Rendon Sánchez Manuel", "modulo": "Pared Abdominal"},
    {"fecha": "2026-04-14", "tema": "Hernia inguinal", "ponente": "Valdez Valdez Ricardo Antonio", "modulo": "Pared Abdominal"},
    {"fecha": "2026-04-15", "tema": "Técnica quirúrgica reparación Onlay", "ponente": "Soto Valle José Emaús", "modulo": "Pared Abdominal"},
    {"fecha": "2026-04-28", "tema": "Manejo abierto y mínima invasión en hernia inguinal", "ponente": "Cordero Medina Marielos", "modulo": "Pared Abdominal"},
    {"fecha": "2026-05-05", "tema": "Anatomía quirúrgica y fisiología del esófago", "ponente": "Portugal Beltran Emma", "modulo": "Cirugía digestiva"},
    {"fecha": "2026-05-06", "tema": "ERGE y esófago de Barrett", "ponente": "Rendon Sánchez Manuel", "modulo": "Cirugía digestiva"},
    {"fecha": "2026-06-17", "tema": "Apendicitis aguda", "ponente": "Maldonado Guardado Diana Guadalupe", "modulo": "Cirugía digestiva"}
]

# ==========================================
# FUNCIONES AUXILIARES
# ==========================================
def obtener_estado_residente(residente_nombre, fecha_actual):
    datos = RESIDENTES[residente_nombre]
    
    # Comprobar vacaciones
    for inicio, fin in datos["vacaciones"]:
        fecha_inicio = datetime.strptime(inicio, "%Y-%m-%d").date()
        fecha_fin = datetime.strptime(fin, "%Y-%m-%d").date()
        if fecha_inicio <= fecha_actual <= fecha_fin:
            return "🌴 Vacaciones"
    
    # Comprobar rotaciones (por mes)
    mes_actual = fecha_actual.month
    if mes_actual in datos["rotaciones"]:
        return f"🏥 Rotación: {datos['rotaciones'][mes_actual]}"
    
    return "✅ Hospital Civil (Servicio)"

def obtener_clases(fecha_actual):
    # Convertimos strings a objetos date
    clases_formateadas = []
    for c in CLASES:
        c_copia = c.copy()
        c_copia["fecha_date"] = datetime.strptime(c["fecha"], "%Y-%m-%d").date()
        clases_formateadas.append(c_copia)
        
    # Ordenar por fecha
    clases_formateadas = sorted(clases_formateadas, key=lambda x: x["fecha_date"])
    
    clase_hoy = next((c for c in clases_formateadas if c["fecha_date"] == fecha_actual), None)
    proximas_clases = [c for c in clases_formateadas if c["fecha_date"] > fecha_actual]
    proxima_clase = proximas_clases[0] if proximas_clases else None
    
    return clase_hoy, proxima_clase

# ==========================================
# BARRA LATERAL (SIDEBAR)
# ==========================================
st.sidebar.image("https://upload.wikimedia.org/wikipedia/commons/thumb/1/1a/Logo_de_la_Universidad_Aut%C3%B3noma_de_Sinaloa.svg/512px-Logo_de_la_Universidad_Aut%C3%B3noma_de_Sinaloa.svg.png", width=150)
st.sidebar.title("Navegación")
vista = st.sidebar.radio("Ir a:", ["🏠 Inicio (Dashboard)", "👨‍⚕️ Perfil por Residente", "📅 Calendario de Clases"])

st.sidebar.markdown("---")
st.sidebar.markdown("### 🗓️ Simulador de Fecha")
st.sidebar.info("Cambia la fecha aquí para ver cómo se actualizan las guardias, vacaciones y rotaciones.")
# Por defecto iniciamos en la fecha sugerida por el PDF para demostración
fecha_simulada = st.sidebar.date_input("Fecha actual:", date(2026, 3, 30))

# ==========================================
# VISTA: INICIO (DASHBOARD)
# ==========================================
if vista == "🏠 Inicio (Dashboard)":
    # ENCABEZADO
    col1, col2 = st.columns([1, 4])
    with col1:
        st.image("https://cdn-icons-png.flaticon.com/512/2966/2966327.png", width=100) # Icono genérico hospital/cirugía
    with col2:
        st.title("Programa Operativo 2026-2027")
        st.subheader("Especialidad en Cirugía General | CIDOCS / HCC")
    
    st.markdown("---")
    
    # SECCIÓN: CLASES
    clase_hoy, proxima_clase = obtener_clases(fecha_simulada)
    
    col_c1, col_c2 = st.columns(2)
    with col_c1:
        st.success("### 📚 Clase de Hoy")
        if clase_hoy:
            st.markdown(f"**Tema:** {clase_hoy['tema']}")
            st.markdown(f"**Módulo:** {clase_hoy['modulo']}")
            st.markdown(f"**Imparte:** 👨‍⚕️ {clase_hoy['ponente']} ({RESIDENTES[clase_hoy['ponente']]['grado']})")
        else:
            st.info("No hay clase programada para el día de hoy.")

    with col_c2:
        st.info("### 🔜 Próxima Clase")
        if proxima_clase:
            st.markdown(f"**Fecha:** {proxima_clase['fecha_date'].strftime('%d de %B, %Y')}")
            st.markdown(f"**Tema:** {proxima_clase['tema']}")
            st.markdown(f"**Imparte:** 👨‍⚕️ {proxima_clase['ponente']} ({RESIDENTES[proxima_clase['ponente']]['grado']})")
        else:
            st.warning("No hay clases futuras registradas.")

    st.markdown("---")
    
    # SECCIÓN: DISPONIBILIDAD DE RESIDENTES
    st.markdown(f"### 📍 Disponibilidad en el Servicio al **{fecha_simulada.strftime('%d/%m/%Y')}**")
    
    # Agrupar por grado
    grados = ["R4", "R3", "R2", "R1"]
    
    tabs = st.tabs(grados)
    
    for i, grado in enumerate(grados):
        with tabs[i]:
            res_grado = {k: v for k, v in RESIDENTES.items() if v["grado"] == grado}
            
            # Crear un dataframe para mostrarlo bonito
            datos_tabla = []
            for nombre, info in res_grado.items():
                estado = obtener_estado_residente(nombre, fecha_simulada)
                datos_tabla.append({"Residente": nombre, "Estado Actual": estado})
                
            df = pd.DataFrame(datos_tabla)
            
            # Estilizar filas basado en el estado
            def color_estado(val):
                if 'Vacaciones' in val: return 'background-color: #ffcccc; color: black'
                elif 'Rotación' in val: return 'background-color: #fff2cc; color: black'
                else: return 'background-color: #ccffcc; color: black'
            
            st.dataframe(df.style.applymap(color_estado, subset=['Estado Actual']), use_container_width=True, hide_index=True)


# ==========================================
# VISTA: PERFIL POR RESIDENTE
# ==========================================
elif vista == "👨‍⚕️ Perfil por Residente":
    st.title("Buscador de Residentes 🔍")
    
    lista_nombres = list(RESIDENTES.keys())
    residente_seleccionado = st.selectbox("Selecciona un residente:", lista_nombres)
    
    if residente_seleccionado:
        datos = RESIDENTES[residente_seleccionado]
        estado_actual = obtener_estado_residente(residente_seleccionado, fecha_simulada)
        
        col_p1, col_p2 = st.columns([1, 2])
        
        with col_p1:
            st.markdown(f"## {datos['grado']}")
            st.markdown(f"### {residente_seleccionado}")
            st.markdown(f"**Estado hoy:** {estado_actual}")
            st.image("https://cdn-icons-png.flaticon.com/512/3874/3874999.png", width=150) # Doctor icon
            
        with col_p2:
            st.markdown("### 📖 Proyecto de Tesis")
            st.info(datos['tesis'])
            
            st.markdown("### 🌴 Periodos Vacacionales")
            for inicio, fin in datos['vacaciones']:
                st.write(f"- Del **{inicio}** al **{fin}**")
                
            st.markdown("### 🏥 Rotaciones Externas (Meses)")
            if datos['rotaciones']:
                for mes, lugar in datos['rotaciones'].items():
                    meses = ["", "Ene", "Feb", "Mar", "Abr", "May", "Jun", "Jul", "Ago", "Sep", "Oct", "Nov", "Dic"]
                    st.write(f"- **{meses[mes]}:** {lugar}")
            else:
                st.write("- Sin rotaciones externas asignadas en este ciclo.")
                
        st.markdown("---")
        st.markdown("### 🎓 Clases a impartir y Sesiones Generales")
        
        # Mostramos las clases donde el ponente sea él, o donde participen TODOS (como los viernes)
        clases_residente = [c for c in CLASES if c["ponente"] == residente_seleccionado or c["ponente"] == "Todos los Residentes"]
        if clases_residente:
            df_clases = pd.DataFrame(clases_residente)[["fecha", "tipo", "modulo", "tema", "ponente"]]
            df_clases.columns = ["Fecha", "Tipo", "Módulo", "Tema", "Ponente"]
            st.table(df_clases)
        else:
            st.write("No tiene clases programadas en la base de datos actual.")

# ==========================================
# VISTA: CALENDARIO DE CLASES
# ==========================================
elif vista == "📅 Calendario de Clases":
    st.title("Calendario Completo de Clases Académicas")
    st.write("Temario de unidades didácticas y expositores")
    
    df_all_clases = pd.DataFrame(CLASES)[["fecha", "tipo", "modulo", "tema", "ponente"]]
    df_all_clases.columns = ["Fecha", "Tipo", "Módulo", "Tema de la Clase", "Ponente"]
    
    # Añadir grado al df
    df_all_clases["Grado"] = df_all_clases["Ponente"].apply(lambda x: RESIDENTES.get(x, {}).get("grado", ""))
    
    st.dataframe(df_all_clases, use_container_width=True, hide_index=True)
    
    st.caption("Nota: El calendario está sujeto a cambios por parte de la Jefatura de Enseñanza.")
