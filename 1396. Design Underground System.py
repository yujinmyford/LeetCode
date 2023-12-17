# Dictionary
# Runtime: O(1)
# Space: O(n)

class UndergroundSystem
    def __init__(self):
        # Hashmap to keep track of when customers check in
        self.checked_in = {}
        # Hashmap to keep track of when customers check out
        self.route_stats = {}

    # Adds the checked in station name and time to checked_in
    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.checked_in[id] = (stationName, t)

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        # Gets the start station and time
        start_station, check_in_time = self.checked_in.pop(id)
        # Get the route and the time it took for the route
        route = (start_station, stationName)
        route_time = t - check_in_time

        # If route is already in checked_out, add the route time to the existing entry, and update the count
        if route in self.route_stats:
            total_time, count = self.route_stats[route]
            self.route_stats[route] = (total_time + route_time, count + 1)
        # If route isn't in checked_out, create the entry in checked_out
        else: 
            self.route_stats[route] = (route_time, 1)

    # Gets the average time by using checked_out, calculating the total route times divided by number of route entries
    def getAverageTime(self, startStation: str, endStation: str) -> float:
        route = (startStation, endStation)
        total_time, count = self.route_stats[route]
        return total_time / count
