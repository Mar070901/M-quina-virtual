# 🤟 Amigo - Traductor de Texto a Lenguaje de Signos

# Índice

1. [Descripción](#descripción)
2. [Requisitos](#requisitos)
   - [Software y Bibliotecas](#software-y-bibliotecas)
   - [Instalación de Librerías](#instalación-de-librerías)
3. [Archivos del Proyecto](#archivos-del-proyecto)
4. [Funcionalidades](#funcionalidades)
5. [Ejemplo de Uso](#ejemplo-de-uso)
6. [Integración con Aplicaciones de Transcripción](#integración-con-aplicaciones-de-transcripción)
7. [Conclusión](#conclusión)


## Descripción
**Amigo** es una aplicación interactiva que transforma texto en lenguaje de signos utilizando una interfaz gráfica intuitiva y una máquina virtual basada en una pila de datos. Cada letra ingresada se convierte en su código ASCII, se almacena en una pila, y luego se muestra en la pantalla con su respectiva imagen en lenguaje de signos. Esta aplicación permite comprender conceptos de pila en un contexto visual y educativo.

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
pip install tkinter
```

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
  
## Integración con Aplicaciones de Transcripción
Para mejorar la accesibilidad, **Amigo** se puede combinar con aplicaciones de transcripción de voz. Estas aplicaciones permiten capturar voz y convertirla a texto, generando un

## Conclusión

Amigo - Traductor de Texto a Lenguaje de Signos es una herramienta innovadora diseñada para facilitar la comunicación de personas con dificultades auditivas y de habla. Al utilizar imágenes interactivas e infantiles, buscamos crear un ambiente accesible y atractivo que fomente el aprendizaje y la interacción. Este enfoque visual no solo ayuda a los usuarios a entender mejor el lenguaje de signos, sino que también les brinda una experiencia educativa enriquecedora.

Además, la posibilidad de integrar este proyecto con aplicaciones de transcripción de voz permite a los usuarios captar el habla y convertirla en texto. De esta forma, los usuarios pueden cargar fácilmente un archivo de texto en nuestra aplicación, lo que amplía aún más sus posibilidades de comunicación y aprendizaje. Amigo no solo promueve la inclusión, sino que también empodera a las personas a expresarse de manera efectiva y confiada.
