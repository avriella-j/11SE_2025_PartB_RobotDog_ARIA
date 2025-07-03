import sys
import os
# Add the project root to Python path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from robot.base_commands import BaseCommands
from robot.camera_feature import CameraFeature
from robot.head_controls import HeadControls
from robot.movement_controls import MovementControls
from robot.sensor_controls import SensorControls
from robot.stability_controls import StabilityControls
from config.settings_controls import RobotDogSettings
from utils.keyboard_controller import KeyboardController
import time

class RobotDogController:
    def __init__(self):
        self.keyboard = KeyboardController()
        
    def run(self):
        """Run the controller."""
        self.keyboard.run()

if __name__ == "__main__":
    controller = RobotDogController()
    controller.run()
