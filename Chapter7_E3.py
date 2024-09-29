def add_airport(airports):
    icao_code = input("Enter the ICAO code of the airport: ").upper()
    airport_name = input("Enter the name of the airport: ")
    airports[icao_code] = airport_name
    print(f"Airport '{airport_name}' with ICAO code '{icao_code}' added successfully.\n")


def fetch_airport(airports):
    icao_code = input("Enter the ICAO code of the airport: ").upper()
    if icao_code in airports:
        print(f"The airport with ICAO code '{icao_code}' is '{airports[icao_code]}'.\n")
    else:
        print(f"No airport found with ICAO code '{icao_code}'.\n")


def main():
    airports = {}
    while True:
        print("Choose an option:")
        print("1. Enter a new airport")
        print("2. Fetch airport information")
        print("3. Quit")

        choice = input("Enter your choice (1/2/3): ")

        if choice == "1":
            add_airport(airports)
        elif choice == "2":
            fetch_airport(airports)
        elif choice == "3":
            print("Exiting program. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.\n")


# Run the main program
main()