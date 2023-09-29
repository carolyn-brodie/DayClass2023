def is_password_strong(password):
    """Return True if password is strong, False otherwise.
    a.	At least 12 characters
b.	At least one upper-case character
c.	At least one lower-case character
d.	At least one  digit
e.	At least one special character
"""
    if len(password) < 12:
        return False
    if password.islower():
        return False
    if password.isupper():
        return False
    if password.isdigit():
        return False
    if password.isalnum():
        return False
    return True

print(is_password_strong('abssdfgJKLMNO'))

