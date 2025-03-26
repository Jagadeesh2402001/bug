# 3rd Code: Robot Returns to Starting Point
class Robot:
    def move_forward(self, distance):
        # Simulate robot moving forward by distance
        print(f"Robot is moving forward {distance} meters.")
    
    def move_backwards(self, distance):
        # Simulate robot moving backward to return to the starting point
        print(f"Robot is moving backward {distance} meters to the starting point.")

# Create robot object
robot = Robot()

# Move robot 5 meters forward and then return
robot.move_forward(5)
robot.move_backwards(5)
