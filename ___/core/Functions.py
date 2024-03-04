import random
import datetime


def str_to_time(time):
    hours = int(time)
    minutes = (time * 60) % 60
    seconds = (time * 3600) % 60
    if seconds > 40:
        minutes += 1
    return "%d:%02d" % (hours, minutes)


def find_path(source, destination, path):
    path_dict = {}
    current_stop = destination

    while current_stop != source:
        print("current_stop", current_stop)
        next_stop = path[current_stop]['from']
        route_id = path[current_stop]['by']
        fare = path[current_stop]['fare']
        time = path[current_stop]['time']
        path_dict[current_stop] = {
            "next_stop": next_stop,
            "route_id": route_id,
            "fare": fare,
            "time": time
        }

        current_stop = next_stop

    # Add the source to the path dictionary with a route ID of None
    path_dict[source] = {
        "next_stop": None,
        "route_id": None,
        "fare": 0,
        "time": 0
    }

    return path_dict


def go_from_source_to_destination(source, destination, path):
    current_stop = source
    route = []

    while current_stop is not None:
        # print("CURR", current_stop)
        route.append(
            [
                path[current_stop]['next_stop'],
                current_stop,
                path[current_stop]['route_id'],
                path[current_stop]['fare'],
                path[current_stop]['time']
            ]
        )
        if current_stop == destination:
            break
        # print("HELLO", route, path[current_stop]['next_stop'], destination)
        next_stop = path[current_stop]['next_stop']
        current_stop = next_stop
    route.pop()
    route.reverse()
    return route


def generate_traffic(current_time=None):

    if current_time is None:
        current_time = datetime.datetime.now()

    # Define base probabilities for each traffic level
    base_traffic_probabilities = {
        "low": 0.1,
        "medium": 0.3,
        "high": 0.6
    }

    # Adjust probabilities based on time of day
    random_number = random.random()
    if 15 <= current_time.hour < 19:  # Rush hours in the evening
        if random_number < 0.35:
            base_traffic_probabilities["low"] /= 0.8
        elif random_number < 0.75:
            base_traffic_probabilities["medium"] /= 1.2
        else:
            base_traffic_probabilities["high"] /= 2.0
    elif 7 <= current_time.hour < 10:  # Morning rush hours
        if random_number < 0.35:
            base_traffic_probabilities["low"] /= 0.8
        elif random_number < 0.75:
            base_traffic_probabilities["medium"] /= 1.5
        else:
            base_traffic_probabilities["high"] /= 1.8

    # Adjust probabilities based on the day of the week
    weekday = current_time.weekday()  # Monday is 0, Sunday is 6
    random_number = random.random()
    if weekday < 5:  # Weekdays
        if random_number < 0.35:
            base_traffic_probabilities["low"] /= 1.2
        elif random_number < 0.75:
            base_traffic_probabilities["medium"] /= 1.4
        else:
            base_traffic_probabilities["high"] /= 1.6
    else:  # Weekends
        if random_number < 0.35:
            base_traffic_probabilities["low"] /= 0.8
        elif random_number < 0.75:
            base_traffic_probabilities["medium"] /= 0.8
        else:
            base_traffic_probabilities["high"] /= 0.8

    # Introduce random event probability
    random_event_probability = random.uniform(0.01, 0.1)  # 5% chance of a random event affecting traffic
    if random.random() < random_event_probability:
        # Adjust probabilities for random event
        random_event_type = random.choice(["protest", "accident", "road_closure"])
        if random_event_type == "protest":
            base_traffic_probabilities["high"] /= 2.1
            base_traffic_probabilities["medium"] *= 1.2
            base_traffic_probabilities["low"] *= 0.8
        elif random_event_type == "accident":
            base_traffic_probabilities["high"] /= 1.5
            base_traffic_probabilities["medium"] /= 1.2
            base_traffic_probabilities["low"] *= 0.8
        elif random_event_type == "road_closure":
            base_traffic_probabilities["high"] /= 2
            base_traffic_probabilities["medium"] /= 1.5
            base_traffic_probabilities["low"] /= 1.2

    # Generate a random number between 0 and 1
    random_number = random.random()

    # Determine traffic level based on adjusted probabilities
    cumulative_probability = 0
    # print("______________PROBS_____________________")
    # print(base_traffic_probabilities)
    for level, probability in base_traffic_probabilities.items():
        cumulative_probability += probability
        if random_number <= cumulative_probability:
            return base_traffic_probabilities[level]

    # Default to low traffic if no match found
    return base_traffic_probabilities['high']
