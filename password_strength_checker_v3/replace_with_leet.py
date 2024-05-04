from typing import Tuple

def replace_with_leet(password: str) -> Tuple[str, str]:    

    """
    Replace characters in the password with leet speak equivalents.

    This function transforms a given password by replacing characters with their 
    leet speak equivalents based on predefined mappings. It returns both the 
    transformed password and the characters that were substituted with leet speak 
    equivalents.

    Parameters:
        password (str): The original password to be transformed.

    Returns:
        Tuple[str, str]: A tuple containing the transformed password with leet 
        speak substitutions and the characters that were substituted with leet 
        speak equivalents. Both strings are returned in lowercase.
    """
        
    # Define a dictionary containing mappings of letters to their leet speak replacements
    leet_speak_replacements = { 
        'A': ['4', '/\\', '@'],
        'B': ['8'],
        'C': ['(', '{', '[', '<'],
        'D': ['|)'],
        'E': ['3'],
        'F': ['|='],
        'G': ['6', '9'],
        'H': ['|-|'],
        'I': ['1', '!', '|'],
        'J': ['_|'],
        'K': ['|<'],
        'L': ['|'],
        'M': ['|\\/|'],
        'N': ['|\\|'],
        'O': ['0', '|o'],
        'P': ['|>', '()'],
        'Q': ['()'],
        'R': ['|2'],
        'S': ['$', '5'],
        'T': ['7', '+'],
        'U': ['|_|'],
        'V': ['\\/'],
        'W': ['\\/\\/', 'vv'],
        'X': ['><'],
        'Y': ['`/`'],
        'Z': ['2']
    }
    
    # Initialize variables to store substitutions and the new password
    substitutions = ''
    new_password = ''
    
    # Loop through each character in the password
    for char in password:
        found = False  # Initialize a flag to track if a leet replacement is found for the current character
        # Loop through each key-value pair in the leet_speak_replacements dictionary
        for leet_char, substitutes in leet_speak_replacements.items():
            # Check if the current character's uppercase version is in the list of substitutes
            if char.upper() in substitutes:
                
                substitutions += char  # Add the original character to the substitutions string
                new_password += leet_char.lower()  # Add the leet replacement to the new password string (convert to lowercase)
                found = True  # Set the flag to True indicating a replacement was found
                break  # Break out of the inner loop since a replacement was found
        # If no replacement was found for the current character, simply add it to the new password as is
        if not found:
            new_password += char
    
    # Return the new password and the substitutions made
    return new_password, substitutions