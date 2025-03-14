# 2nd Code: Robot Stands and Spins 5 Times in Place
class Robot:
    def spin(self, rounds):
        # Simulate robot spinning in place
        for round in range(rounds):
            print(f"Robot is spinning round {round + 1}.")

# Create robot object
robot = Robot()

# Robot spins 5 times
robot.spin(5)
