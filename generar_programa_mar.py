def generar_programa_mar(nombre_archivo_transcripcion, nombre_archivo_programa):
    try:
        with open(nombre_archivo_transcripcion, 'r', encoding='utf-8') as archivo:
            texto = archivo.read().strip()  # Lee y limpia el texto

        instrucciones = []

        # Almacenar caracteres en la pila (instrucciones para la máquina)
        for caracter in texto:
            if caracter.isalpha():  # Solo procesa letras
                valor_ascii = ord(caracter)
                instrucciones.append(f"push {valor_ascii}")  # Apilar cada letra
                instrucciones.append("show_sign")  # Mostrar la letra apilada

        # Guardar todas las instrucciones en el archivo .mar
        with open(nombre_archivo_programa, 'w', encoding='utf-8') as programa:
            for instruccion in instrucciones:
                programa.write(f"{instruccion}\n")

        print(f"{nombre_archivo_programa} generado exitosamente.")
    except OSError as e:
        print(f"Error al generar {nombre_archivo_programa}: {e}")
