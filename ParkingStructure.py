import Vehicle, Ticket

class ParkingStructure:
    
    def __init__(self, capacity):
        self.capacity = capacity
        # Map from ticket to vehicle, will need when removing and calculating rate
        self.ticket_to_vehicle = {}
        self.free_car_spots = []
        self.free_truck_spots = []
        self.free_motorcycle_spots = []
        # First 50% of space goes to the cars
        free_car_spots = capacity // 2
        for i in range(0, free_car_spots):
            self.free_car_spots.append(i)
        # Remaining 50% of space is divided between trucks and motorcycles
        for j in range(free_car_spots, self.capacity):
            self.free_truck_spots.append(j)
            self.free_car_spots.append(j+1)

    def park(self, vehicle):
        pass

    def vehicle_exit(self, ticket):
        pass

        

def main():
    print("Need to implement menu system to park/remove vehicles")
    return

if __name__ == '__main__':
    main()