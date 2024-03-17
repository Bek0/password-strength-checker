import math
def calculate_entropy(password):
    """
    Calculate the entropy of a password.
    
    Inputs:
    - password: The password string.
    
    Outputs:
    - entropy: The entropy of the password.
    - char_amount: The total number of possible characters.
    - possible_combinations: The number of possible combinations of the password in a readable format (multiplied by 10 to the power).
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
    # print(char_amount)
    # Convert possible_combinations to readable format (multiplied by 10 to the power)
    # power_of_ten = 0
    # while possible_combinations >= 10:
    #     possible_combinations /= 10
    #     power_of_ten += 1
    # possible_combinations_readable = "{} × 10^{}".format(int(possible_combinations), power_of_ten)

    # Calculating the entropy using the formula: entropy = log2(char_amount**length)
    entropy = math.log2(char_amount ** length) 
    return entropy, char_amount, possible_combinations # Returning the calculated entropy, character amount, and possible combinations
