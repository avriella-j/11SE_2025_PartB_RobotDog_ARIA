# Changelog

## 2025-07-03 11:13:28 

### Fixed
- Added missing NumPy import in `movement_controls.py` to resolve `NameError: name 'np' is not defined` when turning the robot
- Fixed stability monitoring initialization in `keyboard_controller.py`:
  - Added proper initialization order for components
  - Enabled accelerometer by default in settings
  - Added error handling for accelerometer initialization
- Fixed `StabilityControls` initialization in `keyboard_controller.py`:
  - Removed extra `self.sensors` parameter from constructor
  - Updated to use `start_stability_monitor()` instead of direct accelerometer control
- Enhanced stability monitoring in `stability_controls.py`:
  - Added `_last_stability_score` to maintain last known stability value
  - Improved error handling in `start_stability_monitor`
  - Added graceful fallbacks for None values and errors in `check_stability`
  - Added better error logging and user feedback
- Fixed component initialization order in `keyboard_controller.py` to ensure proper dependencies

### Changed
- Modified stability monitoring to use a default stable state (1.0) when no data is available
- Updated error messages to be more specific about stability monitoring status
- Improved error handling throughout the stability monitoring system

### Added
- Added proper initialization of all robot components in `KeyboardController`
- Added accelerometer initialization with error handling
- Added stability score caching to prevent crashes during sensor failures
- Keyboard-controlled interface with arrow keys for movement
- Main menu system accessible via 'M' key
- Settings menu accessible via 'P' key
- Default settings configuration for accelerometer and camera

## [2025-06-25]

### Added
- Added keyboard controller module for movement and menu handling
- Implemented keyboard-controlled interface with arrow keys for movement
- Added main menu system accessible via 'M' key
- Added settings menu accessible via 'P' key
- Default settings configuration for accelerometer and camera
- Added error handling for component initialization
- Added stability monitoring configuration

### Changed
- Moved keyboard control logic to separate `keyboard_controller.py` module
- Updated README with keyboard control documentation
- Improved error handling and initialization sequence
- Reorganized project structure for better maintainability

### Fixed
- Fixed accelerometer initialization error
- Fixed NoneType initialization errors
- Added proper settings configuration before component initialization
- Resolved keyboard event handling issues

## [2025-06-24]

### Added
- Added proper initialization of all robot components in `KeyboardController`
- Added accelerometer initialization with error handling
- Added stability score caching to prevent crashes during sensor failures

## [2025-06-23]

### Added
- Initial implementation of robot dog control system
- Base commands for initialization and shutdown
- Camera feature with resolution and zoom controls
- Head controls for movement and tracking
- Movement controls for walking and turning
- Sensor controls for accelerometer monitoring
- Stability controls for position adjustment

### Changed
- Reorganized project structure with separate modules
- Added proper dependency management
- Improved error handling and logging

### Fixed
- Various initialization sequence issues
- Component dependency resolution
- Settings management integration

## [2025-06-22]

### Added
- Initial project setup
- Basic component structure
- Settings management system
- Core control functionality

### Changed
- Improved project organization
- Added basic documentation

### Fixed
- Initial setup issues
- Basic functionality bugs

## [Initial Release]
- Basic robot dog control system with keyboard input
- Movement controls (forward, backward, turn)
- Camera and sensor controls
- Settings configuration system