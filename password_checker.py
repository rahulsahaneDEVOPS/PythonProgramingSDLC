import string

def check_password_strength(password):
    # Criteria flags
    has_upper = any(char.isupper() for char in password)
    has_lower = any(char.islower() for char in password)
    has_digit = any(char.isdigit() for char in password)
    
    special_characters = string.punctuation  # !"#$%&'()*+,-./:;<=>?@[\]^_`{|}~
    has_special = any(char in special_characters for char in password)

    # Check all conditions
    if (len(password) >= 8
        and has_upper
        and has_lower
        and has_digit
        and has_special):
        return True
    else:
        return False


# -------------------------
# Main Program
# -------------------------
user_password = input("Enter a password to check strength: ")

if check_password_strength(user_password):
    print("✅ Strong password! All security requirements are met.")
else:
    print("❌ Weak password! Please ensure the following:")
    print("- At least 8 characters long")
    print("- Contains uppercase and lowercase letters")
    print("- Contains at least one digit")
    print("- Contains at least one special character (!,@,#,$,%, etc.)")
