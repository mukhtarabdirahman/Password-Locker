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
def main():
    print("Hello Welcome to our user list.")
    print("what would you like to do?")
    print('\n')
    
    while True:
        print("Use these short codes : cu - create a new user, du - display users, fu -find a user, x -exit the user list")
        short_code = input().lower()
        
        if short_code == 'cu':
            print("New User")
            print("-"*10)
            
            print("Username......")
            username = input()
            
            print("Password......")
            password = input()
            
            save_user(create_user(username,password))
            print('\n')
            print(f"New User {username} created")
            print('\n')
            
        elif short_code == 'du':
            if display_all_users():
                print("Here's the list of all saved users:")
                print('\n')
                
                for user in display_all_users():
                    print(f"{user.username}")
                    
                    print('\n')
                    
            else:
                
                print('\n')
                print("You don't seem to have any users saved yet.")
                print('\n')
                
        elif short_code == 'fu':
            
            print("Please enter the user you want to search:")
            
            search_user = input()
            
            if check_existing_users(search_user):
                
                searched_user = find_user(search_user)
                print(f"{searched_user.username}")
                print('-' * 20)
            else:
                print("That user does not exist!")



if __name__ == '__main__':

    main()



    

    
    

    
    




    
    
    
