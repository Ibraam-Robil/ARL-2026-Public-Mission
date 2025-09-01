def fuse_readings(sensor1: list[int], sensor2: list[int], sensor3: list[int]) -> list:

    fused = []

    for t in range(len(sensor1)):
        readings = [sensor1[t], sensor2[t], sensor3[t]]
        # Majority vote
        majority = max(set(readings), key=readings.count)
        if readings.count(majority) > 1:
            fused.append(majority)
        else:
            # No majority, take average
            fused.append(sum(readings) // 3)

    return fused

    """
    Combines sensor readings using majority vote logic.  
    If no majority exists (all different), fall back to the average of the three readings.  
    
    Args:
        sensor1, sensor2, sensor3 (list[int]): Readings from 3 sensors.
    
    Returns:
        list: Final fused readings for each timestep.
              - Majority value if at least 2 sensors agree.
              - Average value if no consensus.
    """
    # pass
