from enum import Enum
from Arguement import Arguement

class MotionType(Enum):
    LINEAR = 0
    RAPID = 1

class SimpleMotion:


    def __init__(self, command: str, *args: Arguement):
        if command == "G0" or "G00":
            self.motion_type = MotionType.LINEAR
