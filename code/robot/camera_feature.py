from config.settings_controls import RobotDogSettings
import cv2
import numpy as np

class CameraFeature:
    def __init__(self, settings: RobotDogSettings):
        self.settings = settings
        self._camera = None
        self._is_streaming = False

    def start_stream(self):
        """Start the camera stream."""
        if self.settings.get_setting('camera.enabled'):
            self._camera = cv2.VideoCapture(0)
            self._camera.set(cv2.CAP_PROP_FRAME_WIDTH, self.settings.get_setting('camera.resolution')[0])
            self._camera.set(cv2.CAP_PROP_FRAME_HEIGHT, self.settings.get_setting('camera.resolution')[1])
            self._camera.set(cv2.CAP_PROP_FPS, self.settings.get_setting('camera.framerate'))
            self._is_streaming = True
            print("Camera stream started")
        else:
            raise RuntimeError("Camera is not enabled in settings")

    def stop_stream(self):
        """Stop the camera stream."""
        if self._camera:
            self._camera.release()
            self._is_streaming = False
            print("Camera stream stopped")

    def get_frame(self):
        """Get a frame from the camera."""
        if not self._is_streaming:
            raise RuntimeError("Camera stream is not active")
            
        ret, frame = self._camera.read()
        if not ret:
            raise RuntimeError("Failed to capture frame")
            
        return frame

    def apply_zoom(self, frame):
        """Apply zoom to the frame."""
        zoom = self.settings.get_setting('camera.zoom')
        if zoom != 1.0:
            height, width = frame.shape[:2]
            # Calculate new dimensions
            new_width = int(width * zoom)
            new_height = int(height * zoom)
            
            # Resize frame
            frame = cv2.resize(frame, (new_width, new_height))
            
            # Center crop to maintain original aspect ratio
            if zoom > 1.0:
                start_x = (new_width - width) // 2
                start_y = (new_height - height) // 2
                frame = frame[start_y:start_y+height, start_x:start_x+width]
            else:
                start_x = (width - new_width) // 2
                start_y = (height - new_height) // 2
                frame = np.zeros((height, width, 3), dtype=np.uint8)
                frame[start_y:start_y+new_height, start_x:start_x+new_width] = frame
        
        return frame
