from ..config.settings_controls import RobotDogSettings
import numpy as np

class SensorControls:
    def __init__(self, settings: RobotDogSettings):
        self.settings = settings
        self._accel_data = None
        self._is_monitoring = False

    def start_accelerometer(self):
        """Start accelerometer monitoring."""
        if self.settings.get_setting('accelerometer.enabled'):
            self._is_monitoring = True
            print("Accelerometer monitoring started")
        else:
            raise RuntimeError("Accelerometer is not enabled in settings")

    def stop_accelerometer(self):
        """Stop accelerometer monitoring."""
        self._is_monitoring = False
        print("Accelerometer monitoring stopped")

    def read_accelerometer(self):
        """Read accelerometer data."""
        if not self._is_monitoring:
            raise RuntimeError("Accelerometer is not monitoring")
            
        # Simulated accelerometer data (in real implementation, this would read from hardware)
        self._accel_data = {
            'x': np.random.normal(0, 0.1),
            'y': np.random.normal(0, 0.1),
            'z': np.random.normal(1, 0.1)
        }
        
        # Check if movement exceeds threshold
        magnitude = (self._accel_data['x']**2 + 
                    self._accel_data['y']**2 + 
                    self._accel_data['z']**2)**0.5
        
        if magnitude > self.settings.get_setting('accelerometer.threshold'):
            print(f"Movement detected: {magnitude}")
            return True
        
        return False

    def get_accelerometer_data(self):
        """Get the last accelerometer reading."""
        return self._accel_data

    def check_stability(self):
        """Check if robot is stable based on accelerometer data."""
        if not self._is_monitoring:
            raise RuntimeError("Accelerometer is not monitoring")
            
        # Calculate stability based on accelerometer readings
        stability_score = 1.0 - abs(self._accel_data['x']) - abs(self._accel_data['y'])
        stability_score = max(0.0, min(1.0, stability_score))
        
        return stability_score