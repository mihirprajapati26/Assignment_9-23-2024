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

    # Method to drive the car for a given number of hours
    def drive(self, hours):
        distance_travelled = self.current_speed * hours
        self.travelled_distance += distance_travelled
        print(f"Driven for {hours} hours at {self.current_speed} km/h. Distance covered: {distance_travelled:.2f} km.")
        print(f"Total travelled distance: {self.travelled_distance:.2f} km.")

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

    # Drive the car for 1.5 hours
    my_car.drive(1.5)

    # Increase speed by 50 km/h
    my_car.accelerate(50)  # Increase by 50 km/h
    print(f"Current Speed: {my_car.current_speed} km/h")

    # Drive the car for 2 hours
    my_car.drive(2)

    # Emergency brake (decrease by -200 km/h)
    print("Emergency brake!")
    my_car.accelerate(-200)
    print(f"Final Speed: {my_car.current_speed} km/h")

    # Drive for 1 hour after emergency brake
    my_car.drive(1)

# Run the main program
main()