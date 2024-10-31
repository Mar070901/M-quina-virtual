#### 🤟 Amigo - Traductor de Texto a Lenguaje de Signos

## Descripción
**Amigo** es una aplicación interactiva que transforma texto en lenguaje de signos utilizando una interfaz gráfica intuitiva y una máquina virtual basada en una pila de datos. Cada letra ingresada se convierte en su código ASCII, se almacena en una pila, y luego se muestra en la pantalla con su respectiva imagen en lenguaje de signos. Esta aplicación permite comprender conceptos de pila en un contexto visual y educativo.

## Archivos del Proyecto
- **`main.py`**: Programa principal que ejecuta la interfaz gráfica para ingresar texto y visualizar las imágenes correspondientes en lenguaje de signos.
- **`maquina_virtual.py`**: Implementa la máquina virtual que ejecuta las instrucciones en la pila y gestiona la visualización de las imágenes.
- **`traductor.py`**: Convierte el texto en instrucciones de pseudo-ensamblador para ser ejecutado por la máquina virtual.
- **`generar_programa.py`**: Toma el texto de entrada y lo guarda en un archivo `.mar` con las instrucciones generadas.
- **`instructions.py`**: Define las instrucciones usadas por la máquina virtual.

## Funcionalidades

1. **Generación de archivo `.mar`**: Convierte cada letra en el texto a su código ASCII y genera un archivo `.mar` que contiene las instrucciones `push` y `show_sign`.
2. **Máquina Virtual para ejecutar el programa**: La máquina virtual lee el archivo `.mar` y ejecuta cada instrucción, mostrando imágenes de signos basados en el texto ingresado.
3. **Interfaz Gráfica Interactiva (Tkinter)**: Permite al usuario ingresar texto y gestionar el proceso de traducción y visualización con botones fáciles de usar.

## Ejemplo de Uso

- **Interacción visual**: Al ingresar texto en el área de entrada, la máquina virtual procesa cada carácter y muestra una imagen asociada. Cada letra se convierte en un espectáculo visual, ideal para ilustrar conceptos de ensamblador y sistemas de pila.
- **Output de instrucciones**: Genera y guarda automáticamente el archivo `.mar` con las instrucciones generadas, que se pueden reutilizar o visualizar.

## Requisitos
### Software y Bibliotecas
- **Python 3.7+**
- **Bibliotecas**:
  - `tkinter`: Para la interfaz gráfica (suele venir preinstalada con Python).
  - `Pillow`: Para cargar y mostrar las imágenes en lenguaje de signos.

### Instalación de Librerías
Para instalar `Pillow`, ejecuta:
```bash
pip install pillow
