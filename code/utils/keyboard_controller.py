import keyboard
from robot.base_commands import BaseCommands
from robot.camera_feature import CameraFeature
from robot.head_controls import HeadControls
from robot.movement_controls import MovementControls
from robot.sensor_controls import SensorControls
from robot.stability_controls import StabilityControls
from config.settings_controls import RobotDogSettings

class KeyboardController:
    def __init__(self):
        # Initialize settings first
        self.settings = RobotDogSettings()
        
        # Enable accelerometer by default
        self.settings.set_setting('accelerometer.enabled', True)
        
        # Initialize all components in proper order
        self.sensors = SensorControls(self.settings)
        self.stability = StabilityControls(self.settings)
        self.movement = MovementControls(self.settings)
        self.head = HeadControls(self.settings)
        self.camera = CameraFeature(self.settings)
        self.base = BaseCommands(self.settings)
        
        # Start accelerometer monitoring after stability controls are initialized
        try:
            self.stability.start_stability_monitor()
        except RuntimeError as e:
            print(f"Warning: {e}")
            print("Stability monitoring will be disabled.")
            self.settings.set_setting('accelerometer.enabled', False)
        
        self.movement_speed = 100  # Default movement speed in mm
        self.turn_speed = 15  # Default turn speed in degrees
        self.menu_active = False
        self.is_initialized = True
        
        # Register keyboard hooks
        keyboard.on_press_key('up', self._on_up_arrow)
        keyboard.on_press_key('down', self._on_down_arrow)
        keyboard.on_press_key('left', self._on_left_arrow)
        keyboard.on_press_key('right', self._on_right_arrow)
        keyboard.on_press_key('p', self._show_settings)
        keyboard.on_press_key('m', self._show_menu)
        keyboard.on_press_key('esc', self._exit)
        
        # Menu options
        self.menu_options = {
            '1': self._sensor_settings,
            '2': self._camera_settings,
            '3': self._movement_settings
        }
    
    def _on_up_arrow(self, e):
        """Handle up arrow key press."""
        if not self.is_initialized:
            print("Robot not initialized. Press P to show settings.")
            return
            
        self.movement.walk_forward(self.movement_speed)
        print(f"Walking forward {self.movement_speed} mm")

    def _on_down_arrow(self, e):
        """Handle down arrow key press."""
        if not self.is_initialized:
            print("Robot not initialized. Press P to show settings.")
            return
            
        self.movement.walk_forward(-self.movement_speed)
        print(f"Walking backward {self.movement_speed} mm")

    def _on_left_arrow(self, e):
        """Handle left arrow key press."""
        if not self.is_initialized:
            print("Robot not initialized. Press P to show settings.")
            return
            
        self.movement.turn(self.turn_speed)
        print(f"Turning left {self.turn_speed} degrees")

    def _on_right_arrow(self, e):
        """Handle right arrow key press."""
        if not self.is_initialized:
            print("Robot not initialized. Press P to show settings.")
            return
            
        self.movement.turn(-self.turn_speed)
        print(f"Turning right {self.turn_speed} degrees")

    def _show_settings(self, e):
        """Show settings menu."""
        if not self.menu_active:
            print("\nRobot Settings:")
            print("P - Show settings")
            print("M - Main menu")
            print("ESC - Exit")
            print("\nCurrent Settings:")
            print(f"Movement speed: {self.movement_speed} mm")
            print(f"Turn speed: {self.turn_speed} degrees")
            print(f"Power: {self.settings.get_setting('power')}")
            print(f"Stability: {'Stable' if self.stability.check_stability() else 'Unstable'}")

    def _show_menu(self, e):
        """Show main menu."""
        if not self.menu_active:
            print("\nMain Menu:")
            print("1 - Sensor Settings")
            print("2 - Camera Settings")
            print("3 - Movement Settings")
            print("ESC - Exit")
            self.menu_active = True
            
            while self.menu_active:
                try:
                    choice = keyboard.read_event(suppress=True)
                    if choice.event_type == keyboard.KEY_DOWN:
                        if choice.name == 'esc':
                            self.menu_active = False
                            break
                        elif choice.name in self.menu_options:
                            self.menu_options[choice.name]()
                except KeyboardInterrupt:
                    break

    def _sensor_settings(self):
        """Show sensor settings menu."""
        print("\nSensor Settings:")
        print(f"Accelerometer enabled: {self.settings.get_setting('accelerometer.enabled')}")
        print(f"Accelerometer sensitivity: {self.settings.get_setting('accelerometer.sensitivity')}")
        print(f"Accelerometer threshold: {self.settings.get_setting('accelerometer.threshold')}")
        print("\nPress ESC to return")
        
        while True:
            if keyboard.is_pressed('esc'):
                break

    def _camera_settings(self):
        """Show camera settings menu."""
        print("\nCamera Settings:")
        print(f"Camera enabled: {self.settings.get_setting('camera.enabled')}")
        print(f"Resolution: {self.settings.get_setting('camera.resolution')}")
        print(f"Framerate: {self.settings.get_setting('camera.framerate')} FPS")
        print(f"Zoom: {self.settings.get_setting('camera.zoom')}")
        print("\nPress ESC to return")
        
        while True:
            if keyboard.is_pressed('esc'):
                break

    def _movement_settings(self):
        """Show movement settings menu."""
        print("\nMovement Settings:")
        print(f"Movement speed: {self.movement_speed} mm")
        print(f"Turn speed: {self.turn_speed} degrees")
        print("\nPress ESC to return")
        
        while True:
            if keyboard.is_pressed('esc'):
                break

    def _exit(self, e):
        """Handle program exit."""
        if self.is_initialized:
            self.stability.stop_stability_monitor()
            self.base.shutdown()
        print("\nExiting program...")
        keyboard.unhook_all()
        exit(0)

    def initialize(self, settings):
        """Initialize the controller with settings."""
        self.settings = settings
        self.base = BaseCommands(self.settings)
        self.camera = CameraFeature(self.settings)
        self.head = HeadControls(self.settings)
        self.movement = MovementControls(self.settings)
        self.sensors = SensorControls(self.settings)
        self.stability = StabilityControls(self.settings)
        self.is_initialized = True

    def run(self):
        """Run the controller."""
        try:
            # Initialize settings
            self.settings = RobotDogSettings()
            
            # Configure settings
            self.settings.set_setting('accelerometer.enabled', True)
            self.settings.set_setting('accelerometer.sensitivity', 0.8)
            self.settings.set_setting('accelerometer.threshold', 0.3)
            self.settings.set_setting('camera.enabled', True)
            self.settings.set_setting('camera.resolution', (1280, 720))
            self.settings.set_setting('camera.framerate', 30)
            self.settings.set_setting('camera.zoom', 1.0)
            
            # Initialize all components
            self.base = BaseCommands(self.settings)
            self.camera = CameraFeature(self.settings)
            self.head = HeadControls(self.settings)
            self.movement = MovementControls(self.settings)
            self.sensors = SensorControls(self.settings)
            self.stability = StabilityControls(self.settings)
            
            print("Welcome to Robot Dog Controller!")
            print("Use arrow keys to control movement:")
            print("- Up arrow: Move forward")
            print("- Down arrow: Move backward")
            print("- Left arrow: Turn left")
            print("- Right arrow: Turn right")
            print("\nP - Show settings")
            print("M - Main menu")
            print("ESC - Exit")
            
            # Initialize robot
            self.base.initialize()
            self.stability.start_stability_monitor()
            self.is_initialized = True
            
            # Keep program running
            keyboard.wait('esc')
            
        except Exception as e:
            print(f"Error: {str(e)}")
            self._exit(None)
