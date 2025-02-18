# 🌍 Dashboard de Energía Global ⚡

Este es un dashboard interactivo construido con **Dash y Plotly**, que permite visualizar datos de generación y consumo de energía a nivel global y por país. Se basa en el conjunto de datos de [Our World in Data](https://ourworldindata.org/energy).

---

## 📌 **Características**
✔ Filtrado por país o vista global.  
✔ Visualización de las **10 principales fuentes de energía** en cada año.  
✔ Comparación de **generación vs. demanda de electricidad**.  
✔ **Gráficos interactivos** con sliders y opciones de selección.  
✔ **Diseño modular** con código organizado en `scripts/`.

---

## 🛠 **Instalación y Configuración**
### **1⃣ Clonar el Repositorio**
```bash
git clone https://github.com/No-Country-simulation/c24-16-ft-data
```

### **2⃣ Crear un Entorno Virtual (Opcional pero Recomendado)**
```bash
python -m venv venv  # Crear entorno virtual
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate  # Windows
```

### **3⃣ Instalar Dependencias**
```bash
pip install -r requirements.txt
```

### **4⃣ Ejecutar la Aplicación**
```bash
python app.py
```
La aplicación estará disponible en:  
📍 `http://127.0.0.1:8050/`

---

## 📎 **Estructura del Proyecto**
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

## 🛠 **Funciones Actuales**
✅ **Visualización de las 10 principales fuentes de energía** con slider de años.  
✅ **Gráfico dinámico** de generación vs. demanda de electricidad.  
✅ **Filtrado por país o visión global.**  
✅ **Soporte para múltiples gráficos interactivos.**  

---

## 🚀 **Próximas Mejoras**
💨 **Añadir predicciones con Machine Learning** 📈  
🌱 **Gráficos de emisiones de CO₂ y eficiencia energética** 🌿  
🔥 **Comparación de energías renovables vs. fósiles** ⚡️  
📂 **Exportación de datos y gráficos en PDF o CSV** 📊
❓ **Alguna otra idea que se nos ocurra a lo largo del proyecto**🎲

---

🚀 **¡Disfruta explorando los datos de energía!** 🌍⚡

