"""
Este codigo utiliza el uso de la cpu para identificar cuando la llamada
se finalizó y así minimizar la ventana
JUSTIFICACION: en la pantalla el usuario debe disponer de la ventana de
llamada, no debe verse ninguna otra ventana de Skype.
"""
import psutil
import time
import keyboard
import pyautogui
def detectar_enter():
    print("Presiona Enter para iniciar y esperar el inicio de la llamada...")
    keyboard.wait('enter')
    print("Enter presionado. Esperando inicio de la llamada...")

def esperar_inicio_llamada():
    print("Esperando inicio de la llamada...")
    # Obtener el uso de CPU de los procesos de Skype al inicio
    cpu_uso_inicial = obtener_uso_cpu_skype()
    print("Inicio de la llamada detectado.")

def esperar_fin_llamada_skype():
    print("Esperando fin de la llamada...")
    while True:
        # Esperar hasta que el uso de CPU de los procesos de Skype vuelva a niveles normales
        if not hay_llamada_en_progreso():
            pyautogui.hotkey('alt', 'Esc')
            print("Llamada de Skype finalizada.")
            break
        time.sleep(1)

def obtener_uso_cpu_skype():
    # Obtener la lista de procesos de Skype
    procesos_skype = [p for p in psutil.process_iter() if "Skype" in p.name()]
    # Calcular el uso de CPU total de los procesos de Skype
    cpu_total = sum(p.cpu_percent() for p in procesos_skype)
    return cpu_total

def hay_llamada_en_progreso():
    # Esperar hasta que el uso de CPU de los procesos de Skype vuelva a niveles normales
    return obtener_uso_cpu_skype() > 0

# Ejemplo de uso:
detectar_enter()
esperar_inicio_llamada()
esperar_fin_llamada_skype()
