import pass_entropy  # Importing the pass_entropy module for entropy calculation

def calculate_crack_time(password):
    crack_speed = (10 ** 9) * 100  # Default crack speed in hashes per second

    # Calculating the entropy of the password
    entropy, char_amount, possible_combinations = pass_entropy.calculate_entropy(password)
    entropy_value = round(entropy, 2)  # Rounding the entropy value to two decimal places

    password_length = len(password)  # Getting the length of the password

    # Calculating the time to crack the password based on entropy and crack speed
    time_to_crack = (char_amount ** password_length) / crack_speed
    
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

    crack_time_rounded = round(time_to_crack)  # Rounding the crack time to the nearest integer
    return entropy_value, crack_time_rounded, time_unit, possible_combinations  # Returning the entropy value, crack time, and time unit
