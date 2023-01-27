<h3>INFORMATION:</h3>
<p>The new user is named al.<br>
The files requested were left under ~/home/al/<br>
The server file is at /home/al/github/MaxTest/https_server/https_server.py<br>
Run it with:  sudo python3 https_server.py<br>
I created a service that runs that command on startup so theoretically my website should always be up; however, I have noticed the site stop responding after a period of time and the service needs to be restarted.<br>
The service can be restarted with:  sudo systemctl restart al-https-server.service<br>
The URL to my website is:  https://alrobison.com<br>
You can also get to https://alrobison.com/users for a JSON structure, or https://alrobison.com/files for a file upload page.<br>
For the things I was not able to complete, I left files and pieces of non-working code simply to show that I worked on them and what sort of paths I took.<br>
</p>


<p>
<h3>TASKS COMPLETED:</h3>
Using server, username, and password details provided to you, connect to your assigned server using ssh.<br>
Create a new user account as the username of your choice<br>
Login as that new user<br>
In your home directory, create a new directory called “memories”. Inside of it, create a text file which describes your favorite memory. Set the file access to full permissions for all the system (777).<br>
Create a shell script which does the following:<br>
a. Makes a copy of your memories file, naming it “privatemems”<br>
b. Sets permissions of the new file to 755<br>
c. Appends to the file the current system time<br>
Create a local git repository<br>
a. You may do this either starting locally and pushing to an origin (online) location of your choice, or you may create it online first and clone it to your home directory.<br>
Using the language you are most comfortable with, create an HTTPS (you’ll need to generate a keypair) server application...<br>
Make sure to regularly commit changes in your local repo while developing and push those changes to your online repository.<br>
STRETCH GOAL 1. Configure system’s firewall to only allow SSH and HTTPS connections<br>
STRETCH GOAL 2. Get a free domain name for the host ( https://www.noip.com/ is an option)<br>
STRETCH GOAL 3. Get a LetsEncrypt SSL certificate for your server so that it stops complaining about your unsigned certificate (requires a domain name)<br>
Email/call/message me.
</p>

<p>
<h3>TASKS NOT COMPLETED:</h3>
<ol>
<li>Key-value server:</li>
	<ol>
	<li>POST request handler where a user may specify a value to be stored under a key</li>
	<li>POST request handler where a user may request the value for a key</li>
	<li>POST request handler where a user may request all the current contents of the key-value structure</li>
	<li>POST request handler where a user may delete a key-value pair</li>
	<li>POST request handler where a user may clear then entire key-value structure</li>
	</ol>
<li>File upload server:</li>
	<ol>
	<li>Request handler where a user may upload a file</li>
	<li>GET request handler where a user may request a list (text or html) of uploaded files</li>
	<li>GET request handler where a user may request a specific file for download</li>
	</ol>
</ol>
</p>

<p>
<h3>PROBLEMS ENCOUNTERED:</h3>
My biggest challenges were:<br>
<ol>
<li>Figuring out how to use user input to parse JSON data.</li>
<li>On the server side, figuring out how to get the data sent by a POST request.</li>
</ol>
For these reasons, I was not able to complete the POST Request tasks nor the file upload tasks, regrettably.<br>
I feel like I would eventually get them both with enough time, but what can you do? I'm not experienced with either of these tasks :)<br>
</p>
