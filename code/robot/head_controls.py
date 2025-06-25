from ..config.settings_controls import RobotDogSettings
import time

class HeadControls:
    def __init__(self, settings: RobotDogSettings):
        self.settings = settings
        self._current_position = None
        self._target_position = None
        self._is_moving = False

    def move_to(self, x: float, y: float, z: float):
        """
        Move the head to a specific position.
        Args:
            x, y, z: Target position coordinates in mm
        """
        if not self.settings.get_setting('power'):
            raise RuntimeError("Robot dog is not powered")
            
        self._target_position = {'x': x, 'y': y, 'z': z}
        self._is_moving = True
        print(f"Moving head to position ({x}, {y}, {z})")
        
        # Update settings
        self.settings.set_setting('head.position', self._target_position)

    def stop(self):
        """Stop any head movement."""
        self._is_moving = False
        print("Head movement stopped")

    def track_target(self, target_position: dict):
        """
        Track a moving target.
        Args:
            target_position: Dictionary containing x, y, z coordinates
        """
        if not self.settings.get_setting('power'):
            raise RuntimeError("Robot dog is not powered")
            
        # Calculate movement speed based on distance
        current = self.settings.get_setting('head.position')
        distance = ((target_position['x'] - current['x']) ** 2 +
                   (target_position['y'] - current['y']) ** 2 +
                   (target_position['z'] - current['z']) ** 2) ** 0.5
        
        # Calculate movement time
        speed = self.settings.get_setting('head.speed')
        move_time = distance / speed
        
        # Move head smoothly
        self._is_moving = True
        print(f"Tracking target at position ({target_position['x']}, {target_position['y']}, {target_position['z']})")
        
        # Update settings
        self.settings.set_setting('head.position', target_position)
        
        # Wait for movement to complete
        time.sleep(move_time)
        self._is_moving = False