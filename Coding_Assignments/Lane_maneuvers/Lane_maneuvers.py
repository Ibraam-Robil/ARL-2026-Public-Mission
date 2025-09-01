def analyze_drive(lanes: list[int]) -> tuple[int, int]:

    lane_changes = 0
    dangerous_maneuvers = 0

    for i in range(1, len(lanes)):
        if lanes[i] != lanes[i - 1]:
            lane_changes += 1
            if abs(lanes[i] - lanes[i - 1]) > 1:
                dangerous_maneuvers += 1

    return lane_changes, dangerous_maneuvers

    """
    Analyzes the driving behavior based on lane positions.
    
    Args:
        lanes (list[int]): List of lane positions at each second (0, 1, or 2).
    
    Returns:
        tuple[int, int]: (number of lane changes, number of dangerous maneuvers)
    """
    # pass