# PyShort 
 Ted's simple url shortener 

### DEPLYMENT STEPS 

#### Local 

1. Clone the repo
  ```
  $ git clone https://github.com/tedleyem/flask-boilerplate.git
  $ cd folder
  ```

2. Initialize and activate a virtualenv:
  ```
  $ virtualenv --no-site-packages env
  $ source env/bin/activate
  ```

3. Install the dependencies:
  ```
  $ pip install -r requirements.txt
  ```

5. Run the development server:
  ```
  $ python app.py
  ```

6. Navigate to [http://localhost:5000](http://localhost:5000)


#### Deploying to PythonAnywhere

1. Install [Git](http://git-scm.com/downloads) and [Python](http://install.python-guide.org/) - if you don't already have them, of course.

  > If you plan on working exclusively within PythonAnywhere, which you can, because it provides a cloud solution for hosting and developing your application, you can skip step one entirely. :)

2. Sign up for [PythonAnywhere](https://www.pythonanywhere.com/pricing/), if you haven't already
3. Once logged in, you should be on the Consoles tab.
4. Clone this repo:
  ```
  $ git clone git://github.com/realpython/flask-boilerplate.git
  $ cd flask-boilerplate
  ```

5. Create and activate a virtualenv:
  ```
  $ virtualenv venv --no-site-packages
  $ source venv/bin/activate
  ```

6. Install requirements:
  ```
  $ pip install -r requirements.txt
  ```

7. Next, back on PythonAnywhere, click Web tab.
8. Click the "Add a new web app" link on the left; by default this will create an app at your-username.pythonanywhere.com, though if you've signed up for a paid "Web Developer" account you can also specify your own domain name here. Once you've decided on the location of the app, click the "Next" button.
9. On the next page, click the "Flask" option, and on the next page just keep the default settings and click "Next" again.
Once the web app has been created (it'll take 20 seconds or so), you'll see a link near the top of the page, under the "Reload web app" button, saying "It is configured via a WSGI file stored at..." and a filename.  Click this, and you get to a page with a text editor.
10. Put the following lines of code at the start of the WSGI file (changing "your-username" appropriately)

  ```
  activate_this = '/home/your-username/flask-boilerplate/venv/bin/activate_this.py'
  execfile(activate_this, dict(__file__=activate_this))
  ```

11. Then update the following lines of code:

  from

  ```
  project_home = u'/home/your-username/mysite'
  ```

  to

  ```
  project_home = u'/home/your-username/flask-boilerplate'
  ```

  from

  ```
  from flask_app import app as application
  ```

  to

  ```
  from app import app as application
  ```

12. Save the file.
13. Go to the website http://your-username.pythonanywhere.com/ (or your own domain if you specified a different one earlier), and you should see something like this - [http://www.flaskboilerplate.com/](http://www.flaskboilerplate.com/).

*Now you're ready to start developing!*

***Need to PUSH your PythonAnywhere repo to Github?***

1. Start a bash console
2. Run:

  ```
  $ ssh-keygen -t rsa
  ```

3. Just accept the defaults, then show the public key:

  ```
  $ cat ~/.ssh/id_rsa.pub
  ```

4. Log in to GitHub.
5. Go to the "Account settings" option at the top right (currently a wrench and a screwdriver crossed)
6. Select "SSH Keys" from the list at the left.
7. Click the "Add SSH key" button at top right.
8. Enter a title (I suggest something like "From PythonAnywhere" and then paste the output of the previous "cat" command into the Key box.
9. Click the green "Add key" button.  You'll be prompted to enter your password.

PUSH and PULL away!

### What's next?

1. Using Heroku? Make sure you deactivate your virtualenv once you're done deploying: `deactivate`
2. Need to reactivate? (1) Unix - `source venv/bin/activate` (2) Windows - `venv\scripts\activate`
4. Add your Google Analytics ID to the *main.html* file
5. Add a domain name to [Heroku](https://devcenter.heroku.com/articles/custom-domains) or PythonAnywhere via a [CNAME](http://en.wikipedia.org/wiki/CNAME_record) record
5. DEVELOP YOUR APP - need [help](http://realpython.com)?

### My Resources

* [PythonAnywhere - Help](https://www.pythonanywhere.com/help/)
* [Flask Documentation](http://flask.pocoo.org/docs/)
* [Flask Extensions](http://flask.pocoo.org/extensions/)
* [Real Python](http://www.realpythonfortheweb.com) :)

