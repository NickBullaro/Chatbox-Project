# Set up React  
0. `cd ~/environment && git clone https://github.com/NJIT-CS490/project2-m1-nsb38 && cd project2-m1-nsb38`    
1. Install your stuff! :exclamation: REMEMBER `sudo` might not be needed. If it doesn't work with sudo, try without. :exclamation:
  a) `npm install`    
  b) `pip install flask-socketio`    
  c) `pip install eventlet`    
  d) `npm install -g webpack`    
  e) `npm install --save-dev webpack`    
  f) `npm install socket.io-client --save`
  g) `pip install flask`
  h) `pip install python-dotenv`
  i) `npm install -g heroku`
  j) `npm i react-google-login`
  k) `npm i react-linkify`
:warning: :warning: :warning: If you see any error messages, make sure you use `sudo pip` or `sudo npm`. If it says "pip cannot be found", run `which pip` and use `sudo [path to pip from which pip] install` :warning: :warning: :warning:    
2. If you already have psql set up, **SKIP THE REST OF THE STEPS AND JUST DO THE FOLLOWING COMMAND**: `sudo service postgresql start`    
3. Create your `sql.env`.
  
# Getting PSQL to work with Python  
  
1. Update yum: `sudo yum update`, and enter yes to all prompts    
2. Upgrade pip: `sudo /usr/local/bin/pip install --upgrade pip`  
3. Get psycopg2: `sudo /usr/local/bin/pip install psycopg2-binary`    
4. Get SQLAlchemy: `sudo /usr/local/bin/pip install Flask-SQLAlchemy==2.1`    
  
# Setting up PSQL  
  
1. Install PostGreSQL: `sudo yum install postgresql postgresql-server postgresql-devel postgresql-contrib postgresql-docs`    
    Enter yes to all prompts.    
2. Initialize PSQL database: `sudo service postgresql initdb`    
3. Start PSQL: `sudo service postgresql start`    
4. Make a new superuser: `sudo -u postgres createuser --superuser $USER`    
    :warning: :warning: :warning: If you get an error saying "could not change directory", that's okay! It worked! :warning: :warning: :warning:    
5. Make a new database: `sudo -u postgres createdb $USER`    
        :warning: :warning: :warning: If you get an error saying "could not change directory", that's okay! It worked! :warning: :warning: :warning:    
6. Make sure your user shows up:    
    a) `psql`    
    b) `\du` look for ec2-user as a user    
    c) `\l` look for ec2-user as a database    
7. Make a new user:
    a) `psql` (if you already quit out of psql)    
    ## REPLACE THE [VALUES] IN THIS COMMAND! Type this with a new (short) unique password.   
    b) I recommend 4-5 characters - it doesn't have to be very secure. Remember this password!  
        `create user [some_username_here] superuser password '[some_unique_new_password_here]';`    
    c) `\q` to quit out of sql    
8. `cd` into `project2-m2-nsb38` and make a new file called `sql.env`.
9. Add the following lines into it:
  a) SQL_USER='<user>' where <user> is the username you used in step 7b.
  b) SQL_PASSWORD='<pass>' where <pass> is the password you used in step 7b.
  c) `DATABASE_URL='postgresql://<user>:<pass>@localhost/postgres'` where <user> and <pass> are the values from previous steps.
  
  
# Seting up OAuth with Google

