[![Discord](https://discordapp.com/api/guilds/1235469363050577950/widget.png?style=shield)](https://discord.gg/zxkuUC2zeR)

## DISCLAIMER / DESCARGO DE RESPONSABILIDAD

- **Detección de Cheats**: Este proyecto no fue diseñado para ser indetectable y nunca tendrá ese objetivo.
- **Responsabilidad**: Este software está destinado únicamente para fines educativos. No me hago responsable de ningún baneo de cuenta, penalizaciones o cualquier otra consecuencia que pueda resultar del uso de esta herramienta. Úsala bajo tu propio riesgo y sé consciente de las posibles implicaciones.

## Instrucciones de Configuración

### 1. **Instalar Dependencias**:
   - Instala todas las dependencias necesarias ejecutando:
     ```bash
     pip install -r requirements.txt
     ```

### 2. **Configurar `settings.ini`**:
   - Ajusta la configuración en `settings.ini` según tus preferencias. Si quieres cambiar las teclas, puedes encontrar los valores [aquí](https://learn.microsoft.com/windows/win32/inputdev/virtual-key-codes).

### 3. **Configuración en el Juego**:
   - Establece tu sensibilidad del ratón en el juego a **0.5**.
   - Cambia el color de contorno de enemigos a **Púrpura**.
     
### 4. **Ejecutar el Colorbot**:
   - Ejecuta el script principal con:
     ```bash
     python main.py
     ```

## Controles

- **Aimbot**: Botón Derecho del Ratón (0x02)
- **Triggerbot**: Alt Derecho (0xA4)

## ¿Cómo Funciona el Programa?

### 🎯 **Funcionalidades Principales**

#### **1. Detección de Color**
- Captura una región de **200x150 píxeles** en el centro de tu pantalla
- Busca el **color púrpura** (contornos de enemigos en Valorant)
- Identifica las coordenadas exactas donde aparece ese color

#### **2. Aimbot (Apuntado Automático)**
- **Activación**: Mantén presionado el **botón derecho del ratón**
- **Función**: 
  - Detecta enemigos púrpuras en tu campo de visión
  - Mueve automáticamente tu ratón hacia el enemigo más cercano al centro
  - La velocidad se controla con `xSpeed` y `ySpeed` en `settings.ini`

#### **3. Triggerbot (Disparo Automático)**
- **Activación**: Mantén presionado **Alt Derecho**
- **Función**:
  - Vigila una región pequeña en el centro de tu mira
  - Si detecta color púrpura (enemigo), **dispara automáticamente**
  - Tiene delay aleatorio para parecer más humano

### 🎮 **Cómo Usar en Valorant**

1. **Prepara Valorant**:
   - Sensibilidad del ratón: **0.5**
   - Color de contorno de enemigos: **Púrpura**

2. **Durante el Juego**:
   - **Mantén presionado botón derecho** → El ratón se moverá hacia enemigos automáticamente
   - **Mantén presionado Alt Derecho** → Disparará cuando apuntes a un enemigo

3. **El Programa Detecta**:
   - Enemigos con contorno púrpura
   - Los trackea hacia tu mira
   - Dispara cuando están en el centro

### ⚙️ **Configuraciones Personalizables**

En `settings.ini` puedes ajustar:

#### **[Aimbot]**
- `xSpeed`, `ySpeed`: Velocidad de movimiento del ratón
- `xFov`, `yFov`: Campo de visión para detectar enemigos
- `targetOffset`: Precisión del apuntado

#### **[Triggerbot]**
- `minDelay`, `maxDelay`: Tiempo de reacción aleatorio (en milisegundos)
- `xRange`, `yRange`: Área de detección para el disparo automático

### 🔧 **Modificaciones Técnicas**

Este proyecto ha sido **completamente adaptado** para funcionar **sin Arduino**:
- ❌ **Eliminado**: Dependencia de hardware Arduino
- ✅ **Agregado**: Control directo del ratón usando `pyautogui`
- ✅ **Mantenido**: Toda la funcionalidad de detección y aimbot/triggerbot
- ✅ **Mejorado**: Configuración más simple y directa

### ⚠️ **Notas Importantes**

- El programa funciona detectando **únicamente el color púrpura**
- Funciona en **tiempo real** capturando la pantalla
- **No requiere hardware adicional** (sin Arduino)
- Es **detectable** por software anticheat
- Uso bajo **tu propio riesgo**

---

**🎯 ¡Disfruta del colorbot sin Arduino!**
