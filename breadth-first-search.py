from collections import deque


# The Subway Map Graph
subway_map = {
    "Central Station": ["Museum", "Downtown"],
    "Museum": ["Central Station", "Zoo"],
    "Downtown": ["Central Station", "Tech Hub", "Airport"],
    "Zoo": ["Museum", "Airport"],
    "Tech Hub": ["Downtown"],
    "Airport": ["Downtown", "Zoo"]
}



def route_prediction(start_station, target_station):
    station_queue = deque()
    station_queue += subway_map[start_station]
    searched_station = []
    iteration = 0

    while station_queue:
        iteration += 1
        station = station_queue.popleft()

        if station not in searched_station:
            if station == target_station:
                print (f"You have arrived at your destination || iteration: {iteration}")
                return
            else:
                station_queue += subway_map[station]
                searched_station.append(station)

    return False


route_prediction("Central Station", "Airport")


