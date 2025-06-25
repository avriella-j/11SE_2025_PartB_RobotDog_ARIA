from ..config.settings_controls import RobotDogSettings
import time

class MovementControls:
    def __init__(self, settings: RobotDogSettings):
        self.settings = settings
        self._is_moving = False
        self._current_gait = 'walk'
        
    def walk_forward(self, distance: float, speed: float = None):
        """
        Walk forward a specified distance.
        Args:
            distance: Distance to walk in mm
            speed: Optional walking speed
        """
        if not self.settings.get_setting('power'):
            raise RuntimeError("Robot dog is not powered")
            
        if speed is not None:
            self.settings.set_setting('head.speed', speed)
            
        self._is_moving = True
        print(f"Walking forward {distance} mm")
        
        # Move legs in sequence for walking
        for leg in ['front_left', 'front_right', 'rear_left', 'rear_right']:
            current = self.settings.get_setting(f'legs.{leg}')
            target = {
                'x': current['x'] + distance,
                'y': current['y'],
                'z': current['z']
            }
            self.settings.set_setting(f'legs.{leg}', target)
            time.sleep(0.1)  # Small delay for smooth movement
        
        self._is_moving = False

    def turn(self, angle: float):
        """
        Turn the robot dog.
        Args:
            angle: Angle to turn in degrees (positive = clockwise, negative = counterclockwise)
        """
        if not self.settings.get_setting('power'):
            raise RuntimeError("Robot dog is not powered")
            
        self._is_moving = True
        print(f"Turning {angle} degrees")
        
        # Adjust leg positions for turning
        for leg in ['front_left', 'front_right', 'rear_left', 'rear_right']:
            current = self.settings.get_setting(f'legs.{leg}')
            # Simple rotation around Z axis
            rad = angle * (3.14159 / 180)
            new_x = current['x'] * np.cos(rad) - current['y'] * np.sin(rad)
            new_y = current['x'] * np.sin(rad) + current['y'] * np.cos(rad)
            
            target = {
                'x': new_x,
                'y': new_y,
                'z': current['z']
            }
            self.settings.set_setting(f'legs.{leg}', target)
            time.sleep(0.1)  # Small delay for smooth movement
        
        self._is_moving = False

    def stop(self):
        """Stop all movement."""
        self._is_moving = False
        print("Movement stopped")

    def set_gait(self, gait: str):
        """
        Set the walking gait.
        Args:
            gait: One of 'walk', 'trot', 'gallop'
        """
        if gait not in ['walk', 'trot', 'gallop']:
            raise ValueError(f"Invalid gait: {gait}")
            
        self._current_gait = gait
        print(f"Gait set to {gait}")