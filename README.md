# Project Name
- Password Locker
## Description
- An amazing application that will help us manage our passwords and even generate new passwords for us.
## Behavior-driven development
- These are the behaviours that the application implements for use by a user.
## As a user I would like:
- To create an account with my details - log in and password
- Store my existing login credentials
- Generate a password for a new credential/account

| Behaviour | Input | Output |
| :---------------- | :---------------: | ------------------: |
| Display guides for navigation | **In terminal: $./run.py** | Hello Welcome to your Pass Word Locker. What is your name? (once you enter your nname):Use these known short codes to operate : SU -> SIGN UP.  DA -> Display your account.  LN ->LOGIN.  ex ->exit Pass Word Locker. |
| Display prompt for creating an account | **Enter: SU** | Enter account name, user name password and email .|
| Display prompt for login in | **Enter: LN** | Enter your account password to login |
| Once logged in | **You are now logged in to your  account** |  Use these short codes:CA -> Create new credential.DC -> Display your credentials list.  ex ->Log out your credentials account. |
| Display prompt for creating a credential | **Enter: CA** | Create new credential, Credential name: and password |
| Display a list of credentials | **Enter: DC** | Prints a list of saved credentials |
| Log out account  | **Enter: ex** | You have logged out your  account |

## Author 
- Ahmed Mukhtar

## Technologies useed
- Python3.6
## SetUp/ Installation Requirements
- python3.6
- For linux/uuntu users : Git
## Cloning
-  In your terminal

   - $ git clone https://github.com/mukhtarabdirahman/Password-Locker

   - $ cd password locker
## Running the Application
- $ ./run.py

## Testing the Application
-  To run the tests for the class file and check if it functions well:
    - $ python3.6 user_test.py
    - $ python3.6 credential_test.py
## Contact
mukhtarabdirahmanm@gmail.com
-0741421079

## License
MIT Copyright (c) 2019 Ahmed Mukhtar

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
