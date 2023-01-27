<b>INFORMATION:</b>
The new user is named al.
The files requested were left under ~/home/al/
The server file is at /home/al/github/MaxTest/https_server/https_server.py
Run it with:  sudo python3 https_server.py
I created a service that runs that command on startup so theoretically my website should always be up; however, I have noticed the site stop responding after a period of time and the service needs to be restarted.
The service can be restarted with:  sudo systemctl restart al-https-server.service



TASKS COMPLETED:
Using server, username, and password details provided to you, connect to your assigned server using ssh.
Create a new user account as the username of your choice
Login as that new user
In your home directory, create a new directory called “memories”. Inside of it, create a text file which describes your favorite memory. Set the file access to full permissions for all the system (777).
Create a shell script which does the following:
a. Makes a copy of your memories file, naming it “privatemems”
b. Sets permissions of the new file to 755
c. Appends to the file the current system time
Create a local git repository
a. You may do this either starting locally and pushing to an origin (online) location of your choice, or you may create it online first and clone it to your home directory.
Using the language you are most comfortable with, create an HTTPS (you’ll need to generate a keypair) server application...
Make sure to regularly commit changes in your local repo while developing and push those changes to your online repository.
STRETCH GOAL 1. Configure system’s firewall to only allow SSH and HTTPS connections
STRETCH GOAL 2. Get a free domain name for the host ( https://www.noip.com/ is an option)
STRETCH GOAL 3. Get a LetsEncrypt SSL certificate for your server so that it stops complaining about your
unsigned certificate (requires a domain name)
Email/call/message me.

TASKS NOT COMPLETED:
a. Key-value server:
i. POST request handler where a user may specify a value to be stored under a key
ii. POST request handler where a user may request the value for a key
iii. POST request handler where a user may request all the current contents of the
key-value structure
iv. POST request handler where a user may delete a key-value pair
v. POST request handler where a user may clear then entire key-value structure
b. File upload server:
i. Request handler where a user may upload a file
ii. GET request handler where a user may request a list (text or html) of uploaded
files
iii. GET request handler where a user may request a specific file for download
