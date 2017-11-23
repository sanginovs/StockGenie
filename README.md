[TOC]
#Installation#
## Requirements ##
* python 2.7
* linux, unix, mac, windows(with attachments)
* git 

## Creating Development Environment ##

1. **Fork** the reposistory from BitBucket and rename to your project.

2. If working on a **local machine**, then clone the repo from your terminal

``` bash
git clone https://username@bitbucket.org/username/repositoryname.git
source setup.sh
python app.py
```
You can now check your localhost to see if it deployed correctly.

3. If working on a **cloud9** account follow instructions below to create a new workspace
    1. Input your project name and description
    2. Get the git URL of your forked repository from BitBucket
    3. You should get the SSH URL, it should look something like: git@bitbucket.org:username/repositoryname.git
    4. Now paste the git URL into "Clone from Git URL" field in cloud9

3b. Next, you will need to set up your Linux environment for Python development. You only need to do this once.

```bash
sudo apt-get install python-virtualenv python-dev python-yaml
```

3c. Whenever you start a new session, you'll need to "source" the setup.sh file, which gets your Terminal ready for Flask development and testing. You do this by "sourcing" it. After your source the setup script, you can then run your application.

``` bash
source setup.sh
python app.py
``` 
If you are succesful you will see something like:
``` bash
Starting application
Running server at http://0.0.0.0:8080/
```
Click the link in your terminal to check if it deployed correctly.

# Working with the flask template #
## File Hierarchy ##
```
- Project Name
   - App
      -static
      -templates
        -start.html
      - __init__.py
      - allImports.py
      - config.yaml
      - models.py
      - start.py # this an example of a python file that renders a page
   - Data
       - db.sqlite
   - Venv
   - app.py
   - create_db.py
   - setup.sh
```
Above you will find the file structure for the flask template. You will be mostly working with the app/ directory.
Some **important** files and directories.

* models.py - This file contains the database schema or the tables and columns that will be in database.
If you want to make a new table then you will add a class to this file, see the example in the models.py file.
Once you are done making changes to this file run create_db.py to make the changes in the database.

* App/ directory - This directory will contain a python module. In order for python files to be recognized they must be added to the \_\_init\_\_.py file in this directory.

* start.py - This file is a very quick example of a python file that will render a page. This file processes and renders the start.html file located under templates.

## Example for creating a new view ##
If I wanted to create a new webpage then I would do the following.

* Create your python file inside of the app/ directory. Here you will include the decorator @app.route as seen in other files
```python
        from allImports import *
        @app.route("/example", methods = ["GET"])
        def example():
            return render_template("example.html", cfg = cfg)
```
* Create HTML file inside of the templates folder and make sure to give it the **same name** as the one you used in the python file.
```HTML
{% extends "base.html" %}

{% block body %}

<h1> Header 1 </h1>
<p> Example Paragraph </p>

{% endblock %}
```
* Import the python file you created inside the \_\_init\_\_.py file.
```Python
from app import example.py
```

## Reading and Writing to the database ##

In order to read from a database you will need to make a query to get the data. You can find out more about queries at [the peewee site](http://docs.peewee-orm.com/en/latest/peewee/querying.html)
one quick example of a query would be the following:
```python
query = tableName.get( condition = something )
```
This will return a python object that will have the data as attributes. You can pass this object to the html file. You can access this data by typing query.Column. 

## Documentation links ##

* [Jinja Documentation](http://jinja.pocoo.org/)
* [Peewee Documentation](http://docs.peewee-orm.com/en/latest/)
* [Git documentation](https://git-scm.com/documentation)
* [Flask Documentation](http://flask.pocoo.org/docs/0.10/)