import math

def calculate_entropy(password):
    pool = 0
    if any(c.islower() for c in password):
        pool += 26
    if any(c.isupper() for c in password):
        pool += 26
    if any(c.isdigit() for c in password):
        pool += 10
    special_chars = r"!@#$%^&*()-_=+[]{};:'\",.<>?/|\\"
    if any(c in special_chars for c in password):
        pool += 32

    if pool == 0:
        return 0

    entropy = len(password) * math.log2(pool)
    return round(entropy, 2)

common_words = ["password", "123456", "qwerty", "admin", "user"]

def analyze_password(password):
    issues = []
    suggestions = []

    if len(password) < 8:
        issues.append("Password is too short")
        suggestions.append("Use at least 12–14 characters")

    for word in common_words:
        if word in password.lower():
            issues.append("Contains common weak pattern: " + word)
            suggestions.append("Avoid predictable words")
            break

    if not any(c.isdigit() for c in password):
        issues.append("No numbers in password")
        suggestions.append("Add numbers")

    if not any(c.isupper() for c in password):
        issues.append("Missing uppercase letters")
        suggestions.append("Add uppercase letters")

    if not any(c.islower() for c in password):
        issues.append("Missing lowercase letters")
        suggestions.append("Add lowercase letters")

    if not any(c in r"!@#$%^&*()-_=+[]{};:'\",.<>?/|\\" for c in password):
        issues.append("No special characters")
        suggestions.append("Add special characters")

    entropy = calculate_entropy(password)

    if entropy < 40:
        strength = "Weak"
    elif entropy < 60:
        strength = "Moderate"
    else:
        strength = "Strong"

    # Create a nice, readable output
    print(f"\nPassword Analysis for: '{password}'")
    print(f"Entropy: {entropy}")
    print(f"Strength: {strength}")
    if issues:
        print("\nIssues detected:")
        for i, issue in enumerate(issues, 1):
            print(f"{i}. {issue}")
    if suggestions:
        print("\nSuggestions:")
        for i, suggestion in enumerate(suggestions, 1):
            print(f"{i}. {suggestion}")
    print("\n")

pwd = input("Enter a password to analyze: ")
analyze_password(pwd)
