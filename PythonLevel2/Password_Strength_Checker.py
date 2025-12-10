import re

def check_password_strength(password: str) -> dict:
    """
    Checks password strength based on length, and the presence of 
    uppercase, lowercase, numbers, and special characters.

    Returns:
        A dictionary with strength rating, score, and improvement suggestions.
    """
    score = 0
    suggestions = []
    
    # 1. Define criteria checks
    # Criteria will be 1 point each, plus length bonus
    
    # --- Check Minimum Length (8 characters) ---
    min_length = 8
    if len(password) >= min_length:
        score += 10 # Base score for meeting minimum length
    else:
        suggestions.append(f"Increase length to at least {min_length} characters.")

    # --- Check for Uppercase Letters (A-Z) ---
    # re.search returns a match object if found
    if re.search(r"[A-Z]", password):
        score += 15
    else:
        suggestions.append("Add uppercase letters (A-Z).")

    # --- Check for Lowercase Letters (a-z) ---
    if re.search(r"[a-z]", password):
        score += 15
    else:
        suggestions.append("Add lowercase letters (a-z).")

    # --- Check for Numbers (0-9) ---
    if re.search(r"\d", password):
        score += 20
    else:
        suggestions.append("Add numbers (0-9).")

    # --- Check for Special Characters (non-alphanumeric, like !, @, #, etc.) ---
    # The pattern r"[^a-zA-Z0-9\s]" matches any character that is NOT a letter, number, or space.
    if re.search(r"[^a-zA-Z0-9\s]", password):
        score += 30
    else:
        suggestions.append("Add special characters (e.g., !, @, #, $, %).")
        
    # --- Additional Length Bonus (up to 10 points) ---
    # Award 1 point for every character past the minimum length, up to 10 extra points.
    length_bonus = min(10, max(0, len(password) - min_length))
    score += length_bonus
    
    # Cap the score at 100
    score = min(score, 100)

    # 2. Map score to strength rating
    strength = "weak"
    if score >= 90:
        strength = "very strong"
    elif score >= 70:
        strength = "strong"
    elif score >= 40:
        strength = "medium"
    
    # 3. Compile results
    return {
        'strength': strength,
        'score': score,
        'suggestions': suggestions
    }

while True:
    print(check_password_strength(input("Enter the password : ")))