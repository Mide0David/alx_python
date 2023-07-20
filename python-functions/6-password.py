#!/usr/bin/python3

def validate_password(password):
    count = 0
    check = 0
    for i in password:
        count += 1
    if count > 8:
        check += 1
    if any(char.isupper() for char in password):
        check += 1
    if any(char.islower() for char in password):
        check += 1
    if any(num.isdigit() for num in password):
        check += 1
    if any(char.isspace() for char in password):
        check += 1
    if check == 4:
        return True
    else:
        return False
