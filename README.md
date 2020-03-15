# CS9163-Assignment2
## Description
This program returns user information stored in the database after authentication.
## Requirements
`pip install flask`
## Initialization
`export FLASK_APP=run.py`\
`flask run`\
Open 127.0.0.1:5000 in the web browser
## Running the program
1. Enter `Adam` in username and `mada` for the password
2. The browser should return the information for the user
3. Click Login
## SQLi attack
1. Enter `Adam` in username
2. Enter `' OR 1=1 OR 1='` in password
3. Click Login
4. The browser returns the information for all users in the database
##XSS attack
1. Enter `<script>alert("XSS success!")</script>` in username
2. Enter `pw` in password
3. Click Login
4. The browser would run the javascript defined in #1
