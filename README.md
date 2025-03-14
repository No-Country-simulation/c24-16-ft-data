# **🌍 Energía Global ⚡**

## 📄 Descripción del proyecto

El proyecto tiene como objetivo ofrecer un sistema interactivo que permita visualizar y analizar datos relacionados con la energía a nivel global, lo que incluye el consumo de energía, la producción de fuentes renovables y no renovables, las emisiones de CO2, y las políticas energéticas de diferentes países. Se basa en el conjunto de datos de [Our World in Data](https://ourworldindata.org/energy). A través de un dashboard, los usuarios podrán entender las tendencias globales, comparar diferentes regiones y tomar decisiones informadas sobre el futuro energético.

## 👥 Descripción del equipo y roles

- **Ana Santos** - _Project Manager_ : Responsable de la coordinación del equipo y la gestión del proyecto.
- **Cristobal Ramirez** - _Data Analyst_ : Responsable del análisis de datos y creación de visualizaciones en Dash.
- **Raul Tezen** - _Data Analyst_ : Responsable del análisis de datos y creación de visualizaciones en Dash.

## 📇 Metodología de trabajo

Para el desarrollo de este proyecto, se ha elegido la metodología ágil Scrum, debido a su enfoque iterativo e incremental que favorece la flexibilidad y la adaptación continua a los cambios, características clave para un entorno dinámico. Scrum permite dividir el proyecto en ciclos de trabajo cortos y manejables, denominados sprints, lo que facilita la entrega constante de valor y la retroalimentación temprana por parte del cliente.

## 🛠️ Herramientas implementadas

<table>
  <tr>
    <th>Librería/Herramienta</th>
    <th>Logo</th>
    <th>Descripción</th>
  </tr>
  <tr>
    <td><strong>Pandas</strong></td>
    <td align="center"><img src="https://upload.wikimedia.org/wikipedia/commons/e/ed/Pandas_logo.svg" width="40"></td>
    <td>Librería de Python para manipulación y análisis de datos.</td>
  </tr>
  <tr>
    <td><strong>Jupyter</strong></td>
    <td align="center"><img src="https://upload.wikimedia.org/wikipedia/commons/3/38/Jupyter_logo.svg" width="40"></td>
    <td>Software gratuito, estándares abiertos y servicios web para informática interactiva en todos los lenguajes de programación.</td>
  </tr>
  <tr>
    <td><strong>Visual Studio Code</strong></td>
    <td align="center"><img src="https://upload.wikimedia.org/wikipedia/commons/9/9a/Visual_Studio_Code_1.35_icon.svg" width="40"></td>
    <td>Editor de código fuente.</td>
  </tr>
  <tr>
    <td><strong>Python</strong></td>
    <td align="center"><img src="https://upload.wikimedia.org/wikipedia/commons/c/c3/Python-logo-notext.svg" width="40"></td>
    <td>Lenguaje de programación utilizado para análisis de datos y desarrollo de aplicaciones.</td>
  </tr>
  <tr>
    <td><strong>GitHub</strong></td>
    <td align="center"><img src="https://upload.wikimedia.org/wikipedia/commons/9/91/Octicons-mark-github.svg" width="40"></td>
    <td>Plataforma de desarrollo colaborativo para proyectos de software.</td>
  </tr>
  <tr>
    <td><strong>Google Drive</strong></td>
    <td align="center"><img src="https://upload.wikimedia.org/wikipedia/commons/d/da/Google_Drive_logo.png" width="40"></td>
    <td>Servicio de alojamiento y sincronización de archivos.</td>
  </tr>
  <tr>
    <td><strong>Google Meet</strong></td>
    <td align="center"><img src="https://upload.wikimedia.org/wikipedia/commons/9/9b/Google_Meet_icon_%282020%29.svg" width="40"></td>
    <td>Herramienta utilizada para las videollamadas y reuniones.</td>
  </tr>
</table>

---

## 📌 Características

✔ Filtrado por país o vista global.  
✔ Visualización de las **10 principales fuentes de energía** en cada año.  
✔ Comparación de **generación vs. demanda de electricidad**.  
✔ **Gráficos interactivos** con sliders y opciones de selección.  

## 🛠 Instalación y Configuración

### **1 Clonar el Repositorio**

```bash
git clone https://github.com/No-Country-simulation/c24-16-ft-data
```

### **2 Crear un Entorno Virtual (Opcional pero Recomendado)**

```bash
python -m venv venv  # Crear entorno virtual
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate  # Windows
```

### **3 Instalar Dependencias**

```bash
pip install -r requirements.txt
```

### **4 Ejecutar la Aplicación**

```bash
python app.py
```

La aplicación estará disponible en:  
📍 `http://127.0.0.1:8050/`

---

## 📎 Estructura del Proyecto

```
energy-dashboard/
│── app.py  # Archivo principal que ejecuta Dash
│── requirements.txt  # Lista de dependencias
│── README.md  # Documentación del proyecto
│── scripts/  # Código modular
│   │── __init__.py  # Importación automática de módulos
│   │── data_processing.py  # Carga y procesamiento de datos
│   │── layout.py  # Diseño del dashboard
│   │── callbacks.py  # Funciones interactivas
│── data/  # Datos CSV
│   │── owid-energy-data.csv  # Fuente de datos
│── notebooks/  # Aquí irán los notebooks explicando mejor el código
```

---

## 🛠 Funciones Actuales

✅ **Visualización de las 10 principales fuentes de energía** con slider de años.  
✅ **Gráfico dinámico** de generación vs. demanda de electricidad.  
✅ **Filtrado por país o visión global.**  

---

🚀 **¡Disfruta explorando los datos de energía!** 🌍⚡
