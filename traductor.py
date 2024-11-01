def leer_archivo_y_traducir(texto):
    programa = []
    for caracter in texto:
        if caracter.isalpha():  # Solo traducimos letras
            codigo_ascii = ord(caracter)
            programa.append(('push', codigo_ascii))  # Guardamos el código ASCII en el orden del texto
            programa.append(('show_sign',))  # Agregamos una instrucción para mostrar la imagen

    # Añadir una instrucción 'end' para detener la ejecución de la máquina
    programa.append(('end',))

    return programa

def generar_programa_mar(texto, nombre_archivo_mar):
    # Generar instrucciones a partir del texto ingresado
    programa = leer_archivo_y_traducir(texto)

    # Guardar las instrucciones en el archivo .mar
    with open(nombre_archivo_mar, 'w') as archivo:
        for instruccion in programa:
            if len(instruccion) == 2:
                archivo.write(f"{instruccion[0]} {instruccion[1]}\n")
            else:
                archivo.write(f"{instruccion[0]}\n")
    
    print(f"Programa generado y guardado en {nombre_archivo_mar}")
