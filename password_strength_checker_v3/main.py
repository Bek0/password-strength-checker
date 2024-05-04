import crack_time
import score_and_weaknesses
import replace_with_leet
import validation
import entropy
import pwned

# ANSI escape codes for text formatting and co0

BOLD = '\033[1m'
END_BOLD = '\033[0m'
RED = '\033[91m'
GREEN = '\033[92m'
YELLOW = '\033[93m'
BLUE = '\033[94m'
END_COLOR = '\033[0m'

password = input("Enter password: ").replace(" ", "")  # Prompting user to input a password.

# Check if the password is valid
if not validation.is_valid_password(password):
    print(RED + "Invalid password. Please use only English characters, numbers, and allowed symbols." + END_COLOR)
    exit()

# Calculating features count, score, features weight, and weaknesses of the password.
features_count, score, features_weight, weaknesses = score_and_weaknesses.count_features(password)

# Calculating entropy, char amount and possible combinations for the password.
etropy, char_amount, possible_combinations = entropy.calculate_entropy(password)

# Calculating crack time and time unit for the password.
crack_time, time_unit = crack_time.calculate_crack_time(possible_combinations)

print("\nPassword:", BOLD + password + END_BOLD)  # Printing the original password.

max_length = max(len(feature) for feature in features_count.keys())  # Finding the maximum length of feature names.

# Printing feature properties along with their length and weight.
print(f"\n{BOLD}{'Properties'.ljust(max_length+1)}:{END_BOLD}len  weight in score")
print("_" * 31)  # Printing a line to separate header.

# Iterating through features and printing their counts and weights.
for feature in features_count:
    print(f"{feature.ljust(max_length)} : {str(features_count[feature]).rjust(2)} {str(features_weight[feature]).rjust(3)}")

# Determining the strength of the password based on its score.
if score >= 125:
    strength = GREEN + "Excellent" + END_COLOR
elif 100 <= score < 125:
    strength = GREEN + "Very Strong" + END_COLOR
elif 75 < score < 100:
    strength = YELLOW + "Strong" + END_COLOR
elif 50 < score <= 75:
    strength = YELLOW + "Good" + END_COLOR
elif 25 <= score <= 50:
    strength = RED + "Weak" + END_COLOR
elif score < 25:
    strength = RED + "Very Weak" + END_COLOR

print("\n"+BOLD + "Score:".ljust(max_length + 2) + END_BOLD, BOLD + f"{score}" + END_BOLD)  # Printing the score of the password.

# Adding a weakness if the entropy is below 74.
if etropy < 74:
    weaknesses.append("Password's entropy should be 74 or higher.")

# Printing weaknesses if any, else indicating no weaknesses.
if len(weaknesses) >= 1:
    print("\nWeaknesses:")
    for weakness in weaknesses:
        print(RED + "- " + weakness + END_COLOR)  # Print weaknesses in red color
else:
    print(GREEN + "The password doesn't have any weaknesses" + END_COLOR)

print("\nStrength of the password:", strength)  # Printing the strength of the password.
print("\nEntropy of the password:", BOLD + f"{etropy}" + END_BOLD)  # Printing the entropy of the password.
print(f"\nYour password will be bruteforced with an average home computer in approximately...: {BOLD}{crack_time} {time_unit}{END_BOLD}")  # Printing the estimated crack time.
print(f"\nPossible combinations for password: {BOLD}{possible_combinations}{END_BOLD}\n")  # Printing the possible combinations.

if features_count['special_characters'] >= 1:
    new_password, substitutions = replace_with_leet.replace_with_leet(password)
    seen=''  # Initializing a variable to keep track of seen characters.
    for original_char, substituted_char in zip(password, new_password):
        if original_char != substituted_char and original_char not in seen:
            seen+=original_char
            print(f"{original_char} -> {substituted_char}", end=" / ")  # Printing the substitution.
    if len(seen) >= 1:
        print("\n\nPassword after replacing with leet speak:", BOLD + new_password + END_COLOR )  # Printing the password after leet speak replacement.
        print("\nNote: If your password after substitutions (replacing with leet speak) contains common words or names, consider changing it for better security.\n")  # Printing a note for the user.

# Call the function to check if the password has been pwned
pwned_value,number = pwned.check_pwned_password(password)
if "no pwnage" in pwned_value:
    print(GREEN + pwned_value + END_COLOR)
elif "Error" in pwned_value:
    print(pwned_value)
else:
    print(RED + f"This password has been seen {BOLD}{number}{END_BOLD}{RED} times before" + END_COLOR + "\n")