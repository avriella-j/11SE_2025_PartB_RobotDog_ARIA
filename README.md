# Robot Dog ARIA

An advanced quadruped robot dog with multiple control systems and sensors.

## Features

- Four-legged walking and movement system
- Head movement and tracking capabilities
- Camera system with zoom and face detection
- Accelerometer-based stability monitoring
- Power management system
- Configurable settings interface

## Project Structure

```
robot/                # Main robot control components
├── base_commands.py  # Power and initialization
├── camera_feature.py # Camera control and streaming
├── head_controls.py  # Head movement and tracking
├── movement_controls.py # Walking and turning
├── sensor_controls.py # Accelerometer and sensors
└── stability_controls.py # Stability monitoring

config/              # Configuration and settings
└── settings_controls.py # Central settings management

main_code.py         # Main application entry point
requirements.txt      # Project dependencies
```

## Installation

1. Install the required dependencies:
```bash
pip install -r requirements.txt
```

2. Ensure you have a compatible camera connected to your system for the camera features to work.

## Usage

Run the main application:
```bash
python main_code.py
```

### Keyboard Controls

#### Movement Controls
- Up Arrow: Move forward
- Down Arrow: Move backward
- Left Arrow: Turn left
- Right Arrow: Turn right

#### Menu Controls
- P: Show settings
- M: Show main menu
- ESC: Exit program

#### Main Menu (press M)
- 1: Sensor Settings
- 2: Camera Settings
- 3: Movement Settings
- ESC: Return to main screen

#### Settings Menu (press P)
- Shows current settings
- Movement speed
- Turn speed
- Power status
- Stability status

### Default Settings
- Movement speed: 100 mm
- Turn speed: 15 degrees
- Accelerometer:
  - Enabled: True
  - Sensitivity: 0.8
  - Threshold: 0.3
- Camera:
  - Resolution: 1280x720
  - Framerate: 30 FPS
  - Zoom: 1.0

## Components

### Base Commands
- Power management
- Initialization and shutdown
- Reset functionality

### Camera Feature
- High-resolution video streaming
- Configurable resolution and framerate
- Zoom functionality
- Face detection (optional)

### Head Controls
- 3D head movement
- Target tracking
- Smooth movement control

### Movement Controls
- Walking patterns
- Turning capabilities
- Gait configuration
- Leg position control

### Sensor Controls
- Accelerometer monitoring
- Movement detection
- Stability checking

### Stability Controls
- Stability monitoring
- Automatic position adjustment
- Threshold-based stability checking

## Settings

All settings are managed through the central `RobotDogSettings` class, allowing for:
- Power control
- Camera configuration
- Head movement settings
- Accelerometer settings
- Stability thresholds

## Error Handling

The system includes comprehensive error handling for:
- Power state management
- Camera initialization
- Stability monitoring
- Movement control
- Sensor readings

## Contributing

Please create an issue or submit a pull request for any improvements or bug fixes.

## License

Copyright © 2025. All rights reserved.
