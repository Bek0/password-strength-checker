import requests
import hashlib
from typing import Optional, Tuple

# ANSI escape codes for text formatting and colors
BOLD = '\033[1m'
END_BOLD = '\033[0m'
RED = '\033[91m'
GREEN = '\033[92m'
END_COLOR = '\033[0m'


def check_pwned_password(password: str) -> Tuple[Optional[str], Optional[int]]:    

    """
    Check if the given password has been exposed in a data breach.
    
    This function hashes the given password using the SHA-1 algorithm and checks
    if the hashed password exists in the Have I Been Pwned database. If found, 
    it returns a warning message along with the count of occurrences, indicating
    that the password has been compromised. If not found, it returns a message 
    indicating that the password has not been exposed.
    
    Parameters:
        password (str): The password to check.
        
    Returns:
        tuple: A tuple containing a message indicating the status of the password 
            and the count of occurrences if the password has been exposed, otherwise None.
    """

    hashed_password = hashlib.sha1(password.encode()).hexdigest().upper()
    # Hash the password using SHA-1 algorithm and convert it to uppercase hexadecimal.
    
    prefix = hashed_password[:5]
    # Extract the first 5 characters of the hashed password (prefix).
    
    api_call = f'https://api.pwnedpasswords.com/range/{prefix}'
    # Construct the API call URL using the password prefix.
    
    try:
        response = requests.get(api_call)
        # Send a GET request to the API endpoint.
        
        if response.status_code == 200:
            # Check if the response status code is successful.
            
            hashes = response.text.split('\r\n')
            # Split the response text into individual lines.
            
            found = next((h.split(':') for h in hashes if h.startswith(hashed_password[5:])), None)
            # Find the hashed password suffix in the response.
            
            if found:
                count = int(found[1])
                # Extract the count of occurrences of the password from the response.
                return f'This password has been seen {BOLD}{count}{END_BOLD} times before',count
                # Print a warning message with the count of occurrences.
                
            else:
                return 'Good news — no pwnage found', None
                # Print a message indicating that the password has not been found in the database.
                
        else:
            return f'Error: {response.status_code}', None
            # Print an error message if the API request was not successful.
            
    except Exception as e:
        return f'Error: {e}', None
        # Print an error message if an exception occurs during the process.
