# Define the Car class
class Car:
    def __init__(self, registration_number, max_speed):
        self.registration_number = registration_number
        self.max_speed = max_speed
        self.current_speed = 0  # Automatically set to 0
        self.travelled_distance = 0  # Automatically set to 0

# Main program
def main():
    # Create a new car object
    my_car = Car("ABC-123", 142)

    # Print out the properties of the car
    print(f"Car details:")
    print(f"Registration Number: {my_car.registration_number}")
    print(f"Maximum Speed: {my_car.max_speed} km/h")
    print(f"Current Speed: {my_car.current_speed} km/h")
    print(f"Travelled Distance: {my_car.travelled_distance} km")

# Run the main program
main()