#!/usr/bin/env python3.6
from user import User

def create_user(username,password):
    """
    Function to create a user
    """
    new_user = User(username,password)
    return new_user

