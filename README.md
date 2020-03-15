# CS9163-Assignment2
## Description
This program returns user information stored in the database after authentication.
## Requirements
`pip install flask`
## Initialization
`export FLASK_APP=app.py`\
`flask run`\
Open 127.0.0.1:5000 in the web browser
## Running the program
1. Enter `Adam` in username and `mada` for the password
2. The browser should return the information for the user
3. Click Login
## SQLi attack
SQL injection is a code injection technique, used to attack data-driven applications, in which malicious SQL statements are inserted into an entry field for execution.
1. Enter `Adam` in username
2. Enter `' OR 1=1 OR 1='` in password
3. Click Login
4. The browser returns the information for all users in the database
## XSS attack
XSS attacks enable attackers to inject client-side scripts into web pages viewed by other users. A cross-site scripting vulnerability may be used by attackers to bypass access controls such as the same-origin policy.
1. Enter `<script>alert("XSS success!")</script>` in username
2. Enter `pw` in password
3. Click Login
4. The browser would run the javascript defined in #1
## References
https://en.wikipedia.org/wiki/Cross-site_scripting

https://en.wikipedia.org/wiki/SQL_injection

