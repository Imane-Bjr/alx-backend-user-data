#!/usr/bin/env python3
""" document """
import bcrypt


def hash_password(password: str) -> bytes:
    """document"""
    return bcrypt.hashpw(password.encode("utf-8"), bcrypt.gensalt())


def is_valid(hashed_password: bytes, password: str) -> bool:
    """doument"""
    return bcrypt.checkpw(password.encode("utf-8"), hashed_password)
