import re

def is_valid_password(password: str) -> bool:

    """
    Check if the given password is valid based on certain criteria.
    
    This function verifies whether a password meets specific criteria for validity. 
    It checks if the password contains only allowed characters, which include 
    letters (both uppercase and lowercase), numbers, and certain special characters.

    Parameters:
        password (str): The password to check.
        
    Returns:
        bool: True if the password is valid, False otherwise.
    """
    
    # Define a regular expression pattern to match the allowed characters
    pattern = r"^[!@#$%^&*()-=_+/\\|`',.:;~\"<>?{}a-zA-Z0-9]+$"
    
    # Check if the password matches the pattern
    if re.match(pattern, password):
        return True
    else:
        return False
