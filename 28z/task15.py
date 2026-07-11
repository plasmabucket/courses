def TankRush(h1: int, w1: int, s1: str, h2: int, w2: int, s2: str) -> bool:
    # Normalize strings by removing spaces for ease of addressing
    s1_norm = s1.replace(" ", "")
    s2_norm = s2.replace(" ", "")
    # Get dimensions of an area from which search can be started
    h_delta: int = h1 - h2 + 1
    w_delta: int = w1 - w2 + 1
    # Iterate over every starting point in that area
    match: bool = False
    for entrypoint in range(h_delta * w_delta):
        match = True
        # Go through the submap and compare its cells to the map
        for cell in range(h2 * w2):
            sub_y: int = cell // w2
            sub_x: int = cell % w2
            map_y: int = entrypoint // w_delta + sub_y
            map_x: int = entrypoint % w_delta + sub_x
            if s1_norm[map_y * w1 + map_x] != s2_norm[sub_y * w2 + sub_x]:
                match = False
                break
        if match:
            break
    return match



