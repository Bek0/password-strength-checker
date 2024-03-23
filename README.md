# Password Strength Checker And Analyzer .V3

This Python project aims to provide a comprehensive tool for evaluating the strength and validity of passwords. It includes functionalities for calculating password entropy, estimating crack time, checking for common weaknesses, replacing characters with leet speak equivalents, validating passwords based on specified criteria, and checking if passwords have been exposed in data breaches.

## Features

- **Password Validation**: Ensures that passwords meet specified criteria, such as containing only English characters, numbers, and allowed symbols.
- **Entropy Calculation**: Calculates the entropy of passwords to measure their randomness and complexity.
- **Crack Time Estimation**: Estimates the time required to crack passwords based on their entropy and common crack speeds.
- **Leet Speak Transformation**: Replaces characters in passwords with leet speak equivalents to enhance complexity.
- **Weakness Detection**: Identifies potential weaknesses in passwords, such as low entropy, sequential characters, repetition, ..., more details in code.
- **Pwned Password Check**: Checks if passwords have been exposed in data breaches by querying the (Have I Been Pwned) database.

## Project Structure

The project is organized into several Python modules, each responsible for a specific aspect of password analysis:

- `pass_validation.py`: Contains functions for validating passwords based on specified criteria.
- `pass_entropy.py`: Provides functions for calculating entropy, character amount, and possible combinations of passwords.
- `pass_crack_time.py`: Estimates the time required to crack passwords based on their entropy and crack speed.
- `pass_replace_with_leet.py`: Implements functionality to replace characters in passwords with leet speak equivalents.
- `pass_score_and_weaknesses.py`: Calculates the overall score of passwords and identifies potential weaknesses.
- `pwned.py`: Checks if passwords have been exposed in data breaches by querying the Have I Been Pwned API.

## Usage

To use the password strength checker, simply run the main file `main.py`. You will be prompted to enter a password, and the tool will provide detailed analysis including entropy, crack time estimation, weaknesses, and whether the password has been exposed in data breaches.

## Installation

To run the project, ensure you have Python 3 installed on your system. Clone the repository and install the required dependencies using pip:

## Requirements
  
- Python 3
- Requests library (for querying the Have I Been Pwned API)
- ```pip install -r requirements.txt```

## Contributing

Contributions to this project are welcome! If you have suggestions for improvements, bug fixes, or additional features, feel free to open an issue or submit a pull request.

**Note:** This project is intended for educational and informational purposes only. Always use strong, unique passwords and follow best practices for password security.
