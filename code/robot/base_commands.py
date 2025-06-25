from ..config.settings_controls import RobotDogSettings

class BaseCommands:
    def __init__(self, settings: RobotDogSettings):
        self.settings = settings
        self._is_initialized = False

    def initialize(self):
        """Initialize the robot dog system."""
        self.settings.set_setting('power', True)
        self._is_initialized = True
        print("Robot dog initialized")

    def shutdown(self):
        """Shutdown the robot dog system."""
        self.settings.set_setting('power', False)
        self._is_initialized = False
        print("Robot dog shutdown")

    def reset(self):
        """Reset the robot dog to default position."""
        if not self._is_initialized:
            raise RuntimeError("Robot dog not initialized")
            
        # Reset leg positions
        default_position = {'x': 0, 'y': 0, 'z': 0}
        for leg in ['front_left', 'front_right', 'rear_left', 'rear_right']:
            self.settings.set_setting(f'legs.{leg}', default_position)
            
        # Reset head position
        self.settings.set_setting('head.position', default_position)
        
        print("Robot dog reset to default position")

    def is_initialized(self):
        """Check if robot dog is initialized."""
        return self._is_initialized