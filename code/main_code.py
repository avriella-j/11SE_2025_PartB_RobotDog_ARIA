from robot.base_commands import BaseCommands
from robot.camera_feature import CameraFeature
from robot.head_controls import HeadControls
from robot.movement_controls import MovementControls
from robot.sensor_controls import SensorControls
from robot.stability_controls import StabilityControls
from config.settings_controls import RobotDogSettings
import time

def main():
    # Initialize settings
    settings = RobotDogSettings()
    
    # Initialize all components with the settings
    base = BaseCommands(settings)
    camera = CameraFeature(settings)
    head = HeadControls(settings)
    movement = MovementControls(settings)
    sensors = SensorControls(settings)
    stability = StabilityControls(settings)
    
    try:
        # Initialize the robot
        base.initialize()
        
        # Configure camera
        settings.set_setting('camera.enabled', True)
        settings.set_setting('camera.resolution', (1920, 1080))
        settings.set_setting('camera.framerate', 30)
        settings.set_setting('camera.zoom', 1.5)
        
        # Start camera stream
        camera.start_stream()
        
        # Configure stability monitoring
        settings.set_setting('accelerometer.enabled', True)
        settings.set_setting('accelerometer.sensitivity', 0.8)
        settings.set_setting('accelerometer.threshold', 0.3)
        
        # Start stability monitoring
        stability.start_stability_monitor()
        
        # Example movement sequence
        print("\nStarting movement sequence...")
        
        # Walk forward
        movement.walk_forward(1000)  # 1 meter
        time.sleep(2)
        
        # Turn 90 degrees
        movement.turn(90)
        time.sleep(2)
        
        # Move head
        head.move_to(10, 10, 10)
        time.sleep(2)
        
        # Check stability
        print("\nChecking stability...")
        if stability.check_stability():
            print("Robot is stable")
        else:
            print("Robot is not stable, adjusting position...")
            stability.adjust_position()
        
        # Track a target (example position)
        print("\nTracking target...")
        head.track_target({'x': 20, 'y': 20, 'z': 20})
        time.sleep(2)
        
    except Exception as e:
        print(f"Error: {str(e)}")
        
    finally:
        # Clean up
        print("\nShutting down...")
        camera.stop_stream()
        stability.stop_stability_monitor()
        base.shutdown()

if __name__ == "__main__":
    main()
