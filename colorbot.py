import cv2
import numpy as np
import threading
import time
import random
import win32api
from capture import Capture
from mouse import Mouse
from settings import Settings

class Colorbot:
    """
    The Colorbot class handles screen capturing, color detection, and mouse control.
    It supports aiming at specific colors on the screen and triggering actions when
    the color is within a defined region.
    """

    def __init__(self, capture_region, center_x, center_y):
        """
        Initializes the Colorbot with screen capture parameters.

        Args:
            capture_region (list): [x, y, width, height] of the capture area.
            center_x (int): X-coordinate of the screen center.
            center_y (int): Y-coordinate of the screen center.
        """
        self.capture = Capture()
        self.mouse = Mouse()
        self.settings = Settings()
        self.capture_region = capture_region
        self.center_x = center_x
        self.center_y = center_y
        
        # Estados
        self.aimbot_enabled = False
        self.triggerbot_enabled = False
        self.running = True
        
    def detect_color(self, frame):
        """Detecta el color púrpura (enemigos en Valorant)"""
        # Convertir BGR a HSV
        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
        
        # Rango de color púrpura para enemigos
        lower_purple = np.array([130, 50, 50])
        upper_purple = np.array([160, 255, 255])
        
        # Crear máscara
        mask = cv2.inRange(hsv, lower_purple, upper_purple)
        
        # Encontrar contornos
        contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        
        targets = []
        for contour in contours:
            if cv2.contourArea(contour) > 10:  # Filtrar contornos pequeños
                M = cv2.moments(contour)
                if M["m00"] != 0:
                    cx = int(M["m10"] / M["m00"])
                    cy = int(M["m01"] / M["m00"])
                    targets.append((cx, cy))
        
        return targets
    
    def get_closest_target(self, targets):
        """Encuentra el objetivo más cercano al centro"""
        if not targets:
            return None
            
        center_x = self.capture_region[2] // 2
        center_y = self.capture_region[3] // 2
        
        closest = None
        min_distance = float('inf')
        
        for target in targets:
            distance = ((target[0] - center_x) ** 2 + (target[1] - center_y) ** 2) ** 0.5
            if distance < min_distance:
                min_distance = distance
                closest = target
                
        return closest
    
    def aimbot_thread(self):
        """Hilo del aimbot"""
        while self.running:
            if self.aimbot_enabled and self.mouse.is_connected():
                try:
                    # Capturar pantalla
                    frame = self.capture.get_screenshot(self.capture_region)
                    
                    # Detectar objetivos
                    targets = self.detect_color(frame)
                    closest = self.get_closest_target(targets)
                    
                    if closest:
                        # Calcular movimiento necesario
                        center_x = self.capture_region[2] // 2
                        center_y = self.capture_region[3] // 2
                        
                        dx = closest[0] - center_x
                        dy = closest[1] - center_y
                        
                        # Aplicar velocidad y límites de FOV
                        if abs(dx) <= self.settings.aimbot_x_fov and abs(dy) <= self.settings.aimbot_y_fov:
                            move_x = dx * self.settings.aimbot_x_speed
                            move_y = dy * self.settings.aimbot_y_speed
                            
                            # Mover ratón
                            self.mouse.move(int(move_x), int(move_y))
                            
                except Exception as e:
                    pass
                    
            time.sleep(0.01)  # 100 FPS
    
    def triggerbot_thread(self):
        """Hilo del triggerbot"""
        while self.running:
            if self.triggerbot_enabled and self.mouse.is_connected():
                try:
                    # Capturar región pequeña del centro
                    small_region = [
                        self.capture_region[0] + self.capture_region[2]//2 - self.settings.triggerbot_x_range,
                        self.capture_region[1] + self.capture_region[3]//2 - self.settings.triggerbot_y_range,
                        self.settings.triggerbot_x_range * 2,
                        self.settings.triggerbot_y_range * 2
                    ]
                    
                    frame = self.capture.get_screenshot(small_region)
                    targets = self.detect_color(frame)
                    
                    if targets:
                        # Delay aleatorio
                        delay = random.randint(self.settings.triggerbot_min_delay, self.settings.triggerbot_max_delay)
                        time.sleep(delay / 1000.0)
                        
                        # Disparar
                        self.mouse.click()
                        time.sleep(0.1)  # Evitar spam de clics
                        
                except Exception as e:
                    pass
                    
            time.sleep(0.01)
    
    def check_keys(self):
        """Verifica el estado de las teclas"""
        while self.running:
            try:
                # Verificar aimbot toggle
                if self.settings.aimbot_enabled:
                    aimbot_state = win32api.GetAsyncKeyState(self.settings.aimbot_toggle_key) & 0x8000
                    self.aimbot_enabled = bool(aimbot_state)
                
                # Verificar triggerbot toggle
                if self.settings.triggerbot_enabled:
                    triggerbot_state = win32api.GetAsyncKeyState(self.settings.triggerbot_toggle_key) & 0x8000
                    self.triggerbot_enabled = bool(triggerbot_state)
                    
            except Exception as e:
                pass
                
            time.sleep(0.01)
    
    def listen(self):
        """Inicia todos los hilos"""
        print("Colorbot iniciado sin Arduino!")
        print(f"Aimbot: {'Habilitado' if self.settings.aimbot_enabled else 'Deshabilitado'}")
        print(f"Triggerbot: {'Habilitado' if self.settings.triggerbot_enabled else 'Deshabilitado'}")
        
        # Iniciar hilos
        threading.Thread(target=self.aimbot_thread, daemon=True).start()
        threading.Thread(target=self.triggerbot_thread, daemon=True).start()
        threading.Thread(target=self.check_keys, daemon=True).start()
        
        try:
            while self.running:
                time.sleep(1)
        except KeyboardInterrupt:
            print("\nDeteniendo colorbot...")
            self.running = False