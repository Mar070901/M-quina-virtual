import os
from PIL import Image
import time

class MaquinaVirtual:
    def __init__(self):
        self.pila = []
        self.programa = []
        self.pc = 0  # Contador de programa

    def cargar_programa(self, programa):
        self.pila = []  # Reinicia la pila
        self.pc = 0  # Reinicia el contador de programa
        self.programa = programa  # Cargar el programa de instrucciones

    def ejecutar(self):
        # Procesamos todas las instrucciones
        while self.pc < len(self.programa):
            instruccion = self.programa[self.pc]
            self.pc += 1  # Incrementa el contador de programa
            op = instruccion[0]
            
            if op == 'push':
                self.push(instruccion[1])
            elif op == 'show_sign':
                self.mostrar_signo()
            elif op == 'swap':
                self.swap()
            elif op == 'pop':
                self.pop()
            elif op == 'top':
                self.top()

        # Imprimir el contenido final de la pila al terminar
        contenido_pila = [chr(valor) for valor in self.pila]
        print("Contenido final de la pila:", contenido_pila)

    def push(self, valor):
        self.pila.append(valor)
        print(f"Pushed {chr(valor)}")

    def mostrar_signo(self):
        if self.pila:
            ascii_value = self.pila[-1]  # Último valor apilado
            letra = chr(ascii_value).lower()
            image_path = f"C:/Users/mar_a/OneDrive/Escritorio/3º/LYP/MV/imagenes/{letra}.png"
            
            try:
                if os.path.exists(image_path):
                    img = Image.open(image_path)
                    img.show()
                    time.sleep(3)  # Muestra la imagen durante 1 segundo antes de continuar
                else:
                    print(f"Imagen para la letra '{letra.upper()}' no encontrada en: {image_path}")
            except Exception as e:
                print(f"Error al abrir la imagen: {e}")
        else:
            print("La pila está vacía, no hay signo para mostrar.")

    def swap(self):
        if len(self.pila) >= 2:
            self.pila[-1], self.pila[-2] = self.pila[-2], self.pila[-1]
            print("Swapped the top two elements.")
        else:
            print("Error: no se puede intercambiar, la pila no tiene suficientes elementos.")

    def pop(self):
        if self.pila:
            valor = self.pila.pop()
            print(f"Popped {chr(valor)}")
        else:
            print("Error: no hay elementos para hacer pop.")

    def top(self):
        if self.pila:
            print(f"Top element: {chr(self.pila[-1])}")
        else:
            print("La pila está vacía, no hay elementos para mostrar.")
