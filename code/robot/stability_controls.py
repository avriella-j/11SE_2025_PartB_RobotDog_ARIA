from config.settings_controls import RobotDogSettings
from robot.sensor_controls import SensorControls

class StabilityControls:
    def __init__(self, settings: RobotDogSettings):
        self.settings = settings
        self.sensor_controls = SensorControls(settings)
        self._is_stabilizing = False
        self._stability_threshold = 0.7  # Default stability threshold
        self._last_stability_score = 1.0  # Default stable state
        
    def start_stability_monitor(self):
        """Start monitoring stability."""
        if not self.settings.get_setting('accelerometer.enabled'):
            raise RuntimeError("Accelerometer is not enabled in settings")
            
        try:
            self.sensor_controls.start_accelerometer()
            self._is_stabilizing = True
            print("Stability monitoring started")
            # Read initial data to ensure we have a value
            self.sensor_controls.read_accelerometer()
        except RuntimeError as e:
            print(f"Warning: {e}")
            print("Stability monitoring failed to start")
            self._is_stabilizing = False
            raise

    def start_stability_monitor(self):
        """Start monitoring stability."""
        self.sensor_controls.start_accelerometer()
        self._is_stabilizing = True
        print("Stability monitoring started")

    def stop_stability_monitor(self):
        """Stop monitoring stability."""
        self.sensor_controls.stop_accelerometer()
        self._is_stabilizing = False
        print("Stability monitoring stopped")

    def check_stability(self):
        """Check if robot is stable."""
        if not self._is_stabilizing:
            return self._last_stability_score >= self._stability_threshold
            
        try:
            stability_score = self.sensor_controls.check_stability()
            if stability_score is not None:
                self._last_stability_score = stability_score
                print(f"Current stability score: {stability_score:.2f}")
            return stability_score >= self._stability_threshold
        except Exception as e:
            print(f"Error checking stability: {e}")
            return self._last_stability_score >= self._stability_threshold

    def adjust_position(self):
        """Adjust position to improve stability."""
        if not self._is_stabilizing:
            raise RuntimeError("Stability monitoring is not active")
            
        # Get current leg positions
        leg_positions = {}
        for leg in ['front_left', 'front_right', 'rear_left', 'rear_right']:
            leg_positions[leg] = self.settings.get_setting(f'legs.{leg}')
            
        # Adjust positions based on stability score
        stability_score = self.sensor_controls.check_stability()
        if stability_score < self._stability_threshold:
            print("Adjusting position to improve stability")
            
            # Example adjustment: lower the body slightly
            for leg in leg_positions:
                leg_positions[leg]['z'] -= 5  # Lower each leg by 5mm
                self.settings.set_setting(f'legs.{leg}', leg_positions[leg])
            
            # Adjust head position slightly
            current_head = self.settings.get_setting('head.position')
            self.settings.set_setting('head.position', {
                'x': current_head['x'],
                'y': current_head['y'],
                'z': current_head['z'] - 3  # Lower head by 3mm
            })
            
            print("Position adjusted for better stability")
