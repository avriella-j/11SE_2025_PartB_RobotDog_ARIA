class RobotDogSettings:
    def __init__(self):
        # Initialize default settings
        self._settings = {
            'power': False,
            'camera': {
                'enabled': False,
                'resolution': (1280, 720),
                'framerate': 30,
                'zoom': 1.0
            },
            'face_detection': {
                'enabled': False,
                'threshold': 0.8,
                'tracking': False,
                'smoothness': 0.5
            },
            'head': {
                'position': {'x': 0, 'y': 0, 'z': 0},
                'speed': 100
            },
            'legs': {
                'front_left': {'x': 0, 'y': 0, 'z': 0},
                'front_right': {'x': 0, 'y': 0, 'z': 0},
                'rear_left': {'x': 0, 'y': 0, 'z': 0},
                'rear_right': {'x': 0, 'y': 0, 'z': 0}
            },
            'accelerometer': {
                'enabled': False,
                'sensitivity': 1.0,
                'threshold': 0.5
            }
        }

    def get_settings(self):
        """Get all current settings."""
        return self._settings

    def set_setting(self, path: str, value):
        """
        Set a specific setting using dot notation.
        Args:
            path: Setting path (e.g., 'camera.enabled', 'head.position.x')
            value: New value for the setting
        """
        try:
            # Split path into components
            components = path.split('.')
            current = self._settings
            
            # Traverse to the target setting
            for component in components[:-1]:
                current = current[component]
            
            # Set the final value
            current[components[-1]] = value
            print(f"Set {path} to {value}")
            
        except KeyError:
            raise ValueError(f"Invalid setting path: {path}")

    def get_setting(self, path: str):
        """
        Get a specific setting using dot notation.
        Args:
            path: Setting path (e.g., 'camera.enabled', 'head.position.x')
        Returns:
            The value of the setting
        """
        try:
            # Split path into components
            components = path.split('.')
            current = self._settings
            
            # Traverse to the target setting
            for component in components:
                current = current[component]
            
            return current
            
        except KeyError:
            raise ValueError(f"Invalid setting path: {path}")

# Example usage
if __name__ == "__main__":
    # Create a robot dog settings instance
    robot = RobotDogSettings()
    
    # Power control
    robot.set_setting('power', True)
    print(f"Is powered: {robot.get_setting('power')}")
    
    # Camera settings
    robot.set_setting('camera.enabled', True)
    robot.set_setting('camera.resolution', (1920, 1080))
    robot.set_setting('camera.framerate', 60)
    robot.set_setting('camera.zoom', 1.5)
    print(f"Camera settings: {robot.get_setting('camera')}")
    
    # Face detection settings
    robot.set_setting('face_detection.enabled', True)
    robot.set_setting('face_detection.threshold', 0.9)
    robot.set_setting('face_detection.tracking', True)
    robot.set_setting('face_detection.smoothness', 0.7)
    print(f"Face detection settings: {robot.get_setting('face_detection')}")
    
    # Head movement
    robot.set_setting('head.position', {'x': 5, 'y': 10, 'z': 15})
    robot.set_setting('head.speed', 150)
    print(f"Head position: {robot.get_setting('head.position')}")
    
    # Leg movement
    robot.set_setting('legs.front_left', {'x': 10, 'y': 20, 'z': 30})
    print(f"Front left leg position: {robot.get_setting('legs.front_left')}")
    
    # Accelerometer settings
    robot.set_setting('accelerometer.enabled', True)
    robot.set_setting('accelerometer.sensitivity', 0.8)
    robot.set_setting('accelerometer.threshold', 0.3)
    print(f"Accelerometer settings: {robot.get_setting('accelerometer')}")
    
    # Power off
    robot.set_setting('power', False)
    # Create a robot dog settings instance
    robot = RobotDogSettings()
    
    # Power control
    robot.power_on()
    print(f"Is powered: {robot.is_powered()}")
    
    # Leg movement
    robot.set_leg_position('front_left', 10, 20, 30)
    print(f"Front left leg position: {robot.get_leg_position('front_left')}")
    
    # Head movement
    robot.set_head_position(5, 10, 15)
    print(f"Head position: {robot.get_head_position()}")
    robot.set_head_movement_speed(150)
    
    # Accelerometer settings
    robot.enable_accelerometer()
    robot.set_accelerometer_sensitivity(0.8)
    robot.set_accelerometer_threshold(0.3)
    print(f"Accelerometer settings: {robot.get_accelerometer_settings()}")
    
    # Power off
    robot.power_off()