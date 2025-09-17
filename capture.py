import mss
import numpy as np

class Capture:
    """
    The Capture class is responsible for capturing a specified region of the screen.
    """

    def __init__(self):
        """
        Initializes the Capture class with screen capture parameters.
        """
        self.sct = mss.mss()
    
    def get_screenshot(self, region):
        """
        Captures the screen based on the specified region and returns it as a numpy array.

        Args:
            region (tuple): A tuple containing the region coordinates (x, y, width, height).

        Returns:
            np.ndarray: The captured screen region as a numpy array.
        """
        monitor = {
            "top": region[1],
            "left": region[0], 
            "width": region[2],
            "height": region[3]
        }
        
        screenshot = self.sct.grab(monitor)
        img = np.array(screenshot)
        return img[:, :, :3]  # Remover canal alpha