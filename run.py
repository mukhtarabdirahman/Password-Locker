#!/usr/bin/env python3.6
from user import User

def create_user(username,password):
    """
    Function to create a user
    """
    new_user = User(username,password)
    return new_user
def save_user(user):
    """
    Function to save user
    """
    
    user.save_user()
    
def delete_user(user):
    '''
    Function that deletes a user
    '''
    
    user.delete_user()
    
def find_user(username):
    """
    Function that find a User
    """
    return User.find_by_username(username)

def check_existing_users(username):
    """
    Function that search for existing user
    """
    return User.user_exist(username)

def display_all_users():
    """
    Function that returns all the saved  user
    """
    return User.display_all_users()
    

    
    

    
    




    
    
    
