import math
from typing import Dict, List, Tuple
def calculate_entropy(password: str) -> Tuple[float, int, int]:
    
    """
    Calculate the entropy of a password.

    This function computes the entropy of a given password, which represents the
    measure of uncertainty or randomness in the password. It calculates the entropy
    based on the number of possible combinations of characters present in the password.

    Parameters:
        password (str): The password string for which entropy is to be calculated.

    Returns:
        Tuple[float, int, int]: A tuple containing the entropy of the password,
        the total number of possible characters, and the number of possible combinations.
        The entropy value is returned as a float rounded to two decimal places.
    """

    char_amount = 0  # Initializing the character amount to 0
    char_sets = [False, False, False, False]  # List to track if each character set is present
    char_nums = [26, 26, 10, 32]  # List containing the number of characters in each character set

    # Looping through each character in the password
    for char in password:
        if char.islower():  # Checking if the character is lowercase
            char_sets[0] = True  # Setting the corresponding character set flag to True
        elif char.isupper():  # Checking if the character is uppercase
            char_sets[1] = True  # Setting the corresponding character set flag to True
        elif char.isdigit():  # Checking if the character is a digit
            char_sets[2] = True  # Setting the corresponding character set flag to True
        else:  # If the character is not lowercase, uppercase, or a digit, it's a special character
            char_sets[3] = True  # Setting the corresponding character set flag to True
    
    # Calculating the total number of possible characters based on the character sets present
    for x in range(4):
        if char_sets[x]:
            char_amount += char_nums[x]
    
    length = len(password)  # Getting the length of the password
    
    possible_combinations = char_amount ** length  # Calculating the possible combinations

    # Calculating the entropy using the formula: entropy = log2(char_amount**length)
    entropy = math.log2(possible_combinations)
    
    return round(entropy,2), char_amount, possible_combinations # Returning the calculated entropy, character amount, and possible combinations
