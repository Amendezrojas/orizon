import pandas as pd

# Datos del CHECK LIST-RECEPCION DE INSUMOS CARGAS PELIGROSAS
data_recepcion_checklist_items = {
    "Descripción": [
        "VERIFICAR QUE EL CAMION CUENTA CON LETRERO DE IDENTIFICACION CON EL PELIGRO",
        "EMBALAJE EXTERNO DEBE ESTAR MARCADO Y ETIQUETADO SEGÚN SU CLASIFICACION",
        "VERIFICAR QUE LA CARGA SE DISTOTRIBUYE DE MANERA SEGURA Y SUJETA CON MEDIOS APROPIADOS",
        "VERIFICAR QUE LA CARGA NO TENGA RIESGO DE INCOMPATIBILIDAD",
        "SUSTANCIAS INCOMPATIBLES ENTRE SI, SE DEBEN DISTRIBUIR DE MANERA SEPARADA EN EL TRANSPORTE",
        "DETENER EL MOTOR MIENTRAS SE REALIZA ACTIVIDAD DE DESCARGA DE CARGAS PELIGROSAS",
        "EN ACTIVIDAD DE DESCARGA, INMOVILIZAR EL VEHICULO MEDIANTE CUÑAS U OTROS ELEMENTOS QUE EVITE EL DESPLAZAMIENTO",
        "EL CONDUCTOR NO PARTICIPARA EN LA OPERACIÓN DE CARGA, DESCARGA O TRANSBORDO, SOLO EN CASO DE ESTAR DEBIDAMENTE AUTORIZADO",
        "EL PERSONAL QUE REALIZA OPERACIONES DE CARGA, DESCARGA Y TRANSBORDO DE CARGAS PELIGROSAS DEBE UTILIZAR VESTIMENTA ADECUADA EPP",
        "CUENTA CON GUIA DE DESPACHO",
        "GUIA DE DESPACHO COINCIDE CON EL MATERIAL PELIGROSO TRANSPORTADO",
        "SE INSTALARON CONOS EN CANTIDAD NECESARIA ANTES DE INICIAR CARGA O DESCARGA DE MATERIALES PELIGROSOS",
        "CAMION TIENE BALIZA OPERATIVA",
        "LUCES DE CAMION ESTAN OPERATIVAS",
        "PERSONAL TIENE CAPACITACION DE RESIDUOS PELIGROSOS",
        "HOJAS DE SEGURIDAD DE MATERIALES PELIGROSOS TRANSPORTADOS",
        "PRODUCTOS PELIGROSOS ESTAN SUJETOS CON MEDIOS APROPIADOS PARA EVITAR DESPLAZAMIENTO",
        "CALLE ESTA CERRADA ANTES DE INICIAR CARGA O DESCARGA DE MATERIALES PELIGROSOS"
    ],
    "Cumple (Sí/No)": [
        "NO", "Si", "NO", "Si", "Si", "Si", "NO", "Si", "Si", "Si", "NO", "Si", "NO", "NO", "NO", "NO", "NO", "NO"
    ]
}

df_recepcion = pd.DataFrame(data_recepcion_checklist_items)

# Agregamos la información del encabezado, repitiéndola para cada fila
num_rows_recepcion = len(df_recepcion)
df_recepcion['Fecha de Recepción'] = ["08-07-2025"] * num_rows_recepcion
df_recepcion['Proveedor'] = ["RENSTO LO PE PACKERS"] * num_rows_recepcion
df_recepcion['Patente'] = ["KBxj67"] * num_rows_recepcion
df_recepcion['Nombre Conductor'] = ["RENSTO LO PE PACKERS."] * num_rows_recepcion

# Reordenar las columnas para que el encabezado esté al principio
df_recepcion = df_recepcion[['Fecha de Recepción', 'Proveedor', 'Patente', 'Nombre Conductor', 'Descripción', 'Cumple (Sí/No)']]

# Datos del CHECK LIST CAMION AMPLIRROL
data_amplirrol = {
    "Puntos a considerar": [
        "Luces bajas", "Luces altas", "intermitentes", "Luces retroceso", "Alarma retroceso",
        "chasis", "neumáticos", "frenos", "Freno de mano", "extintor", "conos",
        "Cinturón de seguridad", "Licencia de conducir", "Rombo peligrosidad y NU",
        "Baliza", "Guía de despacho", "Hojas de seguridad", "Resolución del camión"
    ],
    "Cumple (X en No/Si)": [
        "X (No)", "X (No)", "X (No)", "X (No)", "X (No)", "Si", "Si", "X (No)", "X (No)", "Si", "Si",
        "Si", "Si", "X (No)", "X (No)", "Si", "X (No)", "Si"
    ],
    "Observaciones": [
        "NO Alumbran lo suficiente", "NO Alumbran de forma correcta.", "Tiene algunas rotas",
        "Existen, pero no funcionan", "No tiene.", "No evidencia deterioro", "En buen estado",
        "Frenos (traseros, delanteros) en mal estado.", "Freno sin reemplazo", "Cumple", "Cumple",
        "Cumple.", "Cumple.", "No tiene", "No tiene", "Cumple", "No tiene", "Cumple"
    ]
}

df_amplirrol = pd.DataFrame(data_amplirrol)

