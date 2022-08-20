# Django-DRF-UserAPI

Python Flask RESTful Server



## Installation	

### Requirements

* Python 3.8 or higher


### Install
Clone git repository

	$ git clone https://github.com/HJSAMO/Flask-RESTful-Postgres.git
  
Generate virtual environment (Optional)

	$ virtualenv venv
	$ source venv/bin/activate

Generate config file(.env)

	$ cat .env
	  WEB_HOST = "localhost"
	  WEB_PORT = "5000"
	  RDB_HOST = "localhost"
	  RDB_PORT = "5432"
	  RDB_DBNAME = "dbname"
	  RDB_USER = "user"
	  RDB_PASSWORD = "password"
  
Install all required libraries

	$ pip install -r requirements.txt

  
### Start a server for development
	$ python apps.py
	

## API manual

Get statistics

	url = http://localhost:5000/v1/stats
	method = GET

Get Concept Table Information

	url = http://localhost:5000/v1/concept
	method = GET
	params = {
        "keyword" : "",
		"page" : ""
    }

Get Concept Table Information

	url = http://localhost:5000/v1/data/<table_name>
	method = GET
	params = {
        "column" : "",
        "keyword" : "",
		"page" : ""
    }

# TODO

Test Code

Tuning

Add more statistics

Keyword Search : Exact > Like