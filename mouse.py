import pyautogui
import threading
import time

class Mouse:
    """
    The Mouse class is responsible for managing mouse movement and clicks using pyautogui.
    """
    
    def __init__(self):
        """
        Initializes the Mouse class with pyautogui configuration.
        """
        self.lock = threading.Lock()
        # Inicializar remainder attributes que faltaban
        self.remainder_x = 0.0
        self.remainder_y = 0.0
        
        # Configurar pyautogui
        pyautogui.FAILSAFE = False  # Deshabilitar failsafe
        pyautogui.PAUSE = 0  # Sin pausa entre comandos
        
    def move(self, x, y):
        """
        Sends a mouse movement command using pyautogui, handling fractional movements.

        Args:
            x (float): The movement along the x-axis.
            y (float): The movement along the y-axis.
        """
        # Add the remainder from the previous calculation
        x += self.remainder_x
        y += self.remainder_y

        # Round x and y, and calculate the new remainder
        move_x = int(x)
        move_y = int(y)
        self.remainder_x = x - move_x
        self.remainder_y = y - move_y

        if move_x != 0 or move_y != 0:
            with self.lock:
                try:
                    pyautogui.moveRel(move_x, move_y, duration=0)
                except:
                    pass

    def click(self):
        """
        Sends a mouse click command using pyautogui.
        """
        with self.lock: 
            try:
                pyautogui.click()
            except:
                pass
    
    def is_connected(self):
        """Siempre retorna True ya que no necesitamos conexión"""
        return True