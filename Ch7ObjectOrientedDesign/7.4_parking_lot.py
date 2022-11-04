"""
Design a parking lot using OO principles
"""
from datetime import datetime

class ParkingLot:
    spots_list = []
    street_light_list = []
    def __init__(self, num_spots, num_street_lights):
        self.num_spots = num_spots
        self.spots_list = [ParkingSpot for spot in range(num_spots)]
        self.num_street_lights = num_street_lights
        self.street_light_list = [StreetLight for light in range(num_street_lights)]
        
class ParkingSpot:
    def __init__(self, occupied=False) -> None:
        self.occupied = occupied

    # Spot location is the index of the list of spots
    def occupy_spot(self, spot_location):
        spot = ParkingLot.spots_list[spot_location]
        spot.occupied = True
        return

class StreetLight:
    now = datetime.now()
    hour_military = int(now.strftime('%H'))
    if 19 < hour_military or hour_military < 7:
        time_status = 'on'
    else:
        time_status = 'off'

    def __init__(self, status=time_status) -> None:
        self.status = status
        pass

    def update_status(self):
        now = datetime.now()
        hour_military = int(now.strftime('%H'))
        if 19 < hour_military or hour_military < 7:
            time_status = 'on'
        else:
            time_status = 'off'

        for light in ParkingLot.street_light_list:
            light.time_status = time_status
        return


lot = ParkingLot(num_spots=25, num_street_lights=5)
