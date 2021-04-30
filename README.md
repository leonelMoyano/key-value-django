# key-value-django
`key-value-django` is an example project that stores key-value pairs recieved through
websocket communication and exposes said values through a REST HTTP endpoint
## Tech/Frameworks used
Complete dependencies on `requirements.txt`
- Python 3.6.9
- Django 3.2
- channels 3.0.3
- pytest 6.2.3
- daphne 3.0.2
## API
### WebSocket
#### /ws/storage/
Message body: `{"key":{key},"value":{value}}`

Will reply `{"message": "{key} created", "status": 200}` if succesfully processed
### HTTP
#### /storage/*{key}*
200 response when key is found
```
{
  "key": "{key}",
  "value": "{value}",
  "message": "",
  "status": 200
}
```
404 response when key is not found 
```
{
  "message": "No value found for key {key}",
  "status": 404
}
```
### Considerations
Values to be stored in this project were only considered to be string
due to database limitations, backend storage is handled with `mysql`.

### Installation
Create the virtual environment and install dependencies
```
git clone {project url}
cd key-value-django 
virtualenv venv
source venv/bin/activate
pip install requirements.txt
```
Let's install the database packages, and get into the mysql shell
```
sudo apt-get install mysql-server libmysqlclient-dev
sudo mysql
```
Inside the mysql shell we'll create the database, create the user for 
this django project and grant it privileges
```
CREATE DATABASE keyvaluedjango CHARACTER SET UTF8;
CREATE USER keyvaluedjango@localhost IDENTIFIED BY 'zaqwsxcde123';
GRANT ALL PRIVILEGES ON keyvaluedjango.* TO keyvaluedjango@localhost;
exit
```
To finish off the database setup let's run the django migrations to create
the schema in our fresh mysql db
```
python manage.py migrate
```
Once migrations finish, the project can be run with
```
daphne config.asgi:application
```

You may now verify everything is working as intended. Since part of this project
communicates through websocket, I included simple .html file to serve as a basic client
for the purpose of testing (can be found at `misc/wstest.html`).

### Tests
Can be run by:

```
source venv/bin/activate
pytest
```

Test suite contains:
-  Integration tests first storing values through WS and later retrieving through HTTP, at `apps.storage.test_integration`
-  Model tests for expected constraints, at `apps.storage.test_models`
-  View tests for REST API behaviour, at `apps.storage.test_views`