# Función para convertir DataFrame a HTML
def df_to_html(df, title):
    html_string = f"<h2>{title}</h2>"
    html_string += df.to_html(index=False, escape=False)
    return html_string

# Generar HTML para ambos DataFrames
html_recepcion = df_to_html(df_recepcion, "CHECK LIST - RECEPCIÓN DE INSUMOS CARGAS PELIGROSAS")
html_amplirrol = df_to_html(df_amplirrol, "CHECK LIST CAMIÓN AMPLIRROL")

# Unir ambos HTML en un solo documento
full_html = f"""
<!DOCTYPE html>
<html>
<head>
    <title>Reporte de Checklists Newen</title>
    <style>
        body {{ font-family: sans-serif; margin: 20px; }}
        table {{ width: 100%; border-collapse: collapse; margin-bottom: 30px; }}
        th, td {{ border: 1px solid #ddd; padding: 8px; text-align: left; }}
        th {{ background-color: #f2f2f2; }}
        h1, h2 {{ color: #333; }}
        .header {{ background-color: #4CAF50; color: white; padding: 10px; text-align: center; }}
        .section {{ margin-top: 40px; border-top: 2px solid #ccc; padding-top: 20px; }}
        .deficiency {{ background-color: #ffe0e0; }}
        .compliant {{ background-color: #e0ffe0; }}
        .action {{ font-weight: bold; color: #0056b3; }}
    </style>
</head>
<body>
    <div class="header">
        <h1>Reporte Detallado de Checklists Newen</h1>
        <p>Generado el {pd.Timestamp.now().strftime('%d-%m-%Y %H:%M:%S')}</p>
        <p>Ubicación: Concepción, Bio Bio, Chile</p>
    </div>

    <div class="section">
        {html_recepcion}
    </div>

    <div class="section">
        {html_amplirrol}
    </div>

    <div class="section">
        <h2>Análisis y Recomendaciones Clave</h2>
        <h3>Preocupaciones del Coordinador (Equipos y Logística)</h3>
        <ul>
            <li>**Mantenimiento del Vehículo y Características de Seguridad:** Reparación inmediata de luces (bajas, altas, intermitentes, retroceso), instalación/reparación de balizas y alarmas de retroceso. Revisión urgente del sistema de frenos y freno de mano. Asegurar señalización de identificación de peligros en camiones. Proveer y hacer cumplir el uso de mecanismos de sujeción de carga y equipo de inmovilización (cuñas).</li>
            <li>**Documentación y Cumplimiento (Vehículo/Carga):** Implementar verificación cruzada rigurosa para que la guía de despacho coincida con el material peligroso. Asegurar rombos de peligrosidad y números NU visibles. Todas las hojas de seguridad (SDS) deben estar presentes y accesibles. Monitorear proactivamente el vencimiento de la revisión técnica.</li>
            <li>**Procedimientos Operativos:** Establecer y hacer cumplir protocolos estrictos para el cierre de calles durante carga/descarga de materiales peligrosos. Asegurar manejo adecuado de materiales sobre paletas.</li>
        </ul>

        <h3>Preocupaciones de Supervisión (Personal y Capacitación)</h3>
        <ul>
            <li>**Capacitación Obligatoria en Seguridad:** Capacitación integral en residuos peligrosos para todo el personal involucrado. Capacitación específica en procedimientos seguros de carga/descarga/transbordo. Entrenamiento en respuesta a emergencias (derrames, accidentes).</li>
            <li>**Equipo de Protección Personal (EPP):** Hacer cumplir estrictamente el uso de EPP adecuado y completo para todo el personal en operaciones de materiales peligrosos.</li>
            <li>**Autorización e Implicación del Conductor:** Clarificar roles y asegurar que los conductores solo participen en carga/descarga si están autorizados y capacitados.</li>
            <li>**Mejora Continua:** Realizar auditorías regulares sin previo aviso. Establecer un mecanismo de retroalimentación para reportar condiciones inseguras. Reforzar continuamente el cumplimiento del D.S.N 28.</li>
        </ul>

        <h3>Comunicación Entre el Equipo y los Clientes</h3>
        <ul>
            <li>**Protocolo de Comunicación Estandarizado:** Desarrollar una lista de verificación/acuerdo pre-servicio con todos los requisitos para materiales peligrosos, a compartir y acordar con clientes antes del servicio. Solicitar requisitos detallados (clasificaciones, cantidades, instrucciones, documentación) con antelación. Establecer puntos de contacto claros.</li>
            <li>**Intercambio Proactivo de Información:** Informar proactivamente a los clientes sobre los preparativos necesarios de su parte. Establecer un canal de comunicación inmediato para reportar incidentes o discrepancias.</li>
            <li>**Bucle de Retroalimentación con los Clientes:** Realizar revisiones post-servicio para recopilar comentarios. Involucrar a los clientes en la resolución conjunta de problemas.</li>
        </ul>
    </div>
</body>
</html>
"""

# Guardar el HTML en un archivo
with open("reporte_checklists_newen.html", "w", encoding="utf-8") as f:
    f.write(full_html)

print("Se ha generado el archivo 'reporte_checklists_newen.html' con los datos y el análisis.")
print("Puedes abrir este archivo en tu navegador web para visualizar el informe.")