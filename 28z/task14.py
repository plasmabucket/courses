def Unmanned(length: int, sl_count: int, track: list[list[int]]) -> int:
    # Create a dictionary for easy red and green time retrieval
    streetlights: dict[int, list[int]] = {}
    for light in track:
        streetlights[light[0]] = [light[1], light[2]]
    # Go through each coordinate and if a streetlight is encountered
    # add required waiting time
    time: int = 0
    for coord in range(length):
        if coord in streetlights:
            red_time: int = streetlights[coord][0]
            green_time: int = streetlights[coord][1]
            time += max(0, red_time - time % (red_time + green_time))
        time += 1  # Time of traveling
    return time



