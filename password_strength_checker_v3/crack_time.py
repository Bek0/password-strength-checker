from typing import Tuple

def calculate_crack_time(possible_combinations: int) -> Tuple[int, str]:    
    """
    Calculate the estimated time required to crack a password based on its entropy and the assumed crack speed.
    
    This function calculates the time required to crack a password by estimating the number of possible combinations
    for the password and dividing it by a default crack speed. It then converts the time into appropriate units for
    better readability.
    
    Parameters:
        possible_combinations (int): The possible_combinations to calculate the crack_time.
        
    Returns:
        Tuple[int, str, int]: A tuple containing the estimated time to crack the password,
        the time unit used for the crack time (e.g., seconds, minutes, hours).
    """

    crack_speed = (10 ** 15)  # Default crack speed in hashes per second

    # Calculating the time to crack the password based on possible_combinations and crack_speed
    time_to_crack = (possible_combinations) / crack_speed
    
    time_unit = "second"  # Default time unit
    
    # Converting time to appropriate units for better readability
    if time_to_crack >= 60:
        time_to_crack /= 60  # Convert seconds to minutes
        time_unit = "minute"
        if time_to_crack >= 60:
            time_to_crack /= 60  # Convert minutes to hours
            time_unit = "hour"
            if time_to_crack >= 24:
                time_to_crack /= 24  # Convert hours to days
                time_unit = "day"
                if time_to_crack >= 30:
                    time_to_crack /= 30  # Convert days to months
                    time_unit = "month"
                    if time_to_crack >= 12:
                        time_to_crack /= 12  # Convert months to years
                        time_unit = "year"
                        if time_to_crack >= 100:
                            time_to_crack /= 100  # Convert years to century
                            time_unit = "century"

    crack_time_rounded = round(time_to_crack)  # Rounding the crack time to the nearest integer
    return  crack_time_rounded, time_unit  # Returning the crack time, and time unit
