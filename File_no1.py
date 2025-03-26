# 1st Code: Robot Moves 5 Meters

DEBUG = False
if DEBUG:
    IMAGE_PATH = "/home/hariharan/"
    DISINFECT_NAVIGATION-LAUNCH_PATH = ["/home/hariharan/turtlebot/src/exploration/launch/turtlebot_nav.launch"]

class Robot:
    def move_forward(self, distance):
        # Simulate robot moving forward by distance
        print(f"Robot is moving forward {distance} meters.")
        

# Create robot object
robot = Robot()

# Move robot 5 meters
robot.move_forward(5)
