import subprocess
import time
import keyboard
import pygetwindow as gw

def hacer_llamada_skype():
    # Obtener la ventana de Skype
    skype_window = gw.getWindowsWithTitle("Skype")
    if skype_window:
        # Ajustar el tamaño de la ventana de Skype
        skype_window[0].width = 100  # Definir el ancho mínimo deseado
        skype_window[0].height = 100  # Definir el alto mínimo deseado

    # Reemplaza "tusitio" con el nombre de usuario de Skype al que deseas llamar.
    skype_username = "live:oligna11_1"
    skype_uri = f"skype:{skype_username}?call"
    
    # Ejecutar el comando para abrir la aplicación de Skype con el enlace de Skype URI
    subprocess.call(["start", skype_uri], shell=True)
    
    # Esperar un tiempo suficiente para que la ventana de Skype se abra
    time.sleep(5)  # Espera 5 segundos (puedes ajustar este valor según sea necesario)
    
    # Minimizar la ventana de Skype utilizando un atajo de teclado
    keyboard.send('alt+space')  # Combinación de teclas para abrir el menú de la ventana
    time.sleep(0.1)  # Espernar un breve momento antes de enviar la siguiente tecla
    keyboard.send('n')  # Tecla para minimizar la ventana (puede variar según el idioma del sistema)
    
    # Esperar un momento para que la ventana se minimice completamente
    time.sleep(1)
    
    

# Ejemplo de uso: llama a la función hacer_llamada_skype.
if __name__ == "__main__":
    hacer_llamada_skype()
