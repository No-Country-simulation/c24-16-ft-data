# **🌍 Energía Global ⚡**

<!--Este es un dashboard interactivo construido con **Dash y Plotly**, que permite visualizar datos de generación y consumo de energía a nivel global y por país. Se basa en el conjunto de datos de [Our World in Data](https://ourworldindata.org/energy).-->


## 📄 Descripción del proyecto
El proyecto tiene como objetivo ofrecer un sistema interactivo que permita visualizar y analizar datos relacionados con la energía a nivel global, lo que incluye el consumo de energía, la producción de fuentes renovables y no renovables, las emisiones de CO2, y las políticas energéticas de diferentes países. Se basa en el conjunto de datos de [Our World in Data](https://ourworldindata.org/energy). A través de un dashboard, los usuarios podrán entender las tendencias globales, comparar diferentes regiones y tomar decisiones informadas sobre el futuro energético.

## 👥 Descripción del equipo y roles
- **Ana Santos** - *Project Manager* : Responsable de la coordinación del equipo y la gestión del proyecto.
- **Eglimar Ramirez** - *Data Science* : Responsable de detectar patrones de datos, y representar tendencias y predicciones.
- **Cristobal Ramirez** - *Data Analyst* : Responsable del análisis de datos y creación de visualizaciones en Dash.
- **Raul Tezen** - *Data Analyst* : Responsable del análisis de datos y creación de visualizaciones en Dash.

## 📇 Metodología de trabajo 
Para el desarrollo de este proyecto, se ha elegido la metodología ágil Scrum, debido a su enfoque iterativo e incremental que favorece la flexibilidad y la adaptación continua a los cambios, características clave para un entorno dinámico. Scrum permite dividir el proyecto en ciclos de trabajo cortos y manejables, denominados sprints, lo que facilita la entrega constante de valor y la retroalimentación temprana por parte del cliente.

## 🗓️ Cronograma
En proceso


## 🛠️ Herramientas implementadas

En proceso

## 📌 Características
✔ Filtrado por país o vista global.  
✔ Visualización de las **10 principales fuentes de energía** en cada año.  
✔ Comparación de **generación vs. demanda de electricidad**.  
✔ **Gráficos interactivos** con sliders y opciones de selección.  
✔ **Diseño modular** con código organizado en `scripts/`.


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
✅ **Soporte para múltiples gráficos interactivos.**  

---

## 🚀 Próximas Mejoras
- 💨 Añadir predicciones con Machine Learning 📈  
- 🌱 Gráficos de emisiones de CO₂ y eficiencia energética 🌿  
- 🔥 Comparación de energías renovables vs. fósiles ⚡️  
- 📂 Exportación de datos y gráficos en PDF o CSV 📊  
- ❓ Alguna otra idea que se nos ocurra a lo largo del proyecto 🎲

---

🚀 **¡Disfruta explorando los datos de energía!** 🌍⚡