1. Go to `https://console.developers.google.com/`` and sign up using your google account.  
2. Click "CREATE PROJECT" or in the dropdown menu called "Select a Project" in the top, click "NEW PROJECT".   
3. Make a new project named whatever you like. It is okay if you choose "No organization".
4. Click "Credentials" in the left hand bar, then click "+ CREATE CREDENTIALS" and then click "OAuth client ID".  
4.5. If you see a warning that says "To create an OAuth client ID, you must first set a product name on the consent screen", do the following steps:  
			1. Click the "CONFIGURE CONSENT SCREEN" button.  
			2. Choose "External"  
			3. For "Application name," specify "Chatbox Program" or something similar.  
			4. Press save.  
5. Go back to Credentials -> Create Credentials -> OAuth client ID. Click "web application". Enter a name for your application.
6. In the 'Authorized Javascript Origins' section, enter your full AWS Cloud9 preview url  :warning: You must leave out the '/' at the end of the link or it will not work! :warning:
7. Once you finish and save, a popup will appear with your ClientID and your client secret. You need your clientID for the next part, however it is saved in your credentials tab in the Google Developer Console if you lose or forget it.
8. Once you have your clientID, open GoogleButton.jsx and replace the clientID string value with your own clientID.



# Enabling read/write from SQLAlchemy

There's a special file that you need to enable your db admin password to work for:  
1. Open the file in vim: `sudo vim /var/lib/pgsql9/data/pg_hba.conf`
If that doesn't work: `sudo vim $(psql -c "show hba_file;" | grep pg_hba.conf)`  
2. Replace all values of `ident` with `md5` in Vim: `:%s/ident/md5/g`  
3. After changing those lines, run `sudo service postgresql restart`  
4. Ensure that `sql.env` has the username/password of the superuser you created!
5. Now create the needed database tables- in the terminal enter:
    a) `psql`
    b) `import models`
    c) `models.db.create_all()`
    d) `models.db.session.commit()`
    e) `quit()`
6. Run your code!    
  a) `npm run watch`. If prompted to install webpack-cli, type "yes"    
  b) In a new terminal, `python app.py`    
  c) Preview Running Application (might have to clear your cache by doing a hard refresh)    


# Setting up Heroku and pushing your database to it

1. Create a heroku account at heroku.com
2. Log into heroku: `heroku login -i`
3. Create a new Heroku app: `heroku create`
4. Create Herkou postgresql: `heroku addons:create heroku-postgresql:hobby-dev`
5. Follow these steps to alter the table owner:
  a) Enter `psql` in the terminal
  b) Enter `ALTER DATABASE postgres OWNER TO <user>` where <user> is your username from 7b
  c) A message should pop up saying 'ALTER DATABASE' if it worked.
  d) Next, enter `\l` and you should see your user in the Owner column next to postgres.
6. Push your local database to Heroku: `PGUSER=<user> heroku pg:push postgres DATABASE_URL` where <user> is the same as in your DATABASE_URL in sql.env.
If that doesn't work, remove the 'PGUSER=<user>' from the command and try again.
7. Check to see if it worked: `heroku pg:psql` followed by `SELECT * FROM messages`. It should output a blank table with 2 columns.
8. Configure your PROCFILE and requrements.txt to make sure you have everything you need to run the app.
9. Push your app to Heroku: `git push heroku master`
10. Navigate to your new Heroku app!




# Technical Issues

1. One technical issue I ran into during this project was the length of the messages. The database was originally set up to allow messages up to 120 chars, but i boosted that up to 1,000 chars. If the length of the message is longer than that, sqlalchemy will throw an error. I fixed this by catching the error, rolling back the db session, and sending an error message to the database saying the user's message failed to send.

2. Another technical issue was having custom usernames be displayed next to the messages. I couldn't think of a way that could allow for this without a login page and new columns in the DB, and I saw the professor say we can just use the SIDs for m1, so I decided to do that for now. So I went about this by using each connection's socketio SID instead of custom names and hardcoding them into the database add command.

3. Another technical issue was pushing my database to heroku. Like many others, when i tried to run the pg:push command, it gave me a peer authentication error. Luckily, the solution to this problem was posted on Slack and in the class FAQ which helped me solve the issue.

4. Another technical issue was having the current user count update automatically when someone connected or disconnected. I solved this by making an emit_all_users function like the emit_all_messages function in app.py and calling it when needed. I also had to add the react hook in Content.jsx which I did by copying what we did for the messages but with users instead.

5. Another technical issue was once I made the chatbox scrollable, I needed to find out how to make the chatbox always stay scrolled all the way down when a new message was sent. I couldn't do this in the html so I looked it up and found some Javascript code that worked. Using this link, https://collaborate.pega.com/question/how-keep-scrollbar-always-bottom, I found out I needed to set the <ul> as a new variable in my updateMessages funtion in Content.jsx and set the scrollTop equal to the scrollHeight.


# Known Issues

1. I would say the one known issue I have is the lack of styling for users vs. the bot. I have it set up so the messages are sent to the DB with the .add function passing this: (the SID + data["messages"]). So, because of that, there really isn't a way for my program to discern between bot messages and user messages.


# Improvements

1. One improvement I would make would be to figure out how to allow for custom usernames when the user connects to the app. I believe I would go about it by creating another .jsx file for making a login screen of sorts. Then I would take that input, redirect to the actual chatbox page, and match that input to each SID in a dictionary like I did with the SIDs in app.py. Then, when a person sends a message, I would grab the corresponding username, and send it to the DB with the message.

2. Another improvement I would make would be having a box on the right side of the chatbox listing all the current users. I would have to create another div in the chatbox area, emit the array of SIDs (or usernames if I implemented that) to Content.jsx, and map the contents out like with the messages.

3. Another improvement I would make would be to add more functionality to the bot. I would want it to be more like a discord bot where it can do a lot more things like play music or have responses to other things like "how are you?". This would mainly be implemented through using other APIs. I would implement the other responses by creating a dictionary with pairs of questions and responses- for example {"how are you?": "I am well. How are you?"}, and parse the messages for the key, then reply with the value.




# --- Milestone 2: ---


# Technical Issues

1. One technical issue I ran into during this milestone was setting up the foreign key connection between the user's id and the messages. After some research, I found an example of how to set up a variable as a foreign key and how to use it in my app.py by using db.session.query().filter().

2. Another technical issue I ran into was how to redirect to <Content /> after the login. I figured out that all I had to do was add a ReactDOM.render call in the handleSubmit function in GoogleButton.jsx. This made it so that after the google auth was finished, it rendered <Content /> which is the main chatbox file.


# Improvements

1. One improvement I would make would be to figure out how to render images inline. I created a regex test to see if a message had an image link in it, but I couldn't figure out how to actually embed that link as an image and render it inline.

2. Another improvement I would make would be to have different styling for user messages and bot messages. I heard one way to go about it would be to create a sort of role for users and a role for the bot and send it with each message, then check the role in the message component and change the styling from there. However, I don't know exactly how I would go about that but that's why we use Google.