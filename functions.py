import sys

def angle_between_hands(hour, minutes):  #takes time as per 24 hr clock
    # convert to 12 hr format
    hour %= 12
    # angle covered by hour hand
    hour_angle = 0.5 * (60 * hour + minutes)
    # Calculate the angle covered by minute hand
    minute_angle = 6 * minutes
    # Absolute difference between the two angles
    angle = abs(hour_angle - minute_angle)
    # Selecting the smaller angle between the angle calculated and its conjugate
    angle = min(angle, 360 - angle)
    return  angle



if __name__ == "__main__":
    # Check if enough arguments are provided
    if len(sys.argv) != 3:
        print("Usage: python functions.py hour minutes")
        print("Please provide hour and minutes as arguments.")
        sys.exit(1)

    # Get hour and minute values from command line arguments
    hour = int(sys.argv[1])
    minutes = int(sys.argv[2])

    # Calculate the angle between hands
    result = angle_between_hands(hour, minutes)

    # Print the result
    print("Angle between hands at", hour, "hours and", minutes, "minutes is:", result, "degrees")