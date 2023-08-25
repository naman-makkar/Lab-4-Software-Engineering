from tabulate import tabulate

class Flight:
    def __init__(self, p_id, process, start_time, priority):
        self.p_id = p_id
        self.process = process
        self.start_time = start_time
        self.priority = priority

    def __repr__(self):
        return f"Flight(p_id={self.p_id}, process={self.process}, start_time={self.start_time}, priority={self.priority})"

def sort_flights(flights, key):
    return sorted(flights, key=key)

def main():
    flights = [
        Flight("P1", "VSCode", 100, "MID"),
        Flight("P23", "Eclipse", 234, "MID"),
        Flight("P93", "Chrome", 189, "High"),
        Flight("P42", "JDK", 9, "High"),
        Flight("P9", "CMD", 7, "High"),
        Flight("P87", "NotePad", 23, "Low"),
    ]

    print("Select the sorting parameter:")
    print("1. Sort by P_ID")
    print("2. Sort by Start Time")
    print("3. Sort by Priority")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        sorted_flights = sort_flights(flights, key=lambda flight: flight.p_id)
    elif choice == 2:
        sorted_flights = sort_flights(flights, key=lambda flight: flight.start_time)
    elif choice == 3:
        sorted_flights = sort_flights(flights, key=lambda flight: flight.priority)
    else:
        print("Invalid choice!")
        return

    sorted_flight_data = [
        [flight.p_id, flight.process, flight.start_time, flight.priority]
        for flight in sorted_flights
    ]

    headers = ["P_ID", "Process", "Start Time", "Priority"]
    print("The flights after sorting are:")
    print(tabulate(sorted_flight_data, headers=headers, tablefmt="grid"))

if __name__ == "__main__":
    main()


