from typing import Dict, List, Tuple

def count_features(password: str) -> Tuple[Dict[str, int], int, Dict[str, int], List[str]]:

    """
    Count various features of a given password and calculate its overall score.

    This function analyzes a given password to determine various characteristics 
    such as length, presence of uppercase and lowercase letters, numbers, special 
    characters, repeating characters, consecutive characters, sequential characters, 
    and more. It calculates an overall score based on these features and identifies 
    potential weaknesses in the password.

    Parameters:
        password (str): The password to analyze.

    Returns:
        Tuple[Dict[str, int], int, Dict[str, int], List[str]]: A tuple containing:
            - A dictionary containing counts of different features of the password.
            - The overall score of the password.
            - A dictionary containing weights for each feature.
            - A list of potential weaknesses in the password.
    """

    weaknesses=[]  # Let's start with an empty list to keep track of any weaknesses in the password.
    
    # First, let's define a dictionary to store various counts of password features.
    counts = {
        "length": len(password),  # Counting the length of the password.
        "upper_char": 0,  # Initializing count of uppercase characters.
        "lower_char": 0,  # Initializing count of lowercase characters.
        "numbers": 0,  # Initializing count of numeric characters.
        "special_characters": 0,  # Initializing count of special characters.
        "middle_numbers": 0,  # Initializing count of numbers in the middle of the password.
        "middle_special_char": 0,  # Initializing count of special characters in the middle of the password.
        "letter_only": 0,  # Flag for indicating if password contains letters only.
        "number_only": 0,  # Flag for indicating if password contains numbers only.
        "repeating_char": 0,  # Count of repeating characters.
        "consecutive_uppercase": 0,  # Count of consecutive uppercase characters.
        "consecutive_lowercase": 0,  # Count of consecutive lowercase characters.
        "consecutive_numbers": 0,  # Count of consecutive numeric characters.
        "sequential_letters": 0,  # Count of sequences of letters.
        "sequential_numbers": 0  # Count of sequences of numbers.
    }

    # Now, let's start counting various features of the password.
    # Counting lowercase, uppercase, numbers, and special_characters
    counts["lower_char"] = sum(1 for char in password if char.islower())  # Counting lowercase characters.
    counts["upper_char"] = sum(1 for char in password if char.isupper())  # Counting uppercase characters.
    counts["numbers"] = sum(1 for char in password if char.isdigit())  # Counting numeric characters.
    
    symbol=0  # Initializing count for special characters.
    for i in password  :
        if i in r"[!@#$%^&*()-=_+/\|`',.:;~\"<>?{}]":
            symbol+=1
    counts["special_characters"]=symbol  # Counting special characters.
    
    # Counting repeating characters
    for char in set(password):
        if password.count(char) > 1:
            counts["repeating_char"] += 1  # Incrementing count if character repeats.

    # Counting middle numbers and middle special characters
    if len(password) > 2:
        middle_section = password[1:-1]
        counts["middle_numbers"] = sum(1 for char in middle_section if char.isdigit())  # Counting numbers in middle.
        counts["middle_special_char"] = sum(1 for char in middle_section if char in r"[!@#$%^&*()-=_+/\|`',.:;~\"<>?{}]")  # Counting special characters in middle.

    # Counting consecutive uppercase, lowercase, and numbers
    for i in range(len(password) - 2):
        if password[i].isupper() and password[i + 1].isupper() and password[i + 2].isupper():
            counts["consecutive_uppercase"] += 1  # Incrementing count of consecutive uppercase.
        elif password[i].islower() and password[i + 1].islower() and password[i + 2].islower():
            counts["consecutive_lowercase"] += 1  # Incrementing count of consecutive lowercase.
        elif password[i].isdigit() and password[i + 1].isdigit() and password[i + 2].isdigit():
            counts["consecutive_numbers"] += 1  # Incrementing count of consecutive numeric characters.

    # Counting sequential letters and numbers
    sequential_letters=""  # Variable to store identified sequential letters.
    sequential_numbers=""  # Variable to store identified sequential numbers.
    for i in range(len(password) - 2):
        if password[i].isalpha() and password[i + 1].isalpha() and password[i + 2].isalpha(): 
            if (ord(password[i]) + 1 == ord(password[i+1]) == ord(password[i+2]) - 1) and password[i]+password[i+1]+password[i+2] not in sequential_letters:
                counts["sequential_letters"] += 1  # Incrementing count of sequential letters.
                sequential_letters+=password[i]+password[i+1]+password[i+2]  # Storing identified sequence.
            elif (ord(password[i]) - 1 == ord(password[i+1]) == ord(password[i+2]) + 1) and password[i]+password[i+1]+password[i+2] not in sequential_letters:
                counts["sequential_letters"] += 1  # Incrementing count of sequential letters.
                sequential_letters+=password[i]+password[i+1]+password[i+2]  # Storing identified sequence.
        elif password[i].isdigit() and password[i + 1].isdigit() and password[i + 2].isdigit():
            if (int(password[i]) + 1 == int(password[i+1]) == int(password[i+2]) - 1)  and password[i]+password[i+1]+password[i+2] not in sequential_numbers: # 12345
                counts["sequential_numbers"] += 1  # Incrementing count of sequential numbers.
                sequential_numbers+=password[i]+password[i+1]+password[i+2]  # Storing identified sequence.
            if (int(password[i]) - 1 == int(password[i+1]) == int(password[i+2]) + 1) and password[i]+password[i+1]+password[i+2] not in sequential_numbers: # 54321
                counts["sequential_numbers"] += 1  # Incrementing count of sequential numbers.
                sequential_numbers+=password[i]+password[i+1]+password[i+2]  # Storing identified sequence.
            if (abs(int(password[i]) - int(password[i+1])) == abs(int(password[i+2]) - int(password[i+1]))) and password[i]+password[i+1]+password[i+2] not in sequential_numbers: # 13579
                counts["sequential_numbers"] += 1  # Incrementing count of sequential numbers.
                sequential_numbers+=password[i]+password[i+1]+password[i+2]  # Storing identified sequence.

    # Checking if password is letter only or number only
    if counts["upper_char"] + counts["lower_char"] == counts["length"]:
        counts["letter_only"] = 1  # Flag indicating password contains letters only.
    elif counts["numbers"] == counts["length"]:
        counts["number_only"] = 1  # Flag indicating password contains numbers only.
    
    # Define weights for each feature
    weight = {
        "length": counts["length"] * 4,
        "upper_char":((counts["length"] - counts["upper_char"])*2)  if counts["upper_char"] >= 1 else 0,
        "lower_char":((counts["length"] - counts["lower_char"])*2)  if counts["lower_char"] >= 1 else 0,
        "numbers": (counts["numbers"] * 4) if counts['length'] > counts['numbers'] else 0,
        "special_characters": counts["special_characters"] * 6,
        "middle_numbers": counts["middle_numbers"] * 2,
        "middle_special_char": counts["middle_special_char"] * 2,
        "letter_only": -(counts["letter_only"] * counts["length"]),
        "number_only": -(counts["number_only"] * counts["length"]),
        "repeating_char": -1 if counts["repeating_char"] >= 1 else 0,
        "consecutive_uppercase": -(counts["consecutive_uppercase"] * 2),
        "consecutive_lowercase": -(counts["consecutive_lowercase"] * 2),
        "consecutive_numbers": -(counts["consecutive_numbers"] * 2),
        "sequential_letters": -(counts["sequential_letters"] * 3),
        "sequential_numbers": -(counts["sequential_numbers"] * 3)
    }

    # Let's identify weaknesses based on the password features.
    if len(password) < 12:
        weaknesses.append("Your password should be 12 characters or longer")
    if counts['upper_char'] == 0:
        weaknesses.append("Password should contain uppercase")
    if counts['lower_char'] == 0:
        weaknesses.append("Password should contain lowercase")
    if counts['numbers'] == 0:
        weaknesses.append("Password should contain number")
    if counts['special_characters'] == 0:
        weaknesses.append("Password should contain special character")
    if counts['repeating_char'] != 0:
        weaknesses.append("Your password contain repeating character")
    if counts['consecutive_uppercase'] != 0:
        weaknesses.append("Your password contain consecutive uppercase")
    if counts['consecutive_lowercase'] != 0:
        weaknesses.append("Your password contain consecutive lowercase")
    if counts['consecutive_numbers'] != 0:
        weaknesses.append("Your password contain consecutive numbers")
    if counts['sequential_letters'] != 0:
        weaknesses.append("Your password contain sequential letters")
    if counts['sequential_numbers'] != 0:
        weaknesses.append("Your password contain sequential numbers")

    # Finally, let's calculate the overall score of the password based on its features.
    score=0  # Initializing score.
    for i in counts:
        score+=weight[i]  # Calculating overall score.

    # Returning the counts of features, the overall score, the weight of each feature, and any potential weaknesses.
    return counts,score,weight,weaknesses