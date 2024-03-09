import pass_crack_time
def count_features(password):
    """
    Welcome to the password strength analyzer! Let's dive deep into your password's features.
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
        if i in r"[!@#$%^&*()-_+=<>?/{}|~.-]":
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
        counts["middle_special_char"] = sum(1 for char in middle_section if char in r"[!@#$%^&*()-_+=<>?/{}|~.-]")  # Counting special characters in middle.

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
    if weight['upper_char'] == 0:
        weaknesses.append("Password should contain uppercase")
    if weight['lower_char'] == 0:
        weaknesses.append("Password should contain lowercase")
    if weight['numbers'] == 0:
        weaknesses.append("Password should contain number")
    if weight['special_characters'] == 0:
        weaknesses.append("Password should contain special character")
    if weight['repeating_char'] == -1:
        weaknesses.append("Your password contain repeating character")
    if weight['consecutive_uppercase'] != 0:
        weaknesses.append("Your password contain consecutive uppercase")
    if weight['consecutive_lowercase'] != 0:
        weaknesses.append("Your password contain consecutive lowercase")
    if weight['consecutive_numbers'] != 0:
        weaknesses.append("Your password contain consecutive numbers")
    if weight['sequential_letters'] != 0:
        weaknesses.append("Your password contain sequential letters")
    if weight['sequential_numbers'] != 0:
        weaknesses.append("Your password contain sequential numbers")

    # Finally, let's calculate the overall score of the password based on its features.
    score=0  # Initializing score.
    for i in counts:
        score+=weight[i]  # Calculating overall score.

    # Returning the counts of features, the overall score, the weight of each feature, and any potential weaknesses.
    return counts,score,weight,weaknesses

def replace_with_leet(password):
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


password = input("Enter password: ")  # Prompting user to input a password.

# Calculating features count, score, features weight, and weaknesses of the password.
features_count, score, features_weight, weaknesses = count_features(password)

# Calculating entropy, crack time, time unit, and possible combinations for the password.
etropy, crack_time, time_unit, possible_combinations = pass_crack_time.calculate_crack_time(password)

# Replacing characters in the password with leet speak equivalents.
new_password, substitutions = replace_with_leet(password)

print(f"\nPassword:{password}\n")  # Printing the original password.

max_length = max(len(feature) for feature in features_count.keys())  # Finding the maximum length of feature names.

# Printing feature properties along with their length and weight.
print(f"{'Properties'.ljust(max_length+1)}:len weight")
print("_" * 31)  # Printing a line to separate header.

# Iterating through features and printing their counts and weights.
for feature in features_count:
    print(f"{feature.ljust(max_length)} : {str(features_count[feature]).rjust(2)} {str(features_weight[feature]).rjust(3)}")

# Determining the strength of the password based on its score.
if score >= 91:
    strength = "Excellent"
elif 80 <= score < 91:
    strength = "Very Strong"
elif 60 < score < 80:
    strength = "Strong"
elif 40 < score <= 60:
    strength = "Good"
elif 20 <= score <= 40:
    strength = "Weak"
elif 0 <= score < 20:
    strength = "Very Weak"


print("score".ljust(max_length + 2), score)  # Printing the score of the password.

# Adding a weakness if the entropy is below 74.
if etropy < 74 :
    weaknesses.append("Password's entropy should be 74 or higher.")

# Printing weaknesses if any, else indicating no weaknesses.
if len(weaknesses)>=1:
    print("\nWeaknesses:")
    for weakness in weaknesses:
        print(f"- {weakness}")
else:
    print("The password doesn't has any weakness")

print(f"\nStrength of the password: {strength}")  # Printing the strength of the password.

print(f"\nEntropy of the password: {etropy}")  # Printing the entropy of the password.
print(f"\nEstimated crack time: {crack_time} {time_unit}")  # Printing the estimated crack time.
print(f"\nPossible combinations for password: {possible_combinations}")  # Printing the possible combinations.

print("\nSubstitutions made during leet speak replacement:")  # Printing the substitutions made during leet speak replacement.
seen=''  # Initializing a variable to keep track of seen characters.
for original_char, substituted_char in zip(password, new_password):
    if original_char != substituted_char and original_char not in seen:
        seen+=original_char
        print(f"{original_char} -> {substituted_char}", end=" / ")  # Printing the substitution.
print(f"\n\nPassword after replacing with leet speak: {new_password}")  # Printing the password after leet speak replacement.
print("\nNote: If your password after Substitutions contains common words or names, consider changing it for better security.\n")  # Printing a note for the user.
