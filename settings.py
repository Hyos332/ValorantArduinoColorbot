import configparser

class Settings:
    """
    The Settings class provides methods to read and write configuration values from a 'settings.ini' file.

    Attributes:
        config (ConfigParser): An instance of ConfigParser used to manage configuration data.
    """

    def __init__(self):
        """
        Initializes the Settings class by reading the configuration from 'settings.ini'.
        """
        self.config = configparser.ConfigParser()
        self.config.read('settings.ini')
        
    # Aimbot settings
    @property
    def aimbot_enabled(self):
        return self.config.getboolean('Aimbot', 'Enabled')
    
    @property
    def aimbot_toggle_key(self):
        return int(self.config.get('Aimbot', 'toggleKey'), 16)
    
    @property
    def aimbot_x_speed(self):
        return self.config.getfloat('Aimbot', 'xSpeed')
    
    @property
    def aimbot_y_speed(self):
        return self.config.getfloat('Aimbot', 'ySpeed')
    
    @property
    def aimbot_x_fov(self):
        return self.config.getint('Aimbot', 'xFov')
    
    @property
    def aimbot_y_fov(self):
        return self.config.getint('Aimbot', 'yFov')
    
    @property
    def aimbot_target_offset(self):
        return self.config.getfloat('Aimbot', 'targetOffset')
    
    # Triggerbot settings
    @property
    def triggerbot_enabled(self):
        return self.config.getboolean('Triggerbot', 'Enabled')
    
    @property
    def triggerbot_toggle_key(self):
        return int(self.config.get('Triggerbot', 'toggleKey'), 16)
    
    @property
    def triggerbot_min_delay(self):
        return self.config.getint('Triggerbot', 'minDelay')
    
    @property
    def triggerbot_max_delay(self):
        return self.config.getint('Triggerbot', 'maxDelay')
    
    @property
    def triggerbot_x_range(self):
        return self.config.getint('Triggerbot', 'xRange')
    
    @property
    def triggerbot_y_range(self):
        return self.config.getint('Triggerbot', 'yRange')