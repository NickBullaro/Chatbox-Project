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
8. `cd` into `project2-m1-nsb38` and make a new file called `sql.env`.
9. Add the following lines into it:
  a) SQL_USER='<user>' where <user> is the username you used in step 7b.
  b) SQL_PASSWORD='<pass>' where <pass> is the password you used in step 7b.
  c) `DATABASE_URL='postgresql://<user>:<pass>@localhost/postgres'` where <user> and <pass> are the values from previous steps.
  
  
# Enabling read/write from SQLAlchemy

There's a special file that you need to enable your db admin password to work for:  
1. Open the file in vim: `sudo vim /var/lib/pgsql9/data/pg_hba.conf`
If that doesn't work: `sudo vim $(psql -c "show hba_file;" | grep pg_hba.conf)`  
2. Replace all values of `ident` with `md5` in Vim: `:%s/ident/md5/g`  
3. After changing those lines, run `sudo service postgresql restart`  
4. Ensure that `sql.env` has the username/password of the superuser you created!  
5. Run your code!    
  a) `npm run watch`. If prompted to install webpack-cli, type "yes"    
  b) In a new terminal, `python app.py`    
  c) Preview Running Application (might have to clear your cache by doing a hard refresh)    


# Setting up Heroku and pushing your database to it

1. Log into heroku: `heroku login -i`
2. Create a new Heroku app: `heroku create`
3. Create Herkou postgresql: `heroku addons:create heroku-postgresql:hobby-dev`
4. Follow these steps to alter the table owner:
  a) Enter `psql` in the terminal
  b) Enter `ALTER DATABASE postgres OWNER TO <user>` where <user> is your username from 7b
  c) A message should pop up saying 'ALTER DATABASE' if it worked.
  d) Next, enter `\l` and you should see your user in the Owner column next to postgres.
4. Push your local database to Heroku: `PGUSER=<user> heroku pg:push postgres DATABASE_URL` where <user> is the same as in your DATABASE_URL in sql.env.
If that doesn't work, remove the 'PGUSER=<user>' from the command and try again.
5. Check to see if it worked: `heroku pg:psql` followed by `SELECT * FROM messages`. It should output a blank table with 2 columns.
6. Configure your PROCFILE and requrements.txt to make sure you have everything you need to run the app.
7. Push your app to Heroku: `git push heroku master`
8. Navigate to your new Heroku app!




# Known Issues

1. One known issue with this project was the length of the messages. The databasewas originally set up to allow messages up to 120 chars, but i boosted that up to 1,000 chars. If the length of the message is longer than that, sqlalchemy will throw an error. I fixed this by catching the error, rolling back the db session, and sending an error message to the database saying the user's message failed to send.

2. Another known issue was having usernames be displayed next to the messages. I solved this by using each connection's socketio SID instead of custom names and hardcoding them into the database add command.

3. Another known issue is 

4. Another known issue is 

5. Another known issue is 



# Improvements

1. One improvement I would make would be to figure out how to allow for custom usernames when the user connects to the app. I believe I would go about it by creating another .jsx file for making a log in screen of sorts. Then I would take that input, redirect to the actual chatbox page, and match that input to each SID in a dictionary. Then, when a person sends a message, I would grab the corresponding username, and send it to the DB with the message.

2. Another improvement I would make would be having a box on the right side of the chatbox listing all the current users. I would have to create another div in the chatbox area, emit the array of SIDs to content, and map the contents out like with the messages.

3. Another improvement I would make would be 