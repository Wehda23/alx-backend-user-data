#!/usr/bin/env python3
"""
File for password encryption
"""
import bcrypt


def hash_password(password: str) -> bytes:
    """
    Hashes a password using bcrypt
    """
    encoded = password.encode()
    hashed = bcrypt.hashpw(encoded, bcrypt.gensalt())

    return hashed


def is_valid(hashed_password: bytes, password: str) -> bool:
    """
    Checks if a password is valid
    """
    valid = False
    encoded = password.encode()
    if bcrypt.checkpw(encoded, hashed_password):
        valid = True
    return valid
