import os
import win32api
from colorbot import Colorbot

def main():
    """
    Función principal que inicializa y ejecuta el colorbot sin Arduino
    """
    # Limpiar pantalla y establecer título
    os.system('cls')
    os.system('title Valorant Colorbot (Sin Arduino)')
    
    print("=== Valorant Colorbot (Sin Arduino) ===")
    print("Enemy Outline Color: Purple")
    
    # Obtener resolución de pantalla
    screen_width = win32api.GetSystemMetrics(0)
    screen_height = win32api.GetSystemMetrics(1)
    
    # Calcular región de captura (centro de pantalla)
    fov_width = 200
    fov_height = 150
    
    capture_region = [
        screen_width // 2 - fov_width // 2,
        screen_height // 2 - fov_height // 2,
        fov_width,
        fov_height
    ]
    
    center_x = screen_width // 2
    center_y = screen_height // 2
    
    print(f"Resolución: {screen_width}x{screen_height}")
    print(f"Región de captura: {capture_region}")
    print("\nPresiona Ctrl+C para salir")
    print("-" * 40)
    
    # Iniciar colorbot
    colorbot = Colorbot(capture_region, center_x, center_y)
    colorbot.listen()

if __name__ == '__main__':
    main()