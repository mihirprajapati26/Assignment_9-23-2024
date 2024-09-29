# Define the Car class
class Car:
    def __init__(self, registration_number, max_speed):
        self.registration_number = registration_number
        self.max_speed = max_speed
        self.current_speed = 0  # Automatically set to 0
        self.travelled_distance = 0  # Automatically set to 0

    # Method to accelerate or decelerate the car
    def accelerate(self, speed_change):
        self.current_speed += speed_change
        # Ensure the speed stays within the allowed limits
        if self.current_speed > self.max_speed:
            self.current_speed = self.max_speed
        elif self.current_speed < 0:
            self.current_speed = 0

# Main program
def main():
    # Create a new car object
    my_car = Car("ABC-123", 142)

    # Speed changes
    print("Accelerating...")
    my_car.accelerate(30)  # Increase by 30 km/h
    print(f"Current Speed: {my_car.current_speed} km/h")

    my_car.accelerate(70)  # Increase by 70 km/h
    print(f"Current Speed: {my_car.current_speed} km/h")

    my_car.accelerate(50)  # Increase by 50 km/h
    print(f"Current Speed: {my_car.current_speed} km/h")

    # Emergency brake (decrease by -200 km/h)
    print("Emergency brake!")
    my_car.accelerate(-200)
    print(f"Final Speed: {my_car.current_speed} km/h")

# Run the main program
main()