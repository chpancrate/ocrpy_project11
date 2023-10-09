# gudlift-registration

# Why

This is a proof of concept (POC) project to show a light-weight version of our competition booking platform. The aim is the keep things as light as possible, and use feedback from the users to iterate.

# Getting Started

This project uses the following technologies:

* Python v3.x+

* [Flask](https://flask.palletsprojects.com/en/1.1.x/)
    Whereas Django does a lot of things for us out of the box, Flask allows us to add only what we need. 

* [Virtual environment](https://virtualenv.pypa.io/en/stable/installation.html)
    This ensures you'll be able to install the correct packages without interfering with Python on your machine.
    Before you begin, please ensure you have this installed globally. 

# Installation
- After cloning, change into the directory and type <code>virtualenv .</code>. This will then set up a a virtual python environment within that directory.
- Next, type <code>source bin/activate</code>. You should see that your command prompt has changed to the name of the folder. This means that you can install packages in here without affecting affecting files outside. To deactivate, type <code>deactivate</code>

- Rather than hunting around for the packages you need, you can install in one step. Type <code>pip install -r requirements.txt</code>. This will install all the packages listed in the respective file. If you install a package, make sure others know by updating the requirements.txt file. An easy way to do this is <code>pip freeze > requirements.txt</code>

- Flask requires that you set an environmental variable to the python file. However you do that, you'll want to set the file to be <code>server.py</code>. Check [here](https://flask.palletsprojects.com/en/1.1.x/quickstart/#a-minimal-application) for more details

- You should now be ready to test the application. In the directory, type either <code>flask run</code> or <code>python -m flask run</code>. The app should respond with an address you should be able to go to using your browser.

# Current Setup

The app is powered by [JSON files](https://www.tutorialspoint.com/json/json_quick_guide.htm). This is to get around having a DB until we actually need one. The main ones are:
    
* competitions.json - list of competitions
* clubs.json - list of clubs with relevant information. You can look here to see what email addresses the app will accept for login.

# Testing

You are free to use whatever testing framework you like-the main thing is that you can show what tests you are using.

We also like to show how well we're testing, so there's a module called 
[coverage](https://coverage.readthedocs.io/en/coverage-5.1/) you should add to your project.

All commands below should be launched from the application directory (where server.py is located). All used testing modules are listed in requirements.txt (you can install all neded modules with <code>pip install -r requirements.txt </code>)

## Unit tests
All unit test are located in ./tests/unit/. In order to launch them from the application directory you need to install pytest and use the command :
```
pytest ./tests/unit/
```

## Integration Tests
In order to run the integration test you need to copy the clubs_test.json and competitions_test.json located in ./json files/ in the directory ./tests/integration/. This ensure you use proper test data. As the test modify the files it has to be done before each test. In order to launch the integration test use the command :
```
pytest .\tests\integration\test_happy_path.py
```

## Functionnal tests
The functionnal test use **selenium**. You should ensure that it is installed.
To ensure correct test data are used, the file clubs.json and competitions.json located in ./json files/ should be copied in the application directory. The application should be run using <code>flak run</code> before starting the selenium tests. The command to launch the test are : 
```
pytest .\tests\functional\test_selenium_happy_path.py
pytest .\tests\functional\test_selenium_errors_messages.py
```
Information about selenium can be found here : https://www.selenium.dev

## Performance tests
The performance tests use **locust**, the module should be installed. The application should be run using <code>flak run</code> before starting the locust tests.
Launch the locust platform with :
```
locust -f .\tests\performance\locustfile.py
```
The locust tool can be accessed with http://localhost:8089/

Information about locust can be found here : https://locust.io

## Test coverage
The test coverage uses the **coverage** module. You can launch the coverage check with :
```
coverage run -m pytest .\tests\unit\
```
You can generate an html report with:
```
coverage html
```
You can acces it with ./htmlcov/index.html

## Test reports
For easy access sample screenshots of tests reports are provided in ./tests reports/

