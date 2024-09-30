# Enhanced Python script to check the strength of a given password.
# Judges password strength based on length, complexity requirements,
# presence of special characters, numbers, upper/lowercase letters,
# and checks against a list of common passwords using Have I Been Pwned API.
# Note: I started project around August 30th finally completed September 30

import re
import math
import hashlib
import requests

# Constants for HIBP API
HIBP_API = 'https://api.pwnedpasswords.com/range/'
USER_AGENT = 'PasswordStrengthValidator/1.0'


def calculate_entropy(password):
    # Calculate the entropy of the password. This is useful for randomness in password' probability
    # Formula for Entropy = log2(pool_size^length) = length * log2(pool_size)
    
    pool_size = 0
    if re.search(r'[a-z]', password):
        pool_size += 26
    if re.search(r'[A-Z]', password):
        pool_size += 26
    if re.search(r'\d', password):
        pool_size += 10
    if re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
        pool_size += 32  # This is the approximate number of common special characters

    if pool_size > 0:  
        entropy = len(password) * math.log2(pool_size) 
    else:
        entropy = 0

    return entropy


def is_common_password(password):
    # Check if the password has been compromised using the HIBP API.
    # Utilizes k-Anonymity to ensure password privacy.
    
    # took this line from a Github repo
    sha1_password = hashlib.sha1(password.encode('utf-8')).hexdigest().upper()
    prefix = sha1_password[:5] 
    suffix = sha1_password[5:] 
    """
    The following section from 'try' till 'except' was taken from GPT as I wasn't extremely 
    well-versed in API requests and request status/exception cases
    
    """
    try:
        response = requests.get(HIBP_API + prefix, headers={'User-Agent': USER_AGENT}, timeout=5)
        if response.status_code != 200:
            print("Error fetching data from HIBP API.")
            return False
        
        hashes = (line.split(':') for line in response.text.splitlines())
        for hash_suffix, count in hashes:
            if hash_suffix == suffix:
                return True  # Password has been pwned
        return False  # Password not found in breaches
    except requests.RequestException as e:
        print(f"Error connecting to HIBP API: {e}")
        return False  # In case of API failure, assume password is not pwned


def validate_password(password):
    # Validate the password and return its strength and feedback.
    
    feedback = []
    strength = "Weak" # initial strength complexity

    # Define password policies, password can't be too long, but has to follow some CIS criteria
    MIN_LENGTH = 12
    MAX_LENGTH = 64
    SPECIAL_CHARACTERS = r'[!@#$%^&*(),.?":{}|<>]'

    # Check password length
    if len(password) < MIN_LENGTH:
        feedback.append(f"Password must be at least {MIN_LENGTH} characters long.")
    elif len(password) > MAX_LENGTH:
        feedback.append(f"Password must not exceed {MAX_LENGTH} characters.")

    # Check for lowercase letters
    if not re.search(r'[a-z]', password):
        feedback.append("Add at least one lowercase letter.")

    # Check for uppercase letters
    if not re.search(r'[A-Z]', password):
        feedback.append("Add at least one uppercase letter.")

    # Check for digits
    if not re.search(r'\d', password):
        feedback.append("Add at least one digit.")

    # Check for special characters
    if not re.search(SPECIAL_CHARACTERS, password):
        feedback.append("Add at least one special character (!@#$%^&*(),.?\":{}|<>).")

    # Check against compromised passwords
    if is_common_password(password):
        feedback.append("This password has been compromised in a data breach. Choose a different one.")

    # Calculate entropy
    entropy = calculate_entropy(password)

    if entropy < 60:
        feedback.append("Password entropy is low. Make it more complex.")

    elif entropy < 80:
        strength = "Moderate"

    else:
        strength = "Strong"

    # Final strength determination
    if not feedback and strength == "Strong":
        feedback.append("Password is strong.")

    return strength, feedback

def main():
    """Main function to run the password validation loop."""
    while True:
        try:
            pwd = input("Enter a password (or type 'exit' to quit): ")
            if pwd.lower() in ['0', 'exit', 'quit']: # if user quits out of program
                print("No password used, ending program.")
                break

            strength, feedback = validate_password(pwd)
            print(f"Password strength: {strength}")
            for msg in feedback:
                print(f"- {msg}")
            print()  # Add an empty line for readability
        except KeyboardInterrupt: # I included this because sometimes user command/ctrl c out
            print("\nScript interrupted by user. Exiting.")
            break

if __name__ == "__main__": # added this for modularity and if I want to use in future scripts
    main()


"""Also Password Manager project coming soon, probably will do browser extension with it"""