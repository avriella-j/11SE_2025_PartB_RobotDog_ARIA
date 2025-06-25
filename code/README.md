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

The robot will:
1. Initialize and power on
2. Set up camera and stability monitoring
3. Perform a movement sequence
4. Check and adjust stability
5. Track a target
6. Clean up and shut down

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
